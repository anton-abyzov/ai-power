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
└── scripts/
    └── convert-excalidraw-svg.py # Conversion script
```

## ⚠️ CRITICAL RULES

### 1. NEVER EDIT `docs/episodes/`
- This folder is AUTO-GENERATED during build
- It's gitignored - changes will be lost
- Always edit files in `episodes/` folder

### 2. Obsidian vs MkDocs Handling
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

## 📌 Remember
- **Edit**: Only in `episodes/` folder
- **Test**: Locally before pushing
- **Wait**: 5-10 min for CDN updates
- **Debug**: Check GitHub Actions logs first