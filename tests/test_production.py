#!/usr/bin/env python3
"""
Test the production GitHub Pages site.
"""

import os
import sys

# Set environment to test production
os.environ["TEST_PRODUCTION"] = "true"

# Import and run the main test
sys.path.insert(0, os.path.dirname(__file__))
from test_navigation_e2e import main, TEST_PRODUCTION, PROD_URL

print(f"🌐 Testing PRODUCTION site: {PROD_URL}")
print("=" * 60)

# Temporarily modify the global variable
import test_navigation_e2e
test_navigation_e2e.TEST_PRODUCTION = True

try:
    main()
except Exception as e:
    print(f"Production test failed: {e}")
    sys.exit(1)