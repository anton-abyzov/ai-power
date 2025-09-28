#!/bin/bash
# Resume Fine-Tuner Setup Script for Mac/Linux
# Run this script to set up your complete resume automation workspace

echo "🚀 Setting up Resume Fine-Tuner Workspace..."

# Create directory structure
echo "📁 Creating directory structure..."
mkdir -p ~/resumes/{templates,outputs,job-descriptions,experience}
mkdir -p ~/resumes/outputs/{drafts,final,archived}
mkdir -p ~/resumes/job-descriptions/{active,applied,archived}

# Set up Claude Code alias for permission bypass (Mac/Linux)
echo "⚙️  Setting up Claude Code alias..."

# Detect shell
if [ -n "$ZSH_VERSION" ]; then
   SHELL_RC="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
   SHELL_RC="$HOME/.bashrc"
else
   SHELL_RC="$HOME/.profile"
fi

# Check if alias already exists
if ! grep -q "function claude()" "$SHELL_RC"; then
    echo "" >> "$SHELL_RC"
    echo "# Claude Code alias for permission bypass" >> "$SHELL_RC"
    echo 'function claude() {' >> "$SHELL_RC"
    echo '    command claude --dangerously-skip-permissions "$@"' >> "$SHELL_RC"
    echo '}' >> "$SHELL_RC"
    echo "✅ Claude alias added to $SHELL_RC"
else
    echo "ℹ️  Claude alias already exists in $SHELL_RC"
fi

# Create sample experience database
echo "📝 Creating sample experience database..."
cat > ~/resumes/experience/my-experience.md << 'EOF'
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
EOF

echo "✅ Sample experience database created at ~/resumes/experience/my-experience.md"

# Create agent configuration
echo "🤖 Creating agent configuration..."
cat > ~/resumes/resume-agent-config.yaml << 'EOF'
name: resume-fine-tuner
description: AI agent for resume optimization
tools: [Read, Write, Edit, Grep, Glob]
experience_file: ~/resumes/experience/my-experience.md
output_directory: ~/resumes/outputs/
EOF

echo "✅ Agent configuration created at ~/resumes/resume-agent-config.yaml"

# Create sample job description
echo "📄 Creating sample job description..."
cat > ~/resumes/job-descriptions/active/sample-senior-dev.txt << 'EOF'
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
EOF

echo "✅ Sample job description created"

# Install useful tools (optional)
echo ""
echo "📦 Optional: Install useful tools for document conversion"
echo "Run these commands if you want PDF/DOCX conversion:"
echo ""
echo "  # For Mac (using Homebrew):"
echo "  brew install pandoc"
echo "  brew install --cask mactex  # For LaTeX/PDF support"
echo ""
echo "  # For Linux (Ubuntu/Debian):"
echo "  sudo apt-get install pandoc"
echo "  sudo apt-get install texlive-full  # For LaTeX/PDF support"
echo ""

# Create quick start guide
cat > ~/resumes/README.md << 'EOF'
# Resume Fine-Tuner Quick Start

## Setup Complete! 🎉

### Directory Structure:
- `templates/` - Store your base resume templates
- `outputs/` - AI-generated tailored resumes
- `job-descriptions/` - Save job postings
- `experience/` - Your complete experience database

### How to Use:

1. Edit your experience database:
   ```bash
   nano ~/resumes/experience/my-experience.md
   ```

2. Add a job description:
   ```bash
   nano ~/resumes/job-descriptions/active/company-role.txt
   ```

3. Run Claude Code agent:
   ```bash
   cd ~/resumes
   claude "Please tailor my resume for the job in job-descriptions/active/company-role.txt using my experience from experience/my-experience.md"
   ```

4. Find your tailored resume in `outputs/drafts/`

### Pro Tips:
- Keep job descriptions that led to interviews in `applied/`
- Archive old applications in `archived/`
- Track success metrics in a spreadsheet
- Save winning resume versions as templates

### Convert Formats:
```bash
# Markdown to PDF
pandoc resume.md -o resume.pdf

# Markdown to DOCX
pandoc resume.md -o resume.docx

# Markdown to HTML
pandoc resume.md -o resume.html
```
EOF

echo "✅ Quick start guide created at ~/resumes/README.md"

# Final message
echo ""
echo "========================================="
echo "✨ Resume Fine-Tuner Setup Complete! ✨"
echo "========================================="
echo ""
echo "Next steps:"
echo "1. Edit your experience: ~/resumes/experience/my-experience.md"
echo "2. Add job descriptions to: ~/resumes/job-descriptions/active/"
echo "3. Run Claude Code to generate tailored resumes"
echo ""
echo "📚 Full documentation at: ~/resumes/README.md"
echo ""
echo "Happy job hunting! 🚀"

# Source the shell configuration
echo ""
echo "⚠️  Run this command to activate the Claude alias:"
echo "source $SHELL_RC"