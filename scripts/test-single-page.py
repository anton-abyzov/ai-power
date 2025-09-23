#!/usr/bin/env python3
"""
Test a single page to debug issues
"""

import asyncio
from playwright.async_api import async_playwright

BASE_URL = "https://anton-abyzov.github.io/ai-power"

async def test_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Show browser
        page = await browser.new_page()

        # Test the index page with broken images
        url = f"{BASE_URL}/episodes/01-portfolio-no-code/"
        print(f"Testing: {url}\n")

        await page.goto(url, wait_until="networkidle")

        # Check all images
        images = await page.query_selector_all("img")
        print(f"Found {len(images)} images:\n")

        for i, img in enumerate(images):
            src = await img.get_attribute("src")
            alt = await img.get_attribute("alt")
            is_loaded = await img.evaluate("(img) => img.complete && img.naturalHeight > 0")

            print(f"  Image {i+1}:")
            print(f"    Alt: {alt}")
            print(f"    Src: {src}")
            print(f"    Loaded: {'✅' if is_loaded else '❌'}")

            if not is_loaded:
                # Try to get the actual URL it's trying to load
                full_url = await img.evaluate("(img) => img.src")
                print(f"    Full URL: {full_url}")
            print()

        # Check lists
        lists = await page.query_selector_all("ul, ol")
        print(f"Found {len(lists)} lists:")

        for i, lst in enumerate(lists):
            list_type = await lst.evaluate("(el) => el.tagName.toLowerCase()")
            items_count = await lst.evaluate("(el) => el.querySelectorAll('li').length")
            list_style = await lst.evaluate("(el) => window.getComputedStyle(el).listStyleType")

            print(f"  List {i+1} ({list_type}):")
            print(f"    Items: {items_count}")
            print(f"    List style: {list_style}")

        # Wait for user to inspect
        print("\nPress Enter to close browser...")
        await asyncio.sleep(30)  # Keep browser open for 30 seconds

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_page())