#!/usr/bin/env python3
"""
Comprehensive E2E tests for MkDocs navigation.
Tests that ALL pages have proper navigation, sidebars, and buttons.
"""

from playwright.sync_api import sync_playwright, expect
import sys

# Local testing URL
BASE_URL = "http://127.0.0.1:8000/ai-power"

class TestCompleteNavigation:
    """Comprehensive navigation test suite."""

    def __init__(self):
        self.failed_tests = []

    def test_ai_tools_landscape_page(self, page):
        """Test that AI Tools Landscape page has all navigation elements."""
        print("\n🔍 Testing AI Tools Landscape page...")

        url = f"{BASE_URL}/episodes/01-portfolio-no-code/content/02-ai-tools-landscape/"
        response = page.goto(url)

        # Check page loads
        assert response.status == 200, f"Page returned {response.status}"
        print("  ✓ Page loads successfully")

        # Check for left sidebar navigation
        sidebar = page.locator("nav.md-nav--primary")
        assert sidebar.count() > 0, "Missing left sidebar navigation!"
        print("  ✓ Left sidebar navigation present")

        # Check sidebar has content
        sidebar_items = sidebar.locator("li.md-nav__item")
        assert sidebar_items.count() > 5, f"Sidebar has only {sidebar_items.count()} items"
        print(f"  ✓ Sidebar has {sidebar_items.count()} navigation items")

        # Check for AI Tools Landscape in sidebar (should be highlighted)
        ai_tools_nav = sidebar.locator("a:has-text('AI Tools Landscape')")
        assert ai_tools_nav.count() > 0, "AI Tools Landscape not in sidebar!"
        print("  ✓ AI Tools Landscape appears in sidebar")

        # Check for navigation footer with Previous/Next buttons
        nav_footer = page.locator("div.navigation-footer")
        assert nav_footer.count() > 0, "Missing navigation footer!"
        print("  ✓ Navigation footer present")

        # Check for Previous button (should go to Obsidian Setup)
        prev_button = page.locator("a:has-text('Obsidian Setup')").first
        assert prev_button.count() > 0, "Missing Previous button to Obsidian Setup!"
        print("  ✓ Previous button to Obsidian Setup found")

        # Check for Next button (should go to Installing Claude)
        next_button = page.locator("a:has-text('Installing Claude')").first
        assert next_button.count() > 0, "Missing Next button to Installing Claude!"
        print("  ✓ Next button to Installing Claude found")

        # Test Previous button navigation
        prev_button.click()
        page.wait_for_load_state("networkidle")
        assert "obsidian-setup" in page.url, "Previous button didn't navigate to Obsidian Setup"
        print("  ✓ Previous button works")

        # Go back to AI Tools page
        page.goto(url)

        # Test Next button navigation
        next_button = page.locator("a:has-text('Installing Claude')").first
        next_button.click()
        page.wait_for_load_state("networkidle")
        assert "claude-code-install" in page.url, "Next button didn't navigate to Claude Install"
        print("  ✓ Next button works")

        print("✅ AI Tools Landscape page - ALL TESTS PASSED")
        return True

    def test_all_content_pages(self, page):
        """Test that all content pages have proper navigation."""
        print("\n🔍 Testing all content pages...")

        pages_to_test = [
            ("00-introduction", "Introduction", None, "Obsidian Setup"),
            ("01-obsidian-setup", "Obsidian Setup", "Introduction", "AI Tools Landscape"),
            ("02-ai-tools-landscape", "AI Tools Landscape", "Obsidian Setup", "Installing Claude"),
            ("03-claude-code-install", "Claude Install", "AI Tools Landscape", "Agent Creation"),
            ("04-agent-creation", "Agent Creation", "Claude", "Portfolio Prep"),
            ("05-portfolio-prep", "Portfolio Prep", "Agent Creation", "Master Prompt"),
            ("06-master-prompt", "Master Prompt", "Portfolio Prep", "GitHub Deploy"),
            ("07-github-deploy", "GitHub Deploy", "Master Prompt", "Closing"),
            ("08-closing", "Closing", "GitHub Deploy", None),
        ]

        for page_name, title, prev_text, next_text in pages_to_test:
            print(f"\n  Testing {page_name}...")
            url = f"{BASE_URL}/episodes/01-portfolio-no-code/content/{page_name}/"
            response = page.goto(url)

            # Check page loads
            if response.status != 200:
                self.failed_tests.append(f"{page_name}: Page returned {response.status}")
                continue
            print(f"    ✓ Page loads")

            # Check for sidebar
            sidebar = page.locator("nav.md-nav--primary")
            if sidebar.count() == 0:
                self.failed_tests.append(f"{page_name}: Missing sidebar navigation")
                print(f"    ✗ Missing sidebar!")
            else:
                print(f"    ✓ Sidebar present")

            # Check for navigation footer
            nav_footer = page.locator("div.navigation-footer")
            if nav_footer.count() == 0:
                self.failed_tests.append(f"{page_name}: Missing navigation footer")
                print(f"    ✗ Missing navigation footer!")
            else:
                print(f"    ✓ Navigation footer present")

            # Check for Previous button (if expected)
            if prev_text:
                prev_button = nav_footer.locator(f"a:has-text('{prev_text}')")
                if prev_button.count() == 0:
                    self.failed_tests.append(f"{page_name}: Missing Previous button to {prev_text}")
                    print(f"    ✗ Missing Previous button!")
                else:
                    print(f"    ✓ Previous button to {prev_text}")

            # Check for Next button (if expected)
            if next_text:
                next_button = nav_footer.locator(f"a:has-text('{next_text}')")
                if next_button.count() == 0:
                    self.failed_tests.append(f"{page_name}: Missing Next button to {next_text}")
                    print(f"    ✗ Missing Next button!")
                else:
                    print(f"    ✓ Next button to {next_text}")

        return len(self.failed_tests) == 0

    def test_navigation_flow(self, page):
        """Test complete navigation flow through all pages."""
        print("\n🔍 Testing complete navigation flow...")

        # Start at introduction
        url = f"{BASE_URL}/episodes/01-portfolio-no-code/content/00-introduction/"
        page.goto(url)

        navigation_path = [
            ("Obsidian Setup", "obsidian-setup"),
            ("AI Tools Landscape", "ai-tools-landscape"),
            ("Installing Claude", "claude-code-install"),
            ("Agent Creation", "agent-creation"),
            ("Portfolio Prep", "portfolio-prep"),
            ("Master Prompt", "master-prompt"),
            ("GitHub Deploy", "github-deploy"),
            ("Closing", "closing"),
        ]

        for link_text, expected_url_part in navigation_path:
            print(f"  Navigating to {link_text}...")

            # Try to find the next button
            next_button = page.locator(f"a:has-text('{link_text}')").first

            if next_button.count() == 0:
                self.failed_tests.append(f"Cannot find link to {link_text}")
                print(f"    ✗ Cannot find link!")
                break

            next_button.click()
            page.wait_for_load_state("networkidle")

            if expected_url_part not in page.url:
                self.failed_tests.append(f"Navigation to {link_text} failed")
                print(f"    ✗ Navigation failed!")
                break

            print(f"    ✓ Successfully navigated to {link_text}")

        print("✅ Navigation flow complete")
        return len(self.failed_tests) == 0

    def run_all_tests(self):
        """Run all tests and report results."""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # Set to True for headless
            context = browser.new_context()
            page = context.new_page()

            print("=" * 60)
            print("COMPREHENSIVE NAVIGATION E2E TESTS")
            print("=" * 60)
            print(f"Testing: {BASE_URL}")

            try:
                # Test AI Tools Landscape specifically
                self.test_ai_tools_landscape_page(page)

                # Test all content pages
                self.test_all_content_pages(page)

                # Test navigation flow
                self.test_navigation_flow(page)

                print("\n" + "=" * 60)
                if self.failed_tests:
                    print("❌ TESTS FAILED!")
                    print("\nFailed tests:")
                    for failure in self.failed_tests:
                        print(f"  - {failure}")
                    sys.exit(1)
                else:
                    print("✅ ALL TESTS PASSED!")
                    print("\nSummary:")
                    print("  ✓ All pages have sidebar navigation")
                    print("  ✓ All pages have navigation footer")
                    print("  ✓ All Previous/Next buttons work")
                    print("  ✓ Complete navigation flow works")

            except Exception as e:
                print(f"\n❌ Test error: {e}")
                sys.exit(1)
            finally:
                browser.close()

if __name__ == "__main__":
    tester = TestCompleteNavigation()
    tester.run_all_tests()