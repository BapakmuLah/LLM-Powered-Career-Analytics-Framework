
from fastapi import HTTPException
from langchain_core.messages import HumanMessage

from setup.model_setup import llm
from setup.schema import project_parser

# 5D. PORTFOLIO PROJECT RECOMMENDER FUNCTION
def recommend_portfolio(target_role: str, missing_skills: str):
    try:
        PROMPT = """You are an Expert Tech Lead and Career Mentor. A candidate is trying to land a job as a {target_role} but their resume is currently missing practical experience with these key skills: {missing_skills}.
                    
                    Your task is to invent 2 highly practical, impressive portfolio projects that will force the candidate to learn and use these exact missing skills.
                    
                    Rules:
                    - The projects MUST be realistic, enterprise-level applications that solve actual business problems, not generic tutorials.
                    - Provide a clear step-by-step development roadmap.
                    - Detail the exact tech stack needed.
                    - Write a powerful, metrics-driven resume bullet point they can use once the project is finished.
                    - Do NOT include any text outside the required format.
                    
                    {format_instructions}"""
        
        # INJECT VARIABLES INTO PROMPT 
        injected_prompt = PROMPT.format(target_role = target_role,
                                        missing_skills = missing_skills,
                                        format_instructions = project_parser.get_format_instructions())

        # CREATE MESSAGE (Text Only)
        message = HumanMessage(content=[{"type": "text", "text": injected_prompt}])

        # RUN LLM 
        results = llm.invoke([message])
        
        # PARSE OUTPUT
        parsed_output = project_parser.parse(results.content)
        return parsed_output

    except Exception as e:
        raise HTTPException(status_code = 500, detail=f"Error generating project recommendations: {str(e)}")