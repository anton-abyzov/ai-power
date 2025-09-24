#!/usr/bin/env python3
"""
End-to-end tests for MkDocs site navigation.
Tests that all navigation links work correctly and there are no 404 errors.
"""

import pytest
from playwright.sync_api import sync_playwright, expect
import time

# Base URL for testing - change to production URL when testing deployed site
BASE_URL = "http://127.0.0.1:8000/ai-power"
# Production URL for GitHub Pages
PROD_URL = "https://anton-abyzov.github.io/ai-power"

# Set to True to test production site, False to test local
TEST_PRODUCTION = False

def get_base_url():
    """Get the base URL based on test configuration."""
    return PROD_URL if TEST_PRODUCTION else BASE_URL

class TestNavigation:
    """Test suite for navigation functionality."""

    @pytest.fixture(scope="class")
    def browser_context(self):
        """Create a browser context for testing."""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            yield context
            browser.close()

    def test_introduction_page_loads(self, browser_context):
        """Test that the introduction page loads correctly."""
        page = browser_context.new_page()
        url = f"{get_base_url()}/episodes/01-portfolio-no-code/content/00-introduction/"
        response = page.goto(url)

        assert response.status == 200, f"Expected 200, got {response.status} for {url}"

        # Check page title contains expected text
        page_title = page.title()
        assert "Introduction" in page_title or "Hook" in page_title, f"Page title doesn't contain expected text: {page_title}"

        # Check that content exists
        heading = page.locator("h1").first
        expect(heading).to_be_visible()

        page.close()

    def test_checklist_displays_correctly(self, browser_context):
        """Test that checklist items display as a proper list, not inline."""
        page = browser_context.new_page()
        url = f"{get_base_url()}/episodes/01-portfolio-no-code/content/00-introduction/"
        page.goto(url)

        # Find the "In the next hour" text
        content = page.locator("text=In the next hour").first
        expect(content).to_be_visible()

        # Check that checklist items are in a list (ul or ol element)
        # Look for list items near the "In the next hour" text
        list_container = page.locator("ul").filter(has_text="Custom design")

        if list_container.count() > 0:
            # Good - it's in a proper list
            list_items = list_container.locator("li")
            assert list_items.count() == 4, f"Expected 4 list items, found {list_items.count()}"

            # Check each item contains expected text
            expected_items = [
                "Custom design",
                "Interactive features",
                "Deployed live",
                "Yours forever"
            ]

            for expected in expected_items:
                item = list_container.locator(f"li:has-text('{expected}')")
                expect(item).to_be_visible()
        else:
            # Check if items are inline (bad)
            content_text = page.locator("text=In the next hour").first.text_content()
            # If all checklist items appear in a single line or paragraph, it's wrong
            pytest.fail("Checklist items are not displayed as a proper list")

        page.close()

    def test_navigation_next_button(self, browser_context):
        """Test that the Next navigation button works correctly."""
        page = browser_context.new_page()

        # Start at introduction page
        url = f"{get_base_url()}/episodes/01-portfolio-no-code/content/00-introduction/"
        page.goto(url)

        # Find and click the Next button
        next_button = page.locator("a:has-text('Obsidian Setup')").first
        expect(next_button).to_be_visible()

        # Get the href to verify it's correct
        href = next_button.get_attribute("href")
        # Check that href ends with the correct path (could be relative or absolute)
        assert href.endswith("01-obsidian-setup/") or href == "../01-obsidian-setup/", f"Next button has wrong href: {href}"

        # Click and verify navigation
        next_button.click()
        page.wait_for_load_state("networkidle")

        # Check we're on the right page (no 404)
        assert "404" not in page.title(), "Navigation led to 404 page"
        assert "obsidian" in page.url.lower(), f"Should be on Obsidian page, but URL is {page.url}"

        page.close()

    def test_navigation_back_button(self, browser_context):
        """Test that the Back navigation button works correctly."""
        page = browser_context.new_page()

        # Start at obsidian setup page
        url = f"{get_base_url()}/episodes/01-portfolio-no-code/content/01-obsidian-setup/"
        page.goto(url)

        # Find and click the Back/Previous button
        back_button = page.locator("a:has-text('Introduction')").first
        expect(back_button).to_be_visible()

        # Click and verify navigation
        back_button.click()
        page.wait_for_load_state("networkidle")

        # Check we're on the right page (no 404)
        assert "404" not in page.title(), "Navigation led to 404 page"
        assert "introduction" in page.url.lower(), f"Should be on Introduction page, but URL is {page.url}"

        page.close()

    def test_back_to_episode_overview(self, browser_context):
        """Test that the Back to Episode Overview button works correctly."""
        page = browser_context.new_page()

        # Start at introduction page
        url = f"{get_base_url()}/episodes/01-portfolio-no-code/content/00-introduction/"
        page.goto(url)

        # Find and click the Back to Episode Overview button
        back_button = page.locator("a:has-text('Episode Overview')").first
        expect(back_button).to_be_visible()

        # Get the href to verify it's correct
        href = back_button.get_attribute("href")
        # Accept both relative and absolute paths that lead to the episode overview
        valid_hrefs = ["../../", "/ai-power/episodes/01-portfolio-no-code/"]
        assert any(href.endswith(valid) for valid in valid_hrefs), f"Back to Episode Overview button has wrong href: {href}"

        # Click and verify navigation
        back_button.click()
        page.wait_for_load_state("networkidle")

        # Check we're on the Episode Overview page (no 404)
        assert "404" not in page.title(), f"Navigation to Episode Overview led to 404 page. URL: {page.url}"
        assert page.url.endswith("/episodes/01-portfolio-no-code/") or "01-portfolio-no-code" in page.url, f"Should be on Episode Overview, but URL is {page.url}"

        # Verify Episode Overview content loads
        heading = page.locator("h1").first
        expect(heading).to_be_visible()

        page.close()

    def test_all_navigation_links_no_404(self, browser_context):
        """Test that all major navigation links work without 404 errors."""
        page = browser_context.new_page()

        # List of pages to test
        pages_to_test = [
            "/episodes/01-portfolio-no-code/content/00-introduction/",
            "/episodes/01-portfolio-no-code/content/01-obsidian-setup/",
            "/episodes/01-portfolio-no-code/content/03-claude-code-install/",
            "/episodes/01-portfolio-no-code/content/04-agent-creation/",
            "/episodes/01-portfolio-no-code/content/05-portfolio-prep/",
            "/episodes/01-portfolio-no-code/content/06-master-prompt/",
            "/episodes/01-portfolio-no-code/content/07-github-deploy/",
        ]

        for page_path in pages_to_test:
            url = f"{get_base_url()}{page_path}"
            response = page.goto(url)

            # Check status code
            assert response.status == 200, f"Got {response.status} for {url}"

            # Check not a 404 page
            assert "404" not in page.title(), f"Page {url} shows 404"

            # Verify some content loads
            heading = page.locator("h1, h2").first
            expect(heading).to_be_visible(timeout=5000)

        page.close()

    def test_navigation_flow_complete(self, browser_context):
        """Test complete navigation flow through multiple pages."""
        page = browser_context.new_page()

        # Start at introduction
        url = f"{get_base_url()}/episodes/01-portfolio-no-code/content/00-introduction/"
        page.goto(url)

        # Navigate through several pages using Next buttons
        navigation_steps = [
            ("Obsidian Setup", "obsidian"),
            # We can add more steps here if needed
        ]

        for link_text, expected_url_part in navigation_steps:
            next_link = page.locator(f"a:has-text('{link_text}')").first
            expect(next_link).to_be_visible()

            next_link.click()
            page.wait_for_load_state("networkidle")

            # Verify we're on the right page
            assert "404" not in page.title(), f"Got 404 when navigating to {link_text}"
            assert expected_url_part in page.url.lower(), f"URL doesn't contain {expected_url_part}"

        page.close()

    def test_discord_link(self, browser_context):
        """Test that Discord link is correct and not a placeholder."""
        page = browser_context.new_page()

        # Go to the episode index page
        url = f"{get_base_url()}/episodes/01-portfolio-no-code/"
        page.goto(url)

        # Find Discord link
        discord_link = page.locator("a[href*='discord.gg']").first

        if discord_link.count() > 0:
            href = discord_link.get_attribute("href")
            # Check it's the correct Discord invite
            assert href == "https://discord.gg/UYg4BGJ65V", f"Discord link is wrong: {href}"
            assert "YOUR-DISCORD" not in href, "Discord link is still a placeholder"

        page.close()


