import PyPDF2
from google import genai
from flask import Flask, render_template, request, redirect, url_for
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize GenAI Client
# Using env variable for security best practices, falling back to basic setup if needed locally
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

# Define a directory for uploads
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text
        return extracted_text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return redirect(request.url)
    
    file = request.files['resume']
    company_name = request.form.get('company_name')
    job_role = request.form.get('job_role')
    job_desc = request.form.get('job_desc')
    
    if file.filename == '':
        return redirect(request.url)
        
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # 1. Extract Text
        resume_text = extract_text_from_pdf(file_path)
        
        # 2. Analyze with Gemini (Single Call, JSON Mode)
        system_prompt = f'''
        Act as a senior SaaS product designer, AI system architect, and recruiter-tech expert.
        Your task is to analyze a resume against a job description in a single pass and return structured JSON.

        ### INPUT DATA
        Target Company: {company_name}
        Target Role: {job_role}
        
        Job Description:
        """
        {job_desc}
        """

        Resume Text:
        """
        {resume_text}
        """

        ### ANALYSIS LOGIC
        1. Context Analysis: Infer hiring standards for {company_name} and role level for {job_role}.
        2. ATS Simulation: Simulate major ATS parsing. Detect lost data, formatting failures (columns, tables), and keyword matching.
        3. Explainability: Generate specific insights on why a score is given.
        4. Scoring: Generate 4 scores (0-100): ATS Compatibility, Recruiter Relevance, Skill Coverage, Experience Alignment.

        ### OUTPUT FORMAT (Strict JSON)
        Return ONLY valid JSON with this structure:
        {{
            "verdict": "String. One sentence overall summary (e.g. 'Moderately competitive but needs formatting fixes').",
            "scores": {{
                "ats_compatibility": {{ "score": Int, "impact": "String (High/Med/Low)", "insight": "String. Why this score?" }},
                "recruiter_relevance": {{ "score": Int, "impact": "String", "insight": "String" }},
                "skill_coverage": {{ "score": Int, "impact": "String", "insight": "String" }},
                "experience_alignment": {{ "score": Int, "impact": "String", "insight": "String" }}
            }},
            "parsing_insights": [
                {{ "type": "Success", "title": "String", "description": "String" }},
                {{ "type": "Error", "title": "String", "description": "String" }},
                {{ "type": "Risk", "title": "String", "description": "String" }}
            ],
            "top_fixes": [
                {{ "fix": "String", "impact_score": "String (e.g. +10%)", "description": "String" }},
                {{ "fix": "String", "impact_score": "String", "description": "String" }},
                {{ "fix": "String", "impact_score": "String", "description": "String" }}
            ],
            "summary": "String. Professional HR-mentor style summary."
        }}
        '''

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=system_prompt,
                config={
                    'response_mime_type': 'application/json'
                }
            )
            
            raw_text = response.text
            print("--- RAW AI RESPONSE ---")
            print(raw_text)
            print("-----------------------")

            # Clean up potential markdown formatting if the model disregards mime_type
            if raw_text.strip().startswith("```json"):
                raw_text = raw_text.strip().split("```json")[1].split("```")[0].strip()
            elif raw_text.strip().startswith("```"):
                raw_text = raw_text.strip().split("```")[1].split("```")[0].strip()
            
            # Parse JSON
            analysis_json = json.loads(raw_text)
            
        except json.JSONDecodeError as je:
            print(f"JSON Parse Error: {je}")
            # Fallback: try to repair common issues or return specific error
            analysis_json = {
                "verdict": "Technical Analysis Error",
                "scores": {
                    "ats_compatibility": {"score": 0, "impact": "High", "insight": f"The AI returned invalid data structure. Raw error: {str(je)}"}, 
                    "recruiter_relevance": {"score": 0, "impact": "High", "insight": "N/A"},
                    "skill_coverage": {"score": 0, "impact": "High", "insight": "N/A"},
                    "experience_alignment": {"score": 0, "impact": "High", "insight": "N/A"}
                },
                "parsing_insights": [],
                "top_fixes": [{"fix": "Retry Analysis", "impact_score": "High", "description": "Please try submitting again. The AI model output was malformed."}],
                "summary": "There was an issue processing the structured data from the AI. This is a temporary glitch."
            }
        except Exception as e:
            analysis_json = {
                "verdict": "Communication Error",
                "scores": {
                    "ats_compatibility": {"score": 0, "impact": "High", "insight": f"Error: {str(e)}"},
                    "recruiter_relevance": {"score": 0, "impact": "High", "insight": "N/A"},
                    "skill_coverage": {"score": 0, "impact": "High", "insight": "N/A"},
                    "experience_alignment": {"score": 0, "impact": "High", "insight": "N/A"}
                },
                "parsing_insights": [],
                "top_fixes": [],
                "summary": "An unexpected error occurred while connecting to the AI analysis engine."
            }
            
        # Clean up
        try:
            os.remove(file_path)
        except:
            pass
            
        return render_template('result.html', data=analysis_json)

if __name__ == "__main__":
    app.run(debug=True)