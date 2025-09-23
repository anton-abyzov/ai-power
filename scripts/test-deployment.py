#!/usr/bin/env python3
"""
Test deployed GitHub Pages site navigation and lists
"""

import asyncio
from playwright.async_api import async_playwright

BASE_URL = "https://anton-abyzov.github.io/ai-power"

async def test_episode_page():
    """Test the main episode page"""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Show browser
        page = await browser.new_page()

        url = f"{BASE_URL}/episodes/01-portfolio-no-code/"
        print(f"🔍 Testing: {url}\n")

        await page.goto(url, wait_until="networkidle")

        # Test "Start Learning Now" button
        print("Testing 'Start Learning Now' button...")
        start_button = await page.query_selector("a.md-button--primary")
        if start_button:
            href = await start_button.get_attribute("href")
            print(f"  Button href: {href}")

            # Click and see where it goes
            await start_button.click()
            await page.wait_for_load_state("networkidle")

            current_url = page.url
            title = await page.title()

            if "404" in title or "Not Found" in title:
                print(f"  ❌ Button leads to 404!")
            else:
                print(f"  ✅ Button works! Goes to: {current_url}")
                print(f"  Page title: {title}")

        # Go back to test lists
        await page.goto(url)

        # Check list display
        print("\nChecking list formatting...")
        lists = await page.query_selector_all(".md-typeset ul:not(.md-nav__list)")

        for i, lst in enumerate(lists[:3]):  # Check first 3 lists
            list_style = await lst.evaluate("(el) => window.getComputedStyle(el).listStyleType")
            items = await lst.query_selector_all("li")
            text = (await items[0].inner_text()) if items else "No items"

            print(f"  List {i+1}:")
            print(f"    Style: {list_style}")
            print(f"    First item: {text[:50]}...")

        # Test navigation on introduction page
        print("\nTesting Introduction page navigation...")
        intro_link = await page.query_selector('a[href*="00-introduction"]')
        if intro_link:
            await intro_link.click()
            await page.wait_for_load_state("networkidle")

            # Check Next button
            next_button = await page.query_selector('.navigation-footer a[href*="obsidian-setup"]')
            if next_button:
                next_text = await next_button.inner_text()
                print(f"  Next button text: {next_text}")

                await next_button.click()
                await page.wait_for_load_state("networkidle")

                current_url = page.url
                if "obsidian-setup" in current_url and "404" not in await page.title():
                    print(f"  ✅ Next navigation works!")
                else:
                    print(f"  ❌ Next navigation broken! URL: {current_url}")

        print("\n" + "="*60)
        print("Keep browser open for 20 seconds for manual inspection...")
        await asyncio.sleep(20)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_episode_page())