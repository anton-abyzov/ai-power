---
title: "Deploying to GitHub Pages"
timestamp: "31:28-42:52"
---

# Going Live with GitHub Pages

## Deployment Options Comparison
![GitHub Flow](../diagrams/06-github-flow.png)
![[episodes/01-portfolio-no-code/diagrams/all-diagrams.excalidraw.md#^clippedframe=Ztri2CGQKDYpPN5xoF3qH]]

- **GitHub Pages**: Free, automatic CI/CD, public code
- **Cloudflare**: Private code, manual updates
- **Vercel**: Private code, 100GB limit

## GitHub Setup Steps

1. **Create Repository**
    - Go to github.com
    - New repository → 'anna-portfolio'
    - Public → Create

2. **Upload Code**
    - Drag folder into GitHub
    - Or use git commands

3. **Enable GitHub Pages**
    - Settings → Pages
    - Source: Deploy from branch
    - Main → Root → Save

4. **Magic Moment**
    - Wait 2 minutes
    - Live at: username.github.io/anna-portfolio

## Custom Domain Setup
- Add CNAME file
- Configure DNS
- Result: abyzova.com

## CI/CD Explained
Push code → GitHub receives → Actions run → Site updates automatically

[→ Next: Philosophy & Closing](08-closing.md)