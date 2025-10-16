# CLAUDE.md - AI Assistant Guide

## 🎯 Project Overview
This project maintains documentation for both Obsidian (local editing) and MkDocs (web deployment) with special handling for Excalidraw diagrams.

## 📂 Critical Folder Structure

```
GitHubAIPower/
├── episodes/                      # SOURCE FILES (Obsidian)
│   └── 01-portfolio-no-code/
│       ├── content/*.md          # Markdown with Obsidian syntax
│       └── diagrams/
│           ├── all-diagrams.excalidraw
│           ├── all-diagrams.excalidraw.md
│           └── *.svg files
│
├── docs/                          # MkDocs content
│   ├── episodes/                  # AUTO-GENERATED (gitignored!)
│   └── (other static docs)
│
├── scripts/                       # Utility scripts
│   ├── convert-excalidraw-svg.py # Conversion script
│   └── fix-navigation.py         # Navigation fixes
│
├── tests/                         # ALL TEST FILES GO HERE
│   ├── test_navigation_e2e.py    # Navigation E2E tests
│   ├── test_full_navigation_e2e.py # Comprehensive navigation tests
│   └── test_production.py        # Production site tests
│
└── [ROOT FOLDER]                  # KEEP CLEAN!
    ├── mkdocs.yml                 # MkDocs config
    ├── CLAUDE.md                  # This file
    ├── README.md                  # Project readme
    └── requirements.txt           # Python dependencies
```

## ⚠️ CRITICAL RULES

### 1. NEVER EDIT `docs/episodes/`
- This folder is AUTO-GENERATED during build
- It's gitignored - changes will be lost
- Always edit files in `episodes/` folder

### 2. KEEP ROOT FOLDER CLEAN
- **NEVER** put test files in root folder
- **NEVER** put images directly in root folder
- **NEVER** create temporary files in root
- All tests MUST go in `tests/` folder
- All scripts MUST go in `scripts/` folder
- All content MUST go in appropriate subdirectories

### 3. Obsidian vs MkDocs Handling
- **Obsidian**: Uses `![[episodes/.../all-diagrams.excalidraw.md#^frame=FRAME_ID]]`
- **MkDocs**: Needs conversion to SVG with viewBox
- Conversion happens during GitHub Actions deployment

## 🔄 Deployment Process

### How It Works:
1. User edits in `episodes/` folder using Obsidian
2. Push to GitHub triggers workflow
3. GitHub Actions runs:
   ```yaml
   - name: Convert Obsidian content for MkDocs
     run: python3 scripts/convert-excalidraw-svg.py
   ```
4. Script converts Excalidraw embeds to inline SVG
5. MkDocs builds from converted content
6. Deploys to GitHub Pages

### Conversion Logic:
```python
# From (Obsidian):
![[episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.md#^frame=KoJdwhj1PwVlHIsIixIRr]]

# To (MkDocs):
<svg viewBox="-2838 -2618 1793 1006">
  <image href="../../diagrams/all-diagrams.excalidraw.light.svg"/>
</svg>
```

## 🐛 Common Issues & Solutions

### Issue: Diagrams not showing on deployed site
**Symptom**: Raw Obsidian syntax appears instead of diagrams

**Solutions**:
1. Check if conversion script ran in GitHub Actions
2. Ensure SVG files are copied to docs/episodes/
3. Wait for GitHub Pages CDN to update (5-10 min)
4. Check for deployment conflicts

### Issue: Deployment fails with "in progress deployment"
**Solution**: Cancel stuck deployment
```bash
gh run list --workflow=deploy.yml --status=in_progress --json databaseId | jq -r '.[0].databaseId' | xargs gh run cancel
```

## 📝 Testing Deployments

### Local Test:
```bash
# Clean and rebuild
rm -rf site docs/episodes
python3 scripts/convert-excalidraw-svg.py
mkdocs build
# Check: site/episodes/01-portfolio-no-code/content/00-introduction/index.html
```

### Remote Test:
```bash
# Check deployed content
curl -s "https://anton-abyzov.github.io/ai-power/episodes/01-portfolio-no-code/content/00-introduction.html" | grep -c "svg"
```

## 🎨 Excalidraw Frame Coordinates

The script maintains frame coordinates for viewport mapping:
```python
FRAME_COORDS = {
    'KoJdwhj1PwVlHIsIixIRr': {'x': -2838, 'y': -2618, 'width': 1793, 'height': 1006},
    'rVOSTdETPrlwu1WhoIxKN': {'x': -303, 'y': -2451, 'width': 963, 'height': 561},
    # ... more frames
}
```

## 🚀 Reverse-Engineered Workflow

### Initial Problem:
"Excalidraw links don't work in Obsidian, showing error and not selecting frame"

