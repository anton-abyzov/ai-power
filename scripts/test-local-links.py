#!/usr/bin/env python3
"""
Test all links on the local MkDocs site
"""

import asyncio
from playwright.async_api import async_playwright
import subprocess
import time

# Start local MkDocs server
def start_mkdocs_server():
    """Start MkDocs dev server"""
    process = subprocess.Popen(
        ["mkdocs", "serve", "--no-livereload"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Wait for server to start
    time.sleep(5)
    return process

# Pages to check
PAGES = [
    "/",
    "/episodes/01-portfolio-no-code/",
    "/episodes/01-portfolio-no-code/content/00-introduction/",
    "/episodes/01-portfolio-no-code/content/01-obsidian-setup/",
    "/episodes/01-portfolio-no-code/content/02-ai-tools-landscape/",
    "/episodes/01-portfolio-no-code/content/03-claude-code-install/",
    "/episodes/01-portfolio-no-code/content/claude-commands/",
    "/episodes/01-portfolio-no-code/content/04-agent-creation/",
    "/episodes/01-portfolio-no-code/content/05-portfolio-prep/",
    "/episodes/01-portfolio-no-code/content/06-master-prompt/",
    "/episodes/01-portfolio-no-code/content/07-github-deploy/",
    "/episodes/01-portfolio-no-code/content/08-closing/"
]

async def test_navigation(page, base_url):
    """Test navigation links on a page"""
    nav_links = await page.query_selector_all(".navigation-footer a")
    issues = []

    for link in nav_links:
        href = await link.get_attribute("href")
        text = await link.inner_text()

        if href and not href.startswith("http"):
            # Try to navigate to the link
            try:
                # Get the full URL
                full_url = await link.evaluate("(el) => el.href")
                response = await page.goto(full_url, wait_until="domcontentloaded", timeout=5000)

                if response and response.status == 404:
                    issues.append(f"  ❌ 404: {text.strip()} -> {href}")
                else:
                    print(f"  ✅ OK: {text.strip()} -> {href}")
            except Exception as e:
                issues.append(f"  ❌ Error: {text.strip()} -> {href}: {str(e)}")

    return issues

async def test_page_lists(page):
    """Check if lists are displayed with bullets"""
    # Check content lists (not navigation)
    lists = await page.query_selector_all(".md-typeset ul:not(.md-nav__list)")

    if lists:
        first_list = lists[0]
        list_style = await first_list.evaluate("""
            (el) => window.getComputedStyle(el).listStyleType
        """)

        if list_style == "none":
            return "⚠️ Lists missing bullets"

    return None

async def test_all_pages():
    """Test all pages on local server"""
    BASE_URL = "http://127.0.0.1:8000"

    print("🚀 Starting MkDocs server...")
    server = start_mkdocs_server()

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            all_issues = []

            for path in PAGES:
                url = BASE_URL + path
                print(f"\n📄 Testing: {path}")

                try:
                    response = await page.goto(url, wait_until="networkidle", timeout=10000)

                    # Check page loads
                    if response.status == 404:
                        print(f"  ❌ 404 Page Not Found")
                        all_issues.append(f"{path}: 404")
                        continue
                    else:
                        print(f"  ✅ Page loads OK")

                    # Check lists
                    list_issue = await test_page_lists(page)
                    if list_issue:
                        print(f"  {list_issue}")
                        all_issues.append(f"{path}: {list_issue}")

                    # Test navigation links
                    nav_issues = await test_navigation(page, BASE_URL)
                    if nav_issues:
                        for issue in nav_issues:
                            print(issue)
                            all_issues.append(f"{path}: {issue}")

                    # Test "Start Learning Now" button on index
                    if path == "/episodes/01-portfolio-no-code/":
                        start_button = await page.query_selector("a.md-button--primary")
                        if start_button:
                            href = await start_button.get_attribute("href")
                            # Try clicking it
                            await start_button.click()
                            await page.wait_for_load_state("networkidle")

                            current_url = page.url
                            if "404" in current_url or "not-found" in current_url:
                                print(f"  ❌ 'Start Learning Now' button -> 404")
                                all_issues.append(f"{path}: Start Learning button -> 404")
                            else:
                                print(f"  ✅ 'Start Learning Now' button works")

                            # Go back for next test
                            await page.goto(url)

                except Exception as e:
                    print(f"  ❌ Error: {str(e)}")
                    all_issues.append(f"{path}: {str(e)}")

            print("\n" + "="*60)
            print("📊 SUMMARY:\n")

            if not all_issues:
                print("✅ All pages and links working correctly!")
            else:
                print(f"❌ Found {len(all_issues)} issues:\n")
                for issue in all_issues:
                    print(f"  - {issue}")

            await browser.close()

    finally:
        # Stop MkDocs server
        print("\n🛑 Stopping MkDocs server...")
        server.terminate()
        server.wait()

if __name__ == "__main__":
    asyncio.run(test_all_pages())