#!/usr/bin/env python3
"""
Verify all pages on the deployed GitHub Pages site using Playwright
"""

import asyncio
from playwright.async_api import async_playwright
import time

BASE_URL = "https://anton-abyzov.github.io/ai-power"

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
    "/episodes/01-portfolio-no-code/content/08-closing/",
    "/episodes/01-portfolio-no-code/prompts/agent-definition/",
    "/episodes/01-portfolio-no-code/prompts/master-prompt/",
    "/episodes/RESOURCES/",
    "/community/showcase/",
    "/community/contributions/"
]

async def check_page(page, url):
    """Check a single page for issues"""
    full_url = BASE_URL + url
    issues = []

    try:
        # Navigate to page
        response = await page.goto(full_url, wait_until="networkidle")

        # Check status code
        if response.status != 200:
            issues.append(f"❌ HTTP {response.status}")

        # Check for 404 page
        title = await page.title()
        if "404" in title or "Not Found" in title:
            issues.append(f"❌ 404 Page")

        # Check for broken images (SVGs)
        images = await page.query_selector_all("img")
        for img in images:
            src = await img.get_attribute("src")
            if src:
                # Check if image loaded successfully
                is_broken = await img.evaluate("""
                    (img) => {
                        return !img.complete || img.naturalHeight === 0;
                    }
                """)
                if is_broken:
                    issues.append(f"❌ Broken image: {src}")

        # Check for JavaScript errors
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        # Check navigation links
        nav_links = await page.query_selector_all(".navigation-footer a")
        for link in nav_links:
            href = await link.get_attribute("href")
            if href and not href.startswith("http"):
                # Try to click and see if it leads to 404
                # (We'll just note the href for now)
                pass

        # Check if lists are visible
        lists = await page.query_selector_all("ul li, ol li")
        if lists:
            # Check if list items have bullets/numbers visible
            first_list = lists[0] if lists else None
            if first_list:
                list_style = await first_list.evaluate("""
                    (el) => window.getComputedStyle(el).listStyleType
                """)
                if list_style == "none":
                    issues.append(f"⚠️  Lists may not display bullets")

        if not issues:
            return f"✅ OK"
        else:
            return " | ".join(issues)

    except Exception as e:
        return f"❌ Error: {str(e)}"

async def main():
    print(f"\n🔍 Verifying GitHub Pages site: {BASE_URL}\n")
    print("=" * 80)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Enable console logging
        page.on("console", lambda msg: print(f"Console: {msg.text}") if msg.type == "error" else None)

        results = []
        for url in PAGES:
            print(f"Checking {url}... ", end="", flush=True)
            result = await check_page(page, url)
            results.append((url, result))
            print(result)
            await asyncio.sleep(0.5)  # Be nice to the server

        print("\n" + "=" * 80)
        print("\n📊 SUMMARY:\n")

        ok_count = sum(1 for _, r in results if "✅" in r and "❌" not in r)
        error_count = sum(1 for _, r in results if "❌" in r)
        warning_count = sum(1 for _, r in results if "⚠️" in r)

        print(f"✅ Pages OK: {ok_count}/{len(PAGES)}")
        if error_count > 0:
            print(f"❌ Pages with errors: {error_count}")
        if warning_count > 0:
            print(f"⚠️  Pages with warnings: {warning_count}")

        if error_count > 0:
            print("\n🔴 Pages with issues:")
            for url, result in results:
                if "❌" in result or "⚠️" in result:
                    print(f"  {url}: {result}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())