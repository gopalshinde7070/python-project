import pdfplumber
from groq import Groq
import json

def extract_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"
    return text.strip()

API_KEY = "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"

import re

def analyze_resume_with_llm(resume_text, job_description):
    client = Groq(api_key=API_KEY)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Return ONLY a JSON object. No explanations."
            },
            {
                "role": "user",
                "content": f"""
Analyze the resume and job description.

Return JSON with this schema:
{{
  "rank": 0-100,
  "skills": [],
  "total_experience": 0,
  "project_category": []
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""
            }
        ],
        temperature=0
    )

    raw = response.choices[0].message.content

    # 🔥 SAFE JSON EXTRACTION
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        raise Exception("No JSON object found in LLM response")

    json_text = match.group()

    return json.loads(json_text)
def process_resume(pdf_path, job_description):
    resume_text = extract_from_pdf(pdf_path)

    if not resume_text:
        raise Exception("Resume text is empty")

    return analyze_resume_with_llm(resume_text, job_description)
