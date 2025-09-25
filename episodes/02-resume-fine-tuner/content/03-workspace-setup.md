---
title: "Setting Up Your Resume Workspace"
timestamp: "3:00-4:00"
---

# Organizing Your Resume System

## Directory Structure

Create a clean, organized workspace for your resume system:

### Mac/Linux
```bash
# Create the directory structure
cd ~/Documents
mkdir -p resumes/{templates,outputs,job-descriptions,samples}

# Optional: Create sections for different markets
mkdir -p resumes/outputs/{remote,onsite,contract,fulltime}
```

### Windows
```powershell
# Create the directory structure
cd $env:USERPROFILE\Documents
mkdir resumes\templates, resumes\outputs, resumes\job-descriptions, resumes\samples

# Optional: Create sections for different markets
mkdir resumes\outputs\remote, resumes\outputs\onsite
mkdir resumes\outputs\contract, resumes\outputs\fulltime
```

### Folder Purposes

```
~/resumes/
├── templates/           # Base resume formats
│   ├── master.md       # Complete experience database
│   ├── sections/       # Reusable components
│   └── styles/         # Formatting templates
├── outputs/            # Generated resumes
│   ├── 2024/          # Organized by year
│   └── archived/      # Older versions
├── job-descriptions/   # Save JDs for reference
│   ├── applied/       # Positions you applied to
│   └── interesting/   # Future opportunities
└── samples/           # Example outputs
    └── successful/    # Resumes that got interviews
```

## File Naming Convention

Smart naming helps track everything:

```bash
# Format: [company]_[role]_[recruiter]_[date].docx
microsoft_senior_dotnet_john_2024-01.docx
google_ml_engineer_sarah_2024-01.docx
aws_solutions_architect_amy_2024-02.docx
```

### Why This Matters
- **Quick identification** of which resume for which opportunity
- **Track recruiter names** for follow-ups
- **Date stamping** for version control
- **Pattern analysis** of what works

## Base Experience Template

Create your master experience file:

```markdown
# Master Experience Database
## Personal Information
Name: Your Name
Location: City, State (or "Remote")
Contact: email@example.com | LinkedIn

## Core Skills Matrix
### Languages
- Expert: Python, JavaScript, Go
- Proficient: Java, C#, Rust
- Familiar: Scala, Kotlin

### Cloud Platforms
- AWS: 5 years (Certified Solutions Architect)
- Azure: 3 years (AZ-305 certified)
- GCP: 2 years (hands-on experience)

## Complete Experience

### Company: TechCorp Inc
**Period**: Jan 2020 - Present
**Role**: Senior Software Engineer
**Team Size**: 12 engineers
**Technologies**: Python, AWS, Kubernetes, PostgreSQL

#### Projects
1. **Payment Platform Modernization**
   - Migrated legacy system to microservices
   - Reduced transaction time by 35%
   - Handled 10M+ transactions daily

2. **ML Fraud Detection System**
   - Built TensorFlow model with 94% accuracy
   - Reduced false positives by 40%
   - Saved $2M annually in fraud losses

### Company: StartupXYZ
[... continue with all experience ...]
```

## Version Control Strategy

Track your resume evolution:

```bash
# Initialize git repository
cd ~/resumes
git init

# Create .gitignore
echo "job-descriptions/applied/*" >> .gitignore
echo "outputs/draft/*" >> .gitignore

# Commit your templates
git add templates/
git commit -m "Initial resume templates"

# Tag successful versions
git tag -a "microsoft-interview-v1" -m "Version that got MS interview"
```

## Integration with Tools

### For Markdown to PDF
```bash
# Install pandoc
brew install pandoc  # Mac
# or
sudo apt-get install pandoc  # Linux

# Convert to PDF
pandoc resume.md -o resume.pdf --pdf-engine=xelatex
```

### For LaTeX Output
```bash
# If you prefer LaTeX formatting
pandoc resume.md -o resume.tex
# Then compile with your preferred LaTeX editor
```

## Best Practices

### 1. Regular Updates
- Add new projects immediately
- Update metrics quarterly
- Refresh skills annually

### 2. Backup Strategy
- Git repository for version control
- Cloud sync (iCloud/Google Drive)
- Export successful versions to PDF

### 3. Privacy Considerations
- Don't commit sensitive client names
- Use project codenames if needed
- Keep salary information separate

---

<div class="navigation-footer">
  <div>
    <a href="../02-claude-agents-overview/">
      <div>← Previous</div>
      <div>Claude Agents</div>
    </a>
  </div>
  <div style="text-align: right;">
    <a href="../04-creating-agent/">
      <div>Next →</div>
      <div>Creating the Agent</div>
    </a>
  </div>
</div>