# ⚠️ IMPORTANT: Obsidian Usage Guide

## 🎯 Use the RIGHT Folder!

### ✅ CORRECT - Edit these files in Obsidian:
```
episodes/
├── 01-portfolio-no-code/
│   ├── content/        ← EDIT THESE
│   ├── diagrams/       ← YOUR EXCALIDRAW FILES
│   └── prompts/        ← EDIT THESE
```

### ❌ WRONG - Never edit these in Obsidian:
```
docs/
└── episodes/           ← AUTO-GENERATED! DO NOT EDIT!
    └── ...            ← Contains HTML for web only
```

## 📝 Quick Guide

1. **In Obsidian**: Always work in the `episodes/` folder
2. **Excalidraw embeds** will work properly in `episodes/` files
3. **The `docs/episodes/` folder** is automatically generated for the website
4. **Never edit** files in `docs/episodes/` - they'll be overwritten!

## 🔍 How to Navigate

In Obsidian's file explorer:
- ✅ Open: `episodes` → `01-portfolio-no-code` → `content`
- ❌ Avoid: `docs` → `episodes` (hidden by .obsidianignore)

## 📊 Excalidraw Diagrams

Your Excalidraw embeds look like this in `episodes/` files:
```markdown
![[episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.md#^clippedframe=FRAME_ID]]
```

These will:
- ✅ Work perfectly in Obsidian when viewing `episodes/` files
- ✅ Automatically convert to web format when deployed

## 🚀 Workflow

1. **Edit** in Obsidian: `episodes/` folder
2. **Push** to GitHub
3. **Auto-conversion** happens during deployment
4. **Website** shows the converted version

---

**Remember**: If you see HTML `<iframe>` code instead of diagrams, you're in the wrong folder!