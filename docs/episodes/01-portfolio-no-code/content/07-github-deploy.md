---
title: "Deploying to GitHub Pages"
timestamp: "31:28-42:52"
---

# Going Live with GitHub Pages

## Deployment Options Comparison

![Deployment Options](../diagrams/frames/frame-7.svg)

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

---

<div class="navigation-footer" style="display: flex; justify-content: space-between; margin: 3rem 0 2rem 0; padding: 2rem 0; border-top: 1px solid #e0e0e0;">
  <div>
    <a href="../06-master-prompt/" style="text-decoration: none;">
      <div style="color: #666; font-size: 0.9rem;">← Previous</div>
      <div style="color: #7c4dff; font-weight: 600;">Master Prompt</div>
    </a>
  </div>
  <div style="text-align: right;">
    <a href="../08-closing/" style="text-decoration: none;">
      <div style="color: #666; font-size: 0.9rem;">Next →</div>
      <div style="color: #7c4dff; font-weight: 600;">Closing</div>
    </a>
  </div>
</div><\!-- End of content -->
