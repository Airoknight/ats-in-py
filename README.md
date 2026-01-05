# HireLens — ATS Resume Checker

HireLens is an AI-powered ATS (Applicant Tracking System) resume checker designed to simulate how real hiring systems and recruiters evaluate resumes.  
The product focuses on **clarity, explainability, and professional credibility**, helping users understand *why* a resume works or fails — not just giving a score.

---

## 🚀 Project Vision

Most resume checkers focus on keyword matching.  
HireLens goes further by combining:

- Realistic ATS parsing simulation  
- Recruiter readability analysis  
- Semantic job description matching  
- Clear, actionable feedback  

The goal is not to “beat the ATS,” but to **maximize interview probability**.

---

## ✨ Key Features

### 🔍 Single-Call AI Resume Analysis
- All inputs are processed in **one AI API call**
- No chained or hidden processing
- Faster, cheaper, and easier to scale

### 📊 Multi-Dimensional Scoring
HireLens generates four explainable scores:
- **ATS Compatibility Score**
- **Recruiter Relevance Score**
- **Skill Coverage Score**
- **Experience Alignment Score**

Each score includes human-readable reasoning.

---

### 🧠 Parsing & Risk Insights
Shows how ATS systems interpret the resume:
- Misread job titles
- Broken or ambiguous dates
- Experience gap risks
- ATS-breaking formatting elements

Example:
> “Your job title was parsed incorrectly due to a two-column layout.”

---

### 🧩 Recruiter-Readable Feedback
- Detects task-based vs impact-based bullets
- Highlights clarity, density, and skimmability issues
- Focuses on what recruiters notice in the first few seconds

---

### 🎯 Action-Oriented Fixes
- Displays **Top 3 highest-impact fixes**
- Ranked by shortlist probability improvement
- Avoids overwhelming users with too many suggestions

---

## 🧱 Architecture Overview

### Inputs
- Company Name
- Job Role
- Full Job Description
- Resume (PDF/DOCX)

### Processing
- Single AI call using Gemini API
- Semantic matching
- ATS parsing simulation
- Formatting survivability detection
- Recruiter readability analysis

### Outputs
- Scores
- Parsing insights
- Risk flags
- Actionable recommendations
- Structured JSON response for UI rendering

---

## 🎨 UI / UX Design Principles

- **Glassmorphism** with frosted panels
- Professional, enterprise-grade visual language
- No playful or cartoonish UI
- Progressive disclosure via scrolling
- Expandable sections instead of step-by-step navigation

### Color Palette
- Primary: Cool blues
- Secondary: Slate gray, muted teal, steel blue
- Accent: Soft cyan
- **No purple**

---

## 🧭 User Experience Flow

1. Upload resume and job description
2. Short analysis animation (magnifying glass search)
3. Results displayed in layers:
   - Overall verdict + scores
   - Score explanations
   - Parsing & risk insights
   - Top fixes
4. Optional upgrade actions

No forced steps. No hidden information.

---

## 🔐 Trust & Privacy

- No resume resale
- Clear data handling boundaries
- Designed for professional and enterprise use
- Results are explainable, not black-box

---

## 🛠️ Tech Stack (Suggested)

- Frontend: React / Next.js
- Styling: Tailwind CSS
- Animations: Framer Motion
- AI: Google Gemini API (`gemini-1.5-flash`)
- File Parsing: PDF/DOCX text extraction
- State & Caching: Local + server-side caching

---

## 💡 Why HireLens Is Different

- Simulates real ATS behavior
- Explains results like a human recruiter
- Focuses on decision clarity, not keyword spam
- Designed as a career optimization engine, not a toy

---

## 📌 Assignment Statement

> “HireLens uses a single-call AI architecture and progressive disclosure UX to analyze resumes through both ATS and recruiter perspectives, providing transparent, actionable feedback that improves interview probability.”

---

## 📈 Future Enhancements

- Role- and company-specific resume versions
- Outcome tracking (interview / rejection feedback loop)
- Market benchmarking
- Cover letter and LinkedIn optimization

---

## 🧑‍💻 Author

Built as an academic and product-design project to demonstrate modern AI-powered SaaS architecture, UX design, and recruiter-tech thinking.

---

## 📄 License

This project is for educational and demonstration purposes.
