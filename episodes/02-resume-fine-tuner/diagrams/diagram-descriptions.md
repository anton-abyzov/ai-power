# Excalidraw Diagrams for Episode 02

## Required Diagrams

### 1. Broad Experience vs Focused JDs
**Frame ID**: `resume-problem-overview`
**Description**: Visual showing the mismatch between broad developer experience and focused job requirements
**Elements**:
- Left side: Developer with bubbles showing multiple skills (C#, Python, JS, Azure, AWS, Docker, K8s, etc.)
- Center: Arrow pointing to multiple JDs
- Right side: Different JDs each highlighting specific requirements
- Use colors: Yellow for skills, Blue for requirements, Red for mismatches

### 2. Agent Architecture Workflow
**Frame ID**: `agent-workflow-diagram`
**Description**: Step-by-step flow of how the resume agent processes information
**Elements**:
1. Input: Job Description (document icon)
2. Process 1: Extract Keywords (magnifying glass)
3. Process 2: Query Experience Database (database icon)
4. Process 3: Match & Rank (sorting icon)
5. Process 4: Generate Tailored Resume (document with checkmark)
6. Output: Optimized Resume
- Use arrows showing data flow
- Color code: Green for process steps, Blue for data

### 3. Experience Mapping Matrix
**Frame ID**: `experience-database-structure`
**Description**: How to organize your career experience for AI consumption
**Structure**:
```
Projects
├── Company
├── Technologies []
├── Achievements []
├── Metrics {}
├── Team Size
└── Duration
```
- Show as interconnected nodes
- Use different shapes for different data types
- Include example data in smaller text

### 4. Multiple Resume Versions Strategy
**Frame ID**: `resume-versioning-strategy`
**Description**: Strategy for maintaining different resume focuses
**Elements**:
- Central: Master Experience Database
- Branches:
  - Backend-Heavy Version
  - Cloud Architecture Focus
  - Leadership Emphasis
  - Startup Version
  - Enterprise Version
- Show how each pulls different aspects from master
- Use color coding for different focus areas

### 5. Do's and Don'ts Checklist
**Frame ID**: `resume-best-practices`
**Description**: Visual guide for authentic resume creation
**Layout**: Two columns
**DO's** (Green):
- ✅ Realistic metrics (15-30%)
- ✅ Mix technical and soft skills
- ✅ Natural language variety
- ✅ Specific project details
- ✅ Update regularly

**DON'Ts** (Red):
- ❌ 10x improvements everywhere
- ❌ Fake experience
- ❌ Robotic language
- ❌ Generic descriptions
- ❌ Forget human review

### 6. File Organization System
**Frame ID**: `file-organization`
**Description**: Smart naming and organization for resume files
**Structure**:
```
~/resumes/
├── templates/
│   ├── base-resume.md
│   └── sections/
├── outputs/
│   ├── experience_microsoft_senior_dotnet_2024.md
│   └── experience_google_ml_engineer_2024.md
└── job-descriptions/
    └── archived/
```

### 7. Resume Transformation Example
**Frame ID**: `before-after-resume`
**Description**: Side-by-side comparison of generic vs tailored resume
**Layout**:
- Left: Generic resume with broad statements
- Center: Agent processing (with gears/magic)
- Right: Tailored resume with specific JD keywords highlighted
- Use highlighting to show matched keywords

### 8. Success Metrics Dashboard
**Frame ID**: `success-metrics`
**Description**: Results from using the AI-powered system
**Elements**:
- Response Rate: 15% → 45% (bar chart)
- Time to Interview: 2 weeks → 24 hours
- Offers Received: Multiple competing offers
- Time Saved: 2 hours → 2 minutes per application
- Use charts and graphs with vibrant colors

## Color Palette
- Primary: #7c4dff (Purple - Claude brand)
- Success: #4caf50 (Green)
- Warning: #ff9800 (Orange)
- Error: #f44336 (Red)
- Info: #2196f3 (Blue)
- Background: #f5f5f5 (Light gray)
- Text: #212121 (Dark gray)

## Typography
- Headers: Bold, Sans-serif
- Body: Regular, Sans-serif
- Code: Monospace
- Annotations: Italic, smaller size

## Style Guidelines
- Use rounded rectangles for process boxes
- Arrows should be curved, not straight
- Include emoji/icons where appropriate
- Keep consistent spacing (grid-based)
- Add subtle shadows for depth
- Use dashed lines for optional flows
- Solid lines for required flows