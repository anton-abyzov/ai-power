#!/usr/bin/env python3
"""Test script for GitHub AI Power MkDocs site"""

import time
from playwright.sync_api import sync_playwright

def test_site():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # Test homepage
            print("Testing homepage...")
            page.goto('http://localhost:8000', wait_until='networkidle')

            # Take screenshot of homepage
            page.screenshot(path='/Users/antonabyzov/Downloads/mkdocs-homepage.png')
            print("✓ Homepage loaded and screenshot saved")

            # Test "Start Learning Now" button
            print("Testing navigation...")
            page.click('a:has-text("Start Learning Now")', timeout=5000)
            page.wait_for_load_state('networkidle')

            # Check if we're on the episode page
            current_url = page.url
            assert 'portfolio' in current_url.lower(), f"Navigation to episode failed. URL: {current_url}"
            print(f"✓ Navigation to episode works: {current_url}")

            # Take screenshot of episode page
            page.screenshot(path='/Users/antonabyzov/Downloads/mkdocs-episode-page.png')
            print("✓ Episode page screenshot saved")

            # Check for 404 errors
            page_content = page.content()
            assert "404" not in page.title(), "404 error found!"
            assert "Not found" not in page_content, "Page not found error!"
            print("✓ No 404 errors")

            # Test bottom CTA button
            page.goto('http://localhost:8000', wait_until='networkidle')
            page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(0.5)

            # Click the bottom "Start Episode 01 Now" button
            page.click('a:has-text("Start Episode 01 Now")', timeout=5000)
            page.wait_for_load_state('networkidle')

            current_url = page.url
            assert 'portfolio' in current_url.lower(), f"Bottom CTA navigation failed. URL: {current_url}"
            print(f"✓ Bottom CTA button works: {current_url}")

            # Test diagram viewer link
            page.click('a:has-text("View All Diagrams")', timeout=5000)
            page.wait_for_load_state('networkidle')
            page.screenshot(path='/Users/antonabyzov/Downloads/mkdocs-diagrams-page.png')
            print("✓ Diagram page works")

            print("\n✅ All tests passed!")
            print("📸 Screenshots saved to Downloads folder:")
            print("  - mkdocs-homepage.png")
            print("  - mkdocs-episode-page.png")
            print("  - mkdocs-diagrams-page.png")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            page.screenshot(path='/Users/antonabyzov/Downloads/mkdocs-error.png')
            print("Error screenshot saved to mkdocs-error.png")

        finally:
            browser.close()

if __name__ == "__main__":
    test_site()