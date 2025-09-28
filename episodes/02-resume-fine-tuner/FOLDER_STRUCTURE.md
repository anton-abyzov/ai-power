# Episode 02 Folder Structure

## 📂 Public Content (Published to MkDocs)
These files will be visible at https://anton-abyzov.github.io/ai-power/

```
episodes/02-resume-fine-tuner/
├── README.md                    # Episode overview
├── index.md                      # Main landing page
│
├── content/                      # Tutorial sections
│   ├── 00-introduction.md       # What users will learn
│   ├── 01-the-problem.md        # Why resume tailoring matters
│   ├── 02-claude-agents-overview.md
│   ├── 03-workspace-setup.md
│   ├── 04-creating-agent.md
│   ├── 05-experience-definition.md
│   ├── 06-live-demo.md
│   ├── 07-advanced-techniques.md
│   ├── 08-format-options.md
│   ├── 09-results-metrics.md
│   └── 10-conclusion.md
│
├── code-examples/               # Working code users can copy
│   ├── resume-agent-config.yaml
│   ├── experience-database-template.md
│   ├── setup-commands.sh
│   ├── setup-commands.ps1
│   └── conversion-scripts/
│       ├── md-to-pdf.sh
│       └── md-to-docx.sh
│
├── templates/                   # Resume templates for users
│   ├── developer-resume-base.md
│   ├── marketer-resume-base.md
│   ├── pm-resume-base.md
│   └── experience-tracker.yaml
│
├── samples/                     # Example job descriptions
│   ├── microsoft_senior_dotnet_2024.md
│   ├── spotify_ml_engineer_2024.md
│   ├── real-job-examples.md
│   └── sample-job-descriptions.md
│
├── prompts/                     # Agent prompts
│   ├── resume-fine-tuner-agent.md
│   └── experience-extractor.md
│
└── diagrams/                    # Visual aids
    └── diagram-descriptions.md
```

## 🔒 Private Content (Creator Only - Not Published)
These files are for video production only.

```
episodes/02-resume-fine-tuner/
├── 📹 FULL_SCRIPT.md            # YouTube video script (STAYS HERE for easy access)
│
└── _production/                 # ALL PRIVATE PRODUCTION FILES
    ├── VIDEO_GENERATION_GUIDE.md     # How to create each visual
    ├── 📹 PRODUCTION_GUIDE.md        # Overall production guide
    ├── ⏰ TIMESTAMPS (Draft).md      # Video timestamps
    │
    ├── production-notes/             # Recording & editing guides
    │   ├── youtube-metadata.md      # SEO optimization
    │   ├── recording-checklist.md   # Pre-recording checklist
    │   ├── editing-notes.md         # Post-production guide
    │   └── voiceover-script-final.md
    │
    └── assets/                      # Production assets
        ├── thumbnails/              # YouTube thumbnails
        ├── screenshots/             # For video
        └── b-roll/                 # Extra footage notes
```

## 📝 Key Differences

### Public (MkDocs) Content:
- ✅ Tutorial content
- ✅ Working code examples
- ✅ Templates users can download
- ✅ Sample data
- ✅ Documentation

### Private (Production) Content:
- 🎬 Video scripts
- 🎬 Recording instructions
- 🎬 Video generation prompts
- 🎬 Production checklists
- 🎬 SEO metadata
- 🎬 Visual creation guides

## 🎯 Quick Reference

When creating the video:
1. **Main Script**: `📹 FULL_SCRIPT.md` (in root for easy access)
2. **Visual Creation**: `_production/VIDEO_GENERATION_GUIDE.md`
3. **Recording Help**: `_production/production-notes/recording-checklist.md`
4. **Editing Guide**: `_production/production-notes/editing-notes.md`

When users visit the site:
- They see clean tutorials in `content/`
- They can copy code from `code-examples/`
- They can use templates from `templates/`
- They DON'T see any production materials

## 🚀 Publishing Workflow

1. **Video Production**: Use files in `_production/`
2. **Public Docs**: Edit files outside `_production/`
3. **GitHub Push**: `_production/` is gitignored
4. **MkDocs Build**: Only processes public files
5. **Result**: Clean documentation site without production clutter