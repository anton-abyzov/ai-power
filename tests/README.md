# E2E Testing Suite

## 📋 Test Files

### `test_full_navigation_e2e.py`
Comprehensive navigation testing suite that verifies:
- All pages load successfully
- Sidebar navigation is present on all pages
- Navigation footer with Previous/Next buttons exists
- All navigation links work without 404 errors
- Complete navigation flow from start to finish

### `test_navigation_e2e.py`
Basic navigation tests including:
- Introduction page functionality
- Checklist display format
- Navigation button functionality
- Episode Overview navigation
- Discord link validation

### `test_production.py`
Wrapper for testing the production site at https://anton-abyzov.github.io/ai-power

## 🚀 Running Tests

### Prerequisites
```bash
# Install dependencies
pip install -r tests/requirements.txt
playwright install chromium
```

### Command Line
```bash
# Run comprehensive navigation tests
python3 tests/test_full_navigation_e2e.py

# Run basic navigation tests
python3 tests/test_navigation_e2e.py

# Test production site
python3 tests/test_production.py

# Run all tests with pytest
pytest tests/ -v
```

### WebStorm Configuration

1. **Open project** in WebStorm

2. **Configure Python Interpreter**:
   - `File → Settings → Project → Python Interpreter`
   - Select Python 3.9+ interpreter
   - Install: `playwright`, `pytest`

3. **Create Run Configuration**:
   - `Run → Edit Configurations → + → Python`
   - Name: "E2E Navigation Tests"
   - Script path: Browse to `tests/test_full_navigation_e2e.py`
   - Working directory: Set to project root
   - Apply & OK

4. **Run Tests**:
   - Click green arrow in toolbar
   - Or right-click test file → Run
   - Or press `Ctrl+Shift+F10` (Win/Linux) / `Cmd+Shift+R` (Mac)

5. **Debug Tests**:
   - Set breakpoints by clicking left gutter
   - Click debug icon (bug) instead of run
   - Use debug console to inspect variables

## 🧪 Test Coverage

### Pages Tested
- ✅ 00-introduction
- ✅ 01-obsidian-setup
- ✅ 02-ai-tools-landscape
- ✅ 03-claude-code-install
- ✅ 04-agent-creation
- ✅ 05-portfolio-prep
- ✅ 06-master-prompt
- ✅ 07-github-deploy
- ✅ 08-closing

### Elements Verified
- ✅ Page loads (200 status)
- ✅ Sidebar navigation presence
- ✅ Navigation footer presence
- ✅ Previous button functionality
- ✅ Next button functionality
- ✅ Checklist formatting
- ✅ Discord link validity

## 📝 Writing New Tests

Add new test files to this directory following the pattern:
```python
from playwright.sync_api import sync_playwright, expect

class TestNewFeature:
    def test_something(self, browser_context):
        page = browser_context.new_page()
        page.goto("http://127.0.0.1:8000/ai-power/...")
        # Your test assertions
```

## 🔍 Troubleshooting

### Server not running
```bash
# Start MkDocs server before running tests
mkdocs serve
```

### Playwright not installed
```bash
playwright install chromium
```

### Tests timing out
- Check if MkDocs server is running on port 8000
- Verify no firewall blocking localhost
- Increase timeout in test configuration