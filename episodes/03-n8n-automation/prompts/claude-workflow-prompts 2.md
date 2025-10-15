# Claude Workflow Prompts for N8N

Reusable Claude API prompts for common N8N automation tasks. Use these in HTTP Request nodes calling the Anthropic API.

---

## 📧 EMAIL & COMMUNICATION

### Email Sentiment Analysis
```
Analyze the sentiment and urgency of this email:

From: {{ $json.from }}
Subject: {{ $json.subject }}
Body: {{ $json.body }}

Provide:
1. Sentiment: positive, neutral, or negative
2. Urgency: low, medium, high, or critical
3. Category: support, sales, inquiry, complaint, or other
4. Key points: bullet list of main topics
5. Suggested response tone: professional, friendly, apologetic, or enthusiastic

Format as JSON.
```

### Draft Email Reply
```
Draft a professional email reply to this customer inquiry:

Original Email:
From: {{ $json.from }}
Subject: {{ $json.subject }}
Body: {{ $json.body }}

Customer Context:
- Customer tier: {{ $json.customerTier }}
- Previous interactions: {{ $json.history }}

Requirements:
- Tone: helpful and professional
- Address all their questions
- Provide actionable next steps
- Keep under 200 words
- Include signature: "Best regards, [Name]"

Generate the email body only.
```

### Meeting Summary
```
Summarize this meeting transcript into actionable items:

Meeting: {{ $json.title }}
Date: {{ $json.date }}
Attendees: {{ $json.attendees }}
Transcript: {{ $json.transcript }}

Provide:
1. Key decisions made
2. Action items (with assigned person if mentioned)
3. Follow-up questions
4. Next meeting date/time (if discussed)

Use bullet points, be concise.
```

---

## 📝 CONTENT GENERATION

### Blog Post Summary
```
Summarize this blog article for social media distribution:

Title: {{ $json.title }}
Author: {{ $json.author }}
Content: {{ $json.content }}

Create three versions:

1. LinkedIn Post (200-300 words):
   - Professional tone
   - Industry insights
   - Call to action
   - Include relevant hashtags

2. Twitter Thread (10 tweets):
   - Conversational tone
   - Hooks and cliffhangers
   - Thread format (1/10, 2/10, etc.)
   - Engaging CTAs

3. Short Summary (50 words):
   - Key takeaway only
   - For email newsletters

Return as JSON with keys: linkedin, twitter, summary
```

### LinkedIn Post Generator
```
Generate an engaging LinkedIn post about this topic:

Topic: {{ $json.topic }}
Key Points: {{ $json.keyPoints }}
Target Audience: {{ $json.audience }}
Call to Action: {{ $json.cta }}

Requirements:
- Hook in first sentence
- Use storytelling or data
- Personal or professional anecdote
- 3-5 short paragraphs
- Include 5 relevant hashtags
- Engaging question at the end
- 200-300 words total

Generate the complete post.
```

### Twitter Thread Creator
```
Create a viral Twitter thread about:

Topic: {{ $json.topic }}
Key Message: {{ $json.message }}
Supporting Facts: {{ $json.facts }}

Requirements:
- 8-10 tweets
- Hook in first tweet
- Each tweet builds on previous
- Use numbers, quotes, or questions
- Clear conclusion with CTA
- Thread format: "1/10", "2/10", etc.
- Conversational, not formal
- Maximum 280 characters per tweet

Return as JSON array: [{number: "1/10", text: "..."}, ...]
```

### Video Script Generator
```
Write a YouTube video script outline for:

Topic: {{ $json.topic }}
Duration: {{ $json.duration }} minutes
Style: {{ $json.style }}
Target Audience: {{ $json.audience }}

Structure:
1. Hook (0:00-0:15): Attention-grabbing opening
2. Introduction (0:15-1:00): What viewer will learn
3. Main Content (1:00-X:00): Step-by-step breakdown
4. Demonstration (if applicable)
5. Results/Benefits
6. Call to Action
7. Closing

For each section, provide:
- Timestamp
- Key talking points (bullet list)
- Screen recordings needed
- B-roll suggestions

Concise, actionable, no fluff.
```

---

## 🤖 CUSTOMER SUPPORT

### Support Ticket Classification
```
Classify this support ticket:

Ticket ID: {{ $json.ticketId }}
From: {{ $json.customerEmail }}
Subject: {{ $json.subject }}
Message: {{ $json.message }}
Customer Plan: {{ $json.plan }}

Analyze and provide:
1. Category: billing, technical, feature-request, bug-report, general-inquiry
2. Priority: low, medium, high, urgent
3. Estimated Resolution Time: 1h, 4h, 24h, 48h, 1-week
4. Suggested Team: support, engineering, billing, product
5. Auto-response: Yes/No (can this be auto-answered?)
6. Key Issues: bullet list

Format as JSON.
```

