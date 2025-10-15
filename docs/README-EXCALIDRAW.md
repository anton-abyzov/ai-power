# Excalidraw Integration Setup

## Overview
This project uses a dual-format approach for Excalidraw diagrams:
- **Obsidian**: Native Excalidraw embeds for editing
- **MkDocs**: HTML iframes for web deployment

## How It Works

### 1. Source Files (episodes/)
- Contains Obsidian-native markdown with Excalidraw embeds
- Format: `![[episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.md#^clippedframe=FRAME_ID]]`
- These files work directly in Obsidian

### 2. Build Process
- `scripts/convert-excalidraw.py` runs during GitHub Actions deployment
- Converts Obsidian embeds to HTML iframes
- Copies files from `episodes/` to `docs/episodes/`
- Transforms Excalidraw links to: `<iframe src="../../diagrams/viewer.html#FRAME_ID">`

### 3. Deployment
- GitHub Actions workflow runs conversion before MkDocs build
- `docs/episodes/` is auto-generated and gitignored
- MkDocs builds from the converted files

## File Structure
```
episodes/                      # Source files (Obsidian format)
├── 01-portfolio-no-code/
│   ├── content/*.md          # With Obsidian Excalidraw embeds
│   └── diagrams/
│       ├── all-diagrams.excalidraw
│       └── all-diagrams.excalidraw.md
│
docs/                         # MkDocs content
├── episodes/                 # AUTO-GENERATED (gitignored)
│   └── ...                   # Converted from episodes/
└── episodes/01-portfolio-no-code/
    └── diagrams/
        └── viewer.html       # Frame viewer for web

scripts/
└── convert-excalidraw.py    # Conversion script
```

## Key Files
- `scripts/convert-excalidraw.py` - Converts Obsidian syntax to MkDocs
- `docs/episodes/01-portfolio-no-code/diagrams/viewer.html` - Displays Excalidraw frames on web
- `.github/workflows/deploy.yml` - Runs conversion during deployment
- `.gitignore` - Excludes `docs/episodes/` from version control

## Workflow
1. Edit content in `episodes/` using Obsidian
2. Push changes to GitHub
3. GitHub Actions automatically:
   - Runs conversion script
   - Builds MkDocs site
   - Deploys to GitHub Pages

## Notes
- Always edit source files in `episodes/` folder
- Never edit files in `docs/episodes/` (auto-generated)
- The conversion preserves all non-markdown files (SVGs, etc.)