def main():
    """Run tests manually without pytest."""
    print(f"Testing {get_base_url()}")
    print("-" * 50)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless
        context = browser.new_context()

        test = TestNavigation()

        try:
            print("✓ Testing introduction page...")
            test.test_introduction_page_loads(context)
            print("  ✅ Introduction page loads correctly")

            print("✓ Testing checklist display...")
            test.test_checklist_displays_correctly(context)
            print("  ✅ Checklist displays as proper list")

            print("✓ Testing Next button navigation...")
            test.test_navigation_next_button(context)
            print("  ✅ Next button works correctly")

            print("✓ Testing Back button navigation...")
            test.test_navigation_back_button(context)
            print("  ✅ Back button works correctly")

            print("✓ Testing Back to Episode Overview...")
            test.test_back_to_episode_overview(context)
            print("  ✅ Back to Episode Overview works correctly")

            print("✓ Testing all navigation links...")
            test.test_all_navigation_links_no_404(context)
            print("  ✅ All navigation links work (no 404)")

            print("✓ Testing complete navigation flow...")
            test.test_navigation_flow_complete(context)
            print("  ✅ Navigation flow works correctly")

            print("✓ Testing Discord link...")
            test.test_discord_link(context)
            print("  ✅ Discord link is correct")

            print("\n" + "=" * 50)
            print("🎉 All tests passed!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            raise
        finally:
            browser.close()


if __name__ == "__main__":
    main()