### FAQ Answer Generator
```
Generate a helpful FAQ answer for this customer question:

Question: {{ $json.question }}
Product: {{ $json.product }}
Customer Type: {{ $json.customerType }}

Use our knowledge base:
{{ $json.knowledgeBase }}

Requirements:
- Clear, concise answer (under 150 words)
- Step-by-step if applicable
- Include relevant links: [Link Text](URL)
- Friendly, helpful tone
- Ask if they need further assistance

Provide answer only.
```

### Bug Report Analysis
```
Analyze this bug report and suggest next steps:

Report:
Title: {{ $json.title }}
Description: {{ $json.description }}
Steps to Reproduce: {{ $json.steps }}
Expected Behavior: {{ $json.expected }}
Actual Behavior: {{ $json.actual }}
Environment: {{ $json.environment }}

Provide:
1. Severity: critical, high, medium, low
2. Likely Cause: hypothesis based on description
3. Affected Users: estimate (few, many, all)
4. Reproducibility: always, sometimes, rare
5. Priority: immediate, high, medium, low
6. Suggested Investigation Steps: bullet list
7. Workaround: if any available

Format as JSON.
```

---

## 📊 DATA ANALYSIS

### Data Summarization
```
Summarize this dataset:

Data: {{ $json.data }}

Provide:
1. Total Records: count
2. Key Metrics: average, min, max, median
3. Trends: increasing, decreasing, stable
4. Outliers: any unusual data points
5. Insights: 3-5 actionable takeaways
6. Recommendations: what to do with this data

Use plain language, no jargon.
```

### Survey Response Analysis
```
Analyze these survey responses:

Question: {{ $json.question }}
Responses: {{ $json.responses }}
Total Respondents: {{ $json.total }}

Provide:
1. Sentiment Distribution: positive %, neutral %, negative %
2. Common Themes: top 5 recurring topics
3. Notable Quotes: 3-5 representative responses
4. Key Insights: what does this tell us?
5. Action Items: what should we do based on this feedback?

Be objective, data-driven.
```

### Competitor Analysis
```
Analyze this competitor information:

Competitor: {{ $json.competitorName }}
Product: {{ $json.productName }}
Pricing: {{ $json.pricing }}
Features: {{ $json.features }}
Customer Reviews: {{ $json.reviews }}

Our Product Context: {{ $json.ourProduct }}

Provide:
1. Strengths: what they do well
2. Weaknesses: where they fall short
3. Unique Features: what they have that we don't
4. Pricing Comparison: are we competitive?
5. Opportunities: what can we learn or exploit?
6. Threats: what should we be concerned about?

SWOT format preferred.
```

---

## 🎬 SORA 2 VIDEO PROMPTS

### Article to Video Prompt
```
Convert this article into a Sora 2 video prompt:

Article Title: {{ $json.title }}
Main Theme: {{ $json.theme }}
Key Visual Concepts: {{ $json.concepts }}

Generate a cinematic Sora 2 prompt that:
- Represents the article's core message visually
- Uses cinematic camera angles and lighting
- Specifies 16:9 aspect ratio, 1080p
- Includes atmosphere and mood
- 10-20 second duration
- No text/words needed (Sora struggles with text)

Example format:
"Cinematic shot of [subject] [action] in [setting]. [Camera movement]. [Lighting]. [Mood]. 1080p, 16:9."

Provide the complete prompt.
```

### Brand Story Video Prompt
```
Create a Sora 2 video prompt for brand storytelling:

Brand: {{ $json.brandName }}
Industry: {{ $json.industry }}
Core Values: {{ $json.values }}
Target Emotion: {{ $json.emotion }}

Generate a 15-second cinematic video prompt that:
- Captures brand essence visually
- Evokes target emotion
- Uses metaphor or symbolism
- Professional, high-production value
- Memorable visual hook

Provide detailed Sora 2 prompt (200-300 words).
```

---

## 🔍 SEO & RESEARCH

### SEO Meta Description
```
Generate an SEO-optimized meta description for:

Page Title: {{ $json.title }}
Content Summary: {{ $json.summary }}
Primary Keyword: {{ $json.keyword }}
Secondary Keywords: {{ $json.secondaryKeywords }}

Requirements:
- 150-160 characters
- Include primary keyword naturally
- Compelling call-to-action
- No clickbait
- Accurate representation of content

Provide meta description only.
```

### Keyword Research Analysis
```
Analyze these search queries for content opportunities:

Queries: {{ $json.queries }}
Our Domain: {{ $json.domain }}

For each query, provide:
1. Search Intent: informational, navigational, transactional, commercial
2. Difficulty: easy, medium, hard (based on competitiveness)
3. Content Type: blog, landing page, guide, comparison, tutorial
4. Suggested Title: SEO-friendly, click-worthy
5. Key Points to Cover: bullet list

Prioritize by opportunity (high traffic + low difficulty).
```

---

## 🛠️ CODE & TECHNICAL

### API Error Explanation
```
Explain this API error in plain language:

Error Code: {{ $json.errorCode }}
Error Message: {{ $json.errorMessage }}
API Endpoint: {{ $json.endpoint }}
Request Method: {{ $json.method }}

Provide:
1. What Happened: simple explanation
2. Why It Happened: likely cause
3. How to Fix: step-by-step solution
4. Prevention: how to avoid in future

No technical jargon, assume non-technical user.
```

### JSON Data Transformation
```
Transform this JSON data for {{ $json.targetSystem }}:

Source Data: {{ $json.sourceData }}
Source Format: {{ $json.sourceFormat }}
Target Format: {{ $json.targetFormat }}

Requirements:
- Map all fields correctly
- Handle missing data gracefully (use defaults)
- Validate data types
- Return valid JSON

Provide:
1. Transformed JSON
2. Mapping explanation: which source field → target field
3. Any data loss or conversions made

Return as JSON with keys: transformedData, mapping, notes
```

---

## 🎯 SALES & MARKETING

### Sales Email Personalization
```
Personalize this sales email for the prospect:

Template: {{ $json.template }}

Prospect Information:
- Name: {{ $json.name }}
- Company: {{ $json.company }}
- Industry: {{ $json.industry }}
- Pain Points: {{ $json.painPoints }}
- Recent Activity: {{ $json.activity }}

Requirements:
- Reference their industry/company specifically
- Address their pain points
- Show you've done research (mention recent activity)
- Value-focused, not feature-focused
- Clear call-to-action
- Keep under 150 words

Generate personalized email.
```

### Product Description Generator
```
Write a compelling product description:

Product: {{ $json.productName }}
Category: {{ $json.category }}
Key Features: {{ $json.features }}
Benefits: {{ $json.benefits }}
Target Audience: {{ $json.audience }}
Price Point: {{ $json.price }}

Requirements:
- Benefit-driven (not just features)
- Address target audience pain points
- Social proof or credibility markers
- Clear unique selling proposition
- Call-to-action
- 100-150 words
- Scannable (use bullet points for key features)

Provide complete product description.
```

---

## 📅 SCHEDULING & PLANNING

### Meeting Agenda Generator
```
Create a meeting agenda based on these inputs:

Meeting Purpose: {{ $json.purpose }}
Attendees: {{ $json.attendees }}
Duration: {{ $json.duration }} minutes
Key Topics: {{ $json.topics }}
Desired Outcomes: {{ $json.outcomes }}

Generate:
1. Meeting Title
2. Time-boxed Agenda:
   - Welcome (5 min)
   - Topic 1 (X min)
   - Topic 2 (X min)
   - Q&A (X min)
   - Action Items & Next Steps (5 min)
3. Pre-meeting Materials: what attendees should review
4. Success Criteria: how we know the meeting was productive

Professional format, clear structure.
```

---

## 💡 HOW TO USE THESE PROMPTS IN N8N

### HTTP Request Node Configuration

```javascript
// Node: HTTP Request (Claude API)
{
  "method": "POST",
  "url": "https://api.anthropic.com/v1/messages",
  "authentication": "predefinedCredentialType",
  "nodeCredentialType": "anthropicApi",
  "headers": {
    "anthropic-version": "2023-06-01"
  },
  "body": {
    "model": "claude-sonnet-4-5-20250929",
    "max_tokens": 2048,
    "messages": [
      {
        "role": "user",
        "content": "{{ $json.prompt }}"
      }
    ]
  },
  "options": {
    "response": {
      "response": {
        "neverError": true,
        "responseFormat": "json"
      }
    }
  }
}
```

### Extract Claude Response (Code Node)

```javascript
// Node: Code (JavaScript)
const response = $input.item.json;

// Extract text from Claude's response
const content = response.content[0].text;

// Optional: Parse as JSON if Claude returned JSON
let parsedContent;
try {
  parsedContent = JSON.parse(content);
} catch (e) {
  parsedContent = { text: content };
}

return {
  json: {
    claudeResponse: content,
    parsed: parsedContent,
    model: response.model,
    usage: response.usage
  }
};
```

---

## 🎓 TIPS FOR EFFECTIVE PROMPTS

1. **Be Specific:** Define exact output format (JSON, plain text, bullets)
2. **Provide Context:** Include all relevant information
3. **Set Constraints:** Word count, tone, style
4. **Use Variables:** Reference N8N node data with `{{ $json.field }}`
5. **Request Structure:** Ask for specific sections or format
6. **Include Examples:** Show Claude what good output looks like
7. **Test Iteratively:** Refine prompts based on results
8. **Handle Errors:** Plan for unexpected Claude responses

---

**Use these prompts as templates. Customize for your specific use case.**