### Solution Evolution:
1. **Attempt 1**: Fix Obsidian embed syntax → Works locally
2. **Attempt 2**: Create viewer.html for iframes → Complex, unreliable
3. **Attempt 3**: Use inline SVG with viewBox → Simple, works!
4. **Final**: Automated conversion during build

### Key Insights:
- Obsidian needs native syntax for editing
- MkDocs needs HTML/SVG for rendering
- Conversion must happen during build, not in source
- GitHub Pages CDN can cache old content

## 🔧 Maintenance Commands

```bash
# Force rebuild without cache
git commit --allow-empty -m "Force rebuild"
git push

# Check workflow status
gh run list --workflow=deploy.yml --limit=5

# Watch deployment
gh run watch $(gh run list --workflow=deploy.yml --limit=1 --json databaseId --jq '.[0].databaseId')

# Cancel stuck deployment
gh workflow run deploy.yml
```

## 🧪 Testing Guide

### Running E2E Tests

#### From Command Line:
```bash
# Run all navigation tests
cd /path/to/GitHubAIPower
python3 tests/test_full_navigation_e2e.py

# Test production site
python3 tests/test_production.py

# Run with pytest (if installed)
pytest tests/ -v
```

#### From WebStorm:
1. **Open Project** in WebStorm
2. **Configure Python Interpreter**:
   - File → Settings → Project → Python Interpreter
   - Select your Python 3.9+ interpreter
   - Install dependencies: `playwright`, `pytest`

3. **Create Run Configuration**:
   - Run → Edit Configurations → Add New Configuration → Python
   - **Name**: "E2E Navigation Tests"
   - **Script path**: `tests/test_full_navigation_e2e.py`
   - **Working directory**: Project root
   - Click OK

4. **Run Tests**:
   - Click green arrow next to configuration
   - Or right-click test file → Run
   - Or use keyboard shortcut: Ctrl+Shift+F10 (Windows/Linux) or Cmd+Shift+R (Mac)

5. **Debug Tests**:
   - Set breakpoints in test files
   - Click debug icon instead of run
   - Step through test execution

### Test Structure:
```
tests/
├── test_navigation_e2e.py        # Basic navigation tests
├── test_full_navigation_e2e.py   # Comprehensive test suite
│   ├── test_ai_tools_landscape_page()
│   ├── test_all_content_pages()
│   ├── test_navigation_flow()
│   └── run_all_tests()
└── test_production.py            # Production site tests
```

### Before Pushing to GitHub:
1. Run local server: `mkdocs serve`
2. Run E2E tests: `python3 tests/test_full_navigation_e2e.py`
3. Verify all tests pass
4. Stop local server
5. Commit and push

## 📌 Remember
- **Edit**: Only in `episodes/` folder
- **Test**: Locally before pushing (run E2E tests!)
- **Keep Clean**: Root folder is for config files only
- **Wait**: 5-10 min for CDN updates after deploy
- **Debug**: Check GitHub Actions logs first

## 🚨 CRITICAL: When Publishing New Episodes

**ALWAYS UPDATE THESE FILES AFTER PUBLISHING A NEW YOUTUBE VIDEO:**

### 1. README.md (GitHub homepage)
```markdown
## 📺 Latest Episode
**[03: N8N + SORA 2 Automation](episodes/03-n8n-automation)** - Build video generation workflows
```

Update:
- Latest Episode section (line ~13)
- YouTube link in table
- Episode number

### 2. docs/index.md (Website homepage)
```markdown
## 🎥 Latest Episode

<div style="margin: 2rem 0;">
  <iframe width="760" height="427" src="https://www.youtube.com/embed/[VIDEO_ID]" ...></iframe>
</div>

### Episode 03: N8N + SORA 2 Automation 🆕
```

Update:
- YouTube embed iframe src (line ~28)
- Episode title and number (line ~31)
- Episode description
- "Available Now" section (line ~96)
- Move previous "latest" episode down

### 3. Checklist Before Publishing
- [ ] YouTube video published and URL confirmed
- [ ] Episode folder exists in `docs/episodes/[episode-name]/`
- [ ] README.md "Latest Episode" updated
- [ ] README.md episode table updated
- [ ] docs/index.md YouTube embed updated
- [ ] docs/index.md "Latest Episode" section updated
- [ ] docs/index.md "Available Now" list updated
- [ ] Git commit with message: "Update to Episode [N]: [Title]"
- [ ] Push to GitHub
- [ ] Verify website updates (wait 5-10 min for CDN)

**Why This Matters:**
- Users land on these pages first
- Outdated "latest episode" = missed views
- SEO and discoverability suffer
- Professionalism and trust impacted