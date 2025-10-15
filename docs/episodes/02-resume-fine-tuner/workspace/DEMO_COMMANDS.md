# Demo Commands - Quick Reference

## Setup (Before Recording)

```bash
# Open VS Code at workspace
cd /Users/antonabyzov/Projects/github/Obsidian/ai-power/episodes/02-resume-fine-tuner/workspace
code .

# In VS Code integrated terminal
claude
```

## Demo 1: Software Engineer

**Note:** You can call the agent two ways:
- `@resume-fine-tuner` (with @ symbol)
- `resume-fine-tuner` (just the name)

### The Prompt:
```
@resume-fine-tuner

Create a tailored resume for this Senior Backend Engineer - Cloud Infrastructure position:

[Open and copy: job-descriptions/senior-backend-engineer-sample.md]

Use experience database: experience-db/software-engineer.md

Output file: outputs/senior-backend-engineer-techscale-2025-10-01.md

Emphasize:
- Python and FastAPI expertise
- Kubernetes and AWS cloud experience
- Microservices architecture
- Performance optimization
- Team leadership and mentoring

Ensure 90%+ keyword match while maintaining authenticity.
```

### After Generation:
```bash
# View the generated resume
cat outputs/senior-backend-engineer-techscale-2025-10-01.md

# Or open in VS Code
code outputs/senior-backend-engineer-techscale-2025-10-01.md
```

## Demo 2: Iterative Refinement (Optional)

```
@resume-fine-tuner

The resume looks great, but can you:
1. Make the professional summary shorter (2 sentences max)
2. Add more quantified metrics to the microservices project
3. Emphasize team leadership throughout

Keep everything else the same.
```

## Show Other Profession Templates

```bash
# Marketing Manager
cat experience-db/marketing-manager.md

# Real Estate Agent
cat experience-db/real-estate-agent.md
```

## Format Conversions (Optional)

```bash
# Convert to Word
pandoc outputs/senior-backend-engineer-techscale-2025-10-01.md -o outputs/resume.docx

# Convert to PDF
pandoc outputs/senior-backend-engineer-techscale-2025-10-01.md -o outputs/resume.pdf
```

## Tips for Recording

1. **Don't speed up Claude's response** - Show it working in real-time (60-90 seconds)
2. **Use a real LinkedIn job** - More authentic than the sample
3. **Show the full prompt** - Don't cut to just "@resume-fine-tuner"
4. **Scroll through generated resume** - Show how well keywords matched
5. **Keep energy high** - This is exciting automation!

## Expected Claude Response Time

- **Job description analysis:** 10-15 seconds
- **Experience database search:** 15-20 seconds
- **Resume generation:** 30-40 seconds
- **Total:** 60-90 seconds (record completely uncut!)

## Files Created

✅ `resume-fine-tuner.md` - Agent configuration
✅ `experience-db/software-engineer.md` - Full experience database
✅ `experience-db/marketing-manager.md` - Template for marketing
✅ `experience-db/real-estate-agent.md` - Template for real estate
✅ `job-descriptions/senior-backend-engineer-sample.md` - Sample job posting

## Ready to Record? ✅

1. Open VS Code at `workspace/` folder
2. Start Claude Code in terminal
3. Have LinkedIn job tab open (or use sample)
4. Copy prompt from above
5. Press Enter and let Claude work!
6. Show generated resume
7. Emphasize: "2 minutes, perfectly tailored, ATS-optimized"
