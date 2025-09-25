---
title: "Output Format Options"
timestamp: "12:30-13:30"
---

# Resume Format Options

## Output Formats Overview

Your AI-generated resume defaults to Word format (.docx) for best ATS compatibility, but you can convert to any professional format.

### What is Pandoc?

Pandoc is the "Swiss Army knife" of document conversion. Think of it as a universal translator between document formats - it can convert between Word, PDF, Markdown, LaTeX, HTML, and dozens of other formats. It's free, open-source, and works on all platforms.

## 1. PDF Output (Most Common)

### Using Pandoc
```bash
# Basic PDF conversion
pandoc resume.md -o resume.pdf

# With better formatting (requires LaTeX)
pandoc resume.md -o resume.pdf --pdf-engine=xelatex

# With custom styling
pandoc resume.md -o resume.pdf --pdf-engine=xelatex \
  --variable geometry:margin=1in \
  --variable fontsize=11pt
```

### Using Markdown-PDF (Node.js)
```bash
# Install
npm install -g markdown-pdf

# Convert
markdown-pdf resume.md -o resume.pdf
```

### Using VS Code Extension
1. Install "Markdown PDF" extension
2. Open your resume.md
3. Press `Ctrl+Shift+P` → "Markdown PDF: Export"
4. Professional PDF ready!

## 2. Word Document (.docx)

### For ATS Compatibility
```bash
# Direct conversion
pandoc resume.md -o resume.docx

# With reference template
pandoc resume.md -o resume.docx \
  --reference-doc=template.docx
```

### Why Word?
- Some ATS systems parse .docx better
- Recruiters can add notes
- Easy for them to reformat if needed
- Maintains formatting across systems

## 3. LaTeX (Professional/Academic)

### The Premium Option

LaTeX gives you pixel-perfect control over formatting, which is why it's preferred for academic and research positions.

### Real Example from Healthcare Position
```latex
% Recruiter: Healthcare Systems - Cardiology Unit
% Company: Healthcare Technology Organization
% Phone: Contact via application portal
% Position: Senior Software Engineer - Healthcare Systems
% Duration: Full-time opportunity

\section*{Professional Summary}
Senior Software Engineer with 18+ years developing enterprise healthcare
applications, specializing in React, C\#, JavaScript, and medical device
integration. Proven expertise in incident management, system upgrades,
and security modifications within healthcare environments.

\section*{Work Experience}

\cventry{Jun 2017 -- Present}{Senior Software Engineer}{Softgreat}{Miami, FL / Remote}{}{
\begin{itemize}
  \item Led healthcare technology initiatives across multiple enterprise clients
  \item Resolved 95\% of critical incidents within 4-hour SLA
  \item Managed system upgrades ensuring 99.9\% uptime for patient-critical apps
  \item \textbf{Selected Healthcare Client Deliveries:}\\
    \begin{itemize}
      \item \textit{\textbf{Pathmate Technologies} – Heart Coach Platform}\\
        Developed React Native app ranked \#68 in App Store medical category.
        Built .NET Core backend processing 10M+ daily health readings.
        Implemented SharePoint content management for medical protocols.

      \item \textit{\textbf{DentalCorp} – Clinical Data Integration}\\
        Built React administration portal for 1,500+ dental clinics.
        Developed .NET Core agents for 9 PMS integrations.
        Created monitoring dashboard with real-time status updates.
    \end{itemize}
\end{itemize}}
```

### Using Overleaf.com
1. Create free account at overleaf.com
2. Upload your .tex file
3. Choose from professional templates
4. Real-time preview with error checking
5. Collaborate with version control
6. Download PDF when ready

**[Video: Navigate to Overleaf and show the live compilation]**

### LaTeX Advantages
- Pixel-perfect formatting
- Consistent across all systems
- Professional appearance
- Version control friendly
- Academic/research standard

## 4. HTML/Web Resume

