from google import genai
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv  # ✅ Import load_dotenv
import os
import enum
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Define Pydantic Model

class JOB_LEVEL(enum.Enum):
    ENTRY = "Entry"
    MID = "Mid"
    SENIOR = "Senior"

class JobDescription(BaseModel):
    job_title: str = Field(..., description="Title of the job position")
    company_name: str = Field(..., description="Name of the company hiring")
    level_of_job: JOB_LEVEL
    year_of_experience: str = Field(..., description="Candidate Experience Required, if mentioned ")
    location: str = Field(..., description="Job location, if mentioned")
    required_skills: List[str] = Field(..., description="Skills needed for the role")
    why_join_us: str = Field(..., description="Reasons why candidates should join")
    hashtag: str = Field(..., description="Be creative add multiple hashtags related to the job")


def get_structured_job_description(job_description_text: str) -> JobDescription:
    """Fetches structured job description using Gemini AI."""
    
    prompt = f"""
    Extract the following job description into a structured JSON format.
    Ensure that you only extract information explicitly mentioned in the text and **do not hallucinate** missing details.

    If any field is **not mentioned**, return an appropriate default (e.g., experience = "0+", hashtag = "#Hiring").

    **Job Description Text:**
    {job_description_text}
    """
    
    # Initialize Gemini Client
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Call Gemini API
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": JobDescription,
        },
    )

    # Print JSON response
    print(response.text)

    if not response.text:
        raise ValueError("Failed to get structured job description.")
    # Parse response into Pydantic Model
    job_details: JobDescription = response.parsed
    return job_details

    
