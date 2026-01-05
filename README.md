# Resume Uncle - AI Powered ATS Resume Checker

Resume Uncle is an advanced Applicant Tracking System (ATS) simulator and resume analyzer. It leverages the power of Google's **Gemini 2.5 Flash** model to parse, analyze, and score resumes against specific job descriptions. 

This tool helps job seekers understand how "robot recruiters" view their applications, providing actionable insights to improve their ATS score and recruiter relevance.

## 🚀 Features

*   **PDF Parsing**: robustly extracts text from PDF resumes using `PyPDF2`.
*   **Deep AI Analysis**: Uses `gemini-2.5-flash` to act as a senior expert (SaaS Product Designer / AI Architect / Recruiter).
*   **Comprehensive Scoring System** (0-100):
    *   **ATS Compatibility**: Checks for formatting issues, columns, tables, and parseability.
    *   **Recruiter Relevance**: How well the profile matches the "vibe" and level of the role.
    *   **Skill Coverage**: Hard skill matching against the JD.
    *   **Experience Alignment**: Seniority and background fit.
*   **SWOT-style Parsing Insights**: Identifies Successes, Errors, and Risks in the resume structure.
*   **Actionable Fixes**: Provides a prioritized list of specific improvements to increase the match rate.

## 🛠️ Tech Stack

*   **Backend**: Python, Flask
*   **AI Engine**: Google GenAI SDK (`google-genai`)
*   **PDF Engine**: `PyPDF2`
*   **Frontend**: HTML5, Vanilla CSS (Modern Design), JavaScript
*   **Environment**: `python-dotenv`

## ⚙️ Installation & Setup

### Prerequisites
*   Python 3.8 or higher
*   A Google Cloud API Key with access to Gemini models.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/resume-ats.git
cd resume-ats
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install flask google-genai pypdf2 python-dotenv
```

### 4. Configure Environment Variables
Create a file named `.env` in the root directory:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
```bash
python main.py
```
The application will start at `http://127.0.0.1:5000/`.

## 📖 Usage Guide

1.  **Launch the App**: Open your browser to the local server address.
2.  **Upload Resume**: Select your PDF resume file.
3.  **Enter Job Details**:
    *   **Target Company**: e.g., "Google", "Startup Inc."
    *   **Target Role**: e.g., "Senior Backend Engineer"
    *   **Job Description**: Paste the full text of the job posting.
4.  **Analyze**: Click the button and wait for the AI to simulate the ATS process.
5.  **Review Results**: detailed scores, insights, and formatting advice.

## 📂 Project Structure

```
├── main.py              # Application entry point and detailed AI logic
├── check_models.py      # Utility to list available Gemini models
├── prompts.txt         # Sample prompts or JD data (for testing)
├── static/
│   ├── css/            # Stylesheets
│   └── js/             # Client-side scripts
├── templates/
│   ├── index.html      # Landing page
│   ├── upload.html     # Upload form
│   └── result.html     # Analysis dashboard
└── README.md
```

## 🤝 Contributing

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