### Static Site Generation
```html
<!-- Convert to HTML -->
pandoc resume.md -o resume.html --standalone \
  --css=resume-style.css

<!-- Or use a static site generator -->
# With Jekyll
jekyll new my-resume
cp resume.md my-resume/_posts/

# With Hugo
hugo new site my-resume
cp resume.md my-resume/content/
```

### GitHub Pages Hosting
```bash
# Create repository: username.github.io
git init
git add resume.md
git commit -m "Add resume"
git push origin main

# Access at: https://username.github.io
```

### Interactive Features
Add interactivity with JavaScript:
```javascript
// Skill filtering
function filterBySkill(skill) {
  document.querySelectorAll('.project').forEach(p => {
    if (p.dataset.skills.includes(skill)) {
      p.style.display = 'block';
    } else {
      p.style.display = 'none';
    }
  });
}
```

## 5. Plain Text (ATS Optimization)

### Why Plain Text?
- 100% ATS compatible
- No parsing errors
- Smallest file size
- Email-body friendly

### Conversion
```bash
# Strip all formatting
pandoc resume.md -t plain -o resume.txt

# Or use sed for more control
sed 's/[#*`]//g' resume.md > resume.txt
```

### Plain Text Best Practices
```
JOHN DOE
Email: john@example.com | Phone: 555-0123
LinkedIn: linkedin.com/in/johndoe

EXPERIENCE

Senior Software Engineer | TechCorp | 2020-Present
- Built microservices handling 1M requests/day
- Reduced deployment time by 30%
- Led team of 5 engineers

[Continue with clear, simple formatting]
```

## Format Comparison Table

| Format | ATS Score | Professional Look | Editability | File Size |
|--------|-----------|------------------|-------------|-----------|
| PDF | Good | Excellent | Poor | Medium |
| Word | Excellent | Good | Excellent | Medium |
| LaTeX PDF | Good | Excellent | Poor | Small |
| HTML | Poor | Good | Good | Small |
| Plain Text | Excellent | Poor | Excellent | Tiny |

## Multi-Format Strategy

### Create Once, Deploy Everywhere
```bash
#!/bin/bash
# generate-all-formats.sh

INPUT="resume.md"
BASE="resume_$(date +%Y%m%d)"

# Generate all formats
pandoc $INPUT -o ${BASE}.pdf --pdf-engine=xelatex
pandoc $INPUT -o ${BASE}.docx
pandoc $INPUT -o ${BASE}.html --standalone
pandoc $INPUT -t plain -o ${BASE}.txt

echo "Generated: PDF, Word, HTML, and Text versions"
```

## Format-Specific Tips

### PDF Tips
- Embed fonts for consistency
- Use vector graphics for logos
- Keep under 2MB for email
- Test print preview

### Word Tips
- Use styles, not direct formatting
- Check compatibility mode
- Avoid text boxes
- Test in Word Online

### HTML Tips
- Responsive design for mobile
- Fast loading (no heavy images)
- SEO optimize if public
- Include print stylesheet

### LaTeX Tips
- Use standard packages
- Comment complex commands
- Version control .tex files
- Keep style separate from content

## Testing Your Formats

### ATS Testing
```bash
# Use online ATS scanners
# 1. Upload to jobscan.co
# 2. Check keyword match
# 3. Verify parsing accuracy
# 4. Adjust formatting if needed
```

### Visual Testing
- Open in different applications
- Check on various devices
- Print to verify layout
- Test email attachments

### Accessibility Testing
- Screen reader compatibility
- High contrast mode
- Font scaling
- Color blind friendly

---

<div class="navigation-footer">
  <div>
    <a href="../07-advanced-techniques/">
      <div>← Previous</div>
      <div>Advanced Techniques</div>
    </a>
  </div>
  <div style="text-align: right;">
    <a href="../09-results-metrics/">
      <div>Next →</div>
      <div>Results & Metrics</div>
    </a>
  </div>
</div>