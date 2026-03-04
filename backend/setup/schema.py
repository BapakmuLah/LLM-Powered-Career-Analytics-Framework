
from pydantic import BaseModel, Field
from typing import Literal, List

from langchain_core.output_parsers import PydanticOutputParser

# ============= THIS FILE IS FOCUSED ON BUILDING A SCHEMA =======================

# 2A. BUILD RESUME CRITIQUE SCHEMA
class Suggestion(BaseModel):
    severity: Literal["HIGH", "MEDIUM", "LOW"]
    recommendation: str = Field(description="Clear actionable improvement suggestion")

# CRITIQUE RESULT
class ResumeCritique(BaseModel):
    suggestions: List[Suggestion]



# 2B. BUILD CV JOB PREDICTION SCHEMA
class jobMatching(BaseModel):
    job_title: str = Field(description = "Predicted Job Title")
    probability: int = Field(description = "Match Probability Percentage (0 - 100)")
    reason: str = Field(description = "Short Explanation based on resume evidence")
    skill_gap: str = Field(description = "Skill gap analysis. Tell them what industry skills/keywords they are missing to reach a probability of 95%+.")

# NUMBER OF MATCHING
class jobPrediction(BaseModel):
    jobs : List[jobMatching]



# 2C. BUILD SALARY ESTIMATION SCHEMA
class SalaryEstimation(BaseModel):
    seniority_level: str = Field(description="Detected seniority level (e.g., Entry-Level, Mid-Level, Senior, Lead, Staff) based on resume impact.")
    estimated_salary_range: str = Field(description="Estimated global tech market salary range in USD (e.g., '$70,000 - $100,000').")
    justification: str = Field(description="Explanation of why this salary range fits, based on their specific skills and years of experience.")
    negotiation_tips: List[str] = Field(description="3 to 5 highly specific salary negotiation strategies tailored to the strengths (leverage) and weaknesses found in this resume.")


# 2D. BUILD PORTFOLIO PROJECT RECOMMENDER SCHEMA

# REQUEST SCHEMA
class ProjectRequest(BaseModel):
    target_role: str = Field(..., example="Senior AI Engineer")
    missing_skills: str = Field(..., example="Multi-Agent Systems, LangChain, Cloud Deployment")

# OUTPUT SCHEMA
class ProjectStep(BaseModel):
    step_name: str = Field(description="Title of the step, e.g., 'Setup Environment & Database'")
    action: str = Field(description="Detailed technical action to perform in this step.")

class PortfolioProject(BaseModel):
    project_name: str = Field(description="Catchy and professional project name.")
    description: str = Field(description="Brief overview of the business problem this project solves.")
    tech_stack: List[str] = Field(description="List of all technologies and frameworks used.")
    steps: List[ProjectStep] = Field(description="Step-by-step roadmap to build the project.")
    cv_bullet_point: str = Field(description="A powerful, PRAQ-formatted bullet point to put on the resume once this project is completed.")

# LIST OF PROJECT SCHEMA
class ProjectRecommendationList(BaseModel):
    projects: List[PortfolioProject]


# DEFINE PARSER
resume_parser = PydanticOutputParser(pydantic_object = ResumeCritique)
job_parser = PydanticOutputParser(pydantic_object = jobPrediction)
salary_parser = PydanticOutputParser(pydantic_object = SalaryEstimation)
project_parser = PydanticOutputParser(pydantic_object = ProjectRecommendationList)