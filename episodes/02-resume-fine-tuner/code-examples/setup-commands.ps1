# Resume Fine-Tuner Setup Script for Windows PowerShell
# Run this script as Administrator for best results

Write-Host "🚀 Setting up Resume Fine-Tuner Workspace..." -ForegroundColor Cyan

# Create directory structure
Write-Host "📁 Creating directory structure..." -ForegroundColor Yellow

$resumePath = "$env:USERPROFILE\resumes"
$directories = @(
    "$resumePath\templates",
    "$resumePath\outputs",
    "$resumePath\outputs\drafts",
    "$resumePath\outputs\final",
    "$resumePath\outputs\archived",
    "$resumePath\job-descriptions",
    "$resumePath\job-descriptions\active",
    "$resumePath\job-descriptions\applied",
    "$resumePath\job-descriptions\archived",
    "$resumePath\experience"
)

foreach ($dir in $directories) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "Created: $dir" -ForegroundColor Green
    } else {
        Write-Host "Exists: $dir" -ForegroundColor Gray
    }
}

# Set up Claude Code function for permission bypass
Write-Host "`n⚙️  Setting up Claude Code function..." -ForegroundColor Yellow

$profilePath = $PROFILE
$profileDir = Split-Path $profilePath -Parent

# Create profile directory if it doesn't exist
if (!(Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}

# Create profile file if it doesn't exist
if (!(Test-Path $profilePath)) {
    New-Item -ItemType File -Path $profilePath -Force | Out-Null
}

# Check if function already exists
$profileContent = Get-Content $profilePath -ErrorAction SilentlyContinue
if ($profileContent -notcontains "function claude {") {
    Add-Content $profilePath "`n# Claude Code function for permission bypass"
    Add-Content $profilePath "function claude {"
    Add-Content $profilePath "    & claude --dangerously-skip-permissions `$args"
    Add-Content $profilePath "}"
    Write-Host "✅ Claude function added to PowerShell profile" -ForegroundColor Green
} else {
    Write-Host "ℹ️  Claude function already exists in profile" -ForegroundColor Cyan
}

# Create sample experience database
Write-Host "`n📝 Creating sample experience database..." -ForegroundColor Yellow

$experienceContent = @"
# My Professional Experience

## Contact Information
- Name: [Your Name]
- Email: [your.email@example.com]
- Location: [City, State / Remote]
- LinkedIn: [linkedin.com/in/yourprofile]

## Experience

### Software Engineer at TechCorp (2020-Present)
- Built scalable microservices handling 10M+ requests daily
- Improved API response time by 25% through optimization
- Led team of 5 engineers on cloud migration project
- Technologies: Python, React, PostgreSQL, AWS, Docker

### Junior Developer at StartupCo (2018-2020)
- Developed full-stack features for SaaS platform
- Implemented automated testing, reducing bugs by 30%
- Technologies: JavaScript, Node.js, MongoDB

## Skills
- Languages: Python, JavaScript, TypeScript, Go
- Frameworks: React, Django, Express.js
- Databases: PostgreSQL, MongoDB, Redis
- Cloud: AWS, Azure, Docker, Kubernetes
"@

Set-Content -Path "$resumePath\experience\my-experience.md" -Value $experienceContent
Write-Host "✅ Sample experience database created" -ForegroundColor Green

# Create agent configuration
Write-Host "`n🤖 Creating agent configuration..." -ForegroundColor Yellow

$agentConfig = @"
name: resume-fine-tuner
description: AI agent for resume optimization
tools: [Read, Write, Edit, Grep, Glob]
experience_file: $resumePath\experience\my-experience.md
output_directory: $resumePath\outputs\
"@

Set-Content -Path "$resumePath\resume-agent-config.yaml" -Value $agentConfig
Write-Host "✅ Agent configuration created" -ForegroundColor Green

# Create sample job description
Write-Host "`n📄 Creating sample job description..." -ForegroundColor Yellow

$jobDescription = @"
Senior Software Engineer - Cloud Platform

Requirements:
- 5+ years software development experience
- Strong Python and cloud platform expertise (AWS preferred)
- Experience with microservices and containerization
- PostgreSQL and NoSQL database proficiency
- Leadership experience mentoring junior developers

Nice to have:
- Kubernetes and Docker expertise
- React or modern frontend framework experience
- Open source contributions
- DevOps and CI/CD pipeline experience
"@

Set-Content -Path "$resumePath\job-descriptions\active\sample-senior-dev.txt" -Value $jobDescription
Write-Host "✅ Sample job description created" -ForegroundColor Green

# Create quick start guide
$readme = @"
# Resume Fine-Tuner Quick Start

## Setup Complete! 🎉

### Directory Structure:
- ``templates\`` - Store your base resume templates
- ``outputs\`` - AI-generated tailored resumes
- ``job-descriptions\`` - Save job postings
- ``experience\`` - Your complete experience database

### How to Use:

1. Edit your experience database:
   ```powershell
   notepad $resumePath\experience\my-experience.md
   ```

2. Add a job description:
   ```powershell
   notepad $resumePath\job-descriptions\active\company-role.txt
   ```

3. Run Claude Code agent:
   ```powershell
   cd $resumePath
   claude "Please tailor my resume for the job in job-descriptions\active\company-role.txt using my experience from experience\my-experience.md"
   ```

4. Find your tailored resume in ``outputs\drafts\``

### Pro Tips:
- Keep job descriptions that led to interviews in ``applied\``
- Archive old applications in ``archived\``
- Track success metrics in Excel
- Save winning resume versions as templates

### Convert Formats:
```powershell
# Install Pandoc first: https://pandoc.org/installing.html

# Markdown to PDF
pandoc resume.md -o resume.pdf

# Markdown to DOCX
pandoc resume.md -o resume.docx

# Markdown to HTML
pandoc resume.md -o resume.html
```

### Optional Tools:
- Pandoc: https://pandoc.org/installing.html (for document conversion)
- MiKTeX: https://miktex.org/download (for PDF generation)
- VS Code: https://code.visualstudio.com/ (recommended editor)
"@

Set-Content -Path "$resumePath\README.md" -Value $readme
Write-Host "✅ Quick start guide created" -ForegroundColor Green

# Check for optional tools
Write-Host "`n📦 Checking for optional tools..." -ForegroundColor Yellow

# Check for Pandoc
if (Get-Command pandoc -ErrorAction SilentlyContinue) {
    Write-Host "✅ Pandoc is installed" -ForegroundColor Green
} else {
    Write-Host "⚠️  Pandoc not found. Install from: https://pandoc.org/installing.html" -ForegroundColor Yellow
}

# Check for VS Code
if (Get-Command code -ErrorAction SilentlyContinue) {
    Write-Host "✅ VS Code is installed" -ForegroundColor Green
} else {
    Write-Host "ℹ️  VS Code not found. Install from: https://code.visualstudio.com/" -ForegroundColor Cyan
}

# Check for Claude
if (Get-Command claude -ErrorAction SilentlyContinue) {
    Write-Host "✅ Claude Code is installed" -ForegroundColor Green
} else {
    Write-Host "⚠️  Claude Code not found. Install instructions at: https://docs.claude.com/claude-code" -ForegroundColor Yellow
}

# Final message
Write-Host "`n" -NoNewline
Write-Host "=========================================" -ForegroundColor Magenta
Write-Host "✨ Resume Fine-Tuner Setup Complete! ✨" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Magenta
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Edit your experience: " -NoNewline
Write-Host "$resumePath\experience\my-experience.md" -ForegroundColor Yellow
Write-Host "2. Add job descriptions to: " -NoNewline
Write-Host "$resumePath\job-descriptions\active\" -ForegroundColor Yellow
Write-Host "3. Run Claude Code to generate tailored resumes"
Write-Host ""
Write-Host "📚 Full documentation at: " -NoNewline
Write-Host "$resumePath\README.md" -ForegroundColor Yellow
Write-Host ""
Write-Host "⚠️  IMPORTANT: Restart PowerShell or run this command to activate the Claude function:" -ForegroundColor Red
Write-Host ". `$PROFILE" -ForegroundColor Yellow
Write-Host ""
Write-Host "Happy job hunting! 🚀" -ForegroundColor Green

# Open the resumes folder in Explorer
Write-Host "`nOpening resumes folder..." -ForegroundColor Cyan
Start-Process explorer.exe $resumePath