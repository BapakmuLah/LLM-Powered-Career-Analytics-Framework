
from fastapi import HTTPException

from setup.model_setup import llm
from setup.data_loader import check_document, extract_file
from setup.schema import salary_parser

# 5C. SALARY ESTIMATION FUNCTION
def salary_estimation(file_path: str):
    try:
        # LOAD DOCUMENTS 
        resume_content = check_document(file_path = file_path)

        # PROMPT
        PROMPT = """You are an Expert Tech Recruiter and Compensation Analyst. Analyze the provided resume to estimate the candidate's market value.
                    
                    Rules:
                    - Determine the candidate's true seniority level based on their business impact and experience, not just their previous job titles.
                    - Provide a realistic annual salary range (in USD) assuming a global remote or US tech market standard.
                    - Provide highly specific negotiation strategies. For example, if they have rare skills (like Kubernetes or LLMs), tell them to use that as leverage. If they lack years of experience, give tips on how to pivot focus to their portfolio.
                    - Do NOT include any text outside the required format.
                    
                    {format_instructions}"""

        # INJECT RESUME INTO PROMPT 
        injected_prompt = PROMPT.format(format_instructions = salary_parser.get_format_instructions())

        # EXTRACT FILE (WHETHER ITS TEXT OR IMAGE)
        human_message = extract_file(file_content = resume_content, prompt = injected_prompt)

        # RUN LLM 
        results = llm.invoke([human_message])
        
        # PARSE OUTPUT
        parsed_output = salary_parser.parse(results.content)
        return parsed_output

    except Exception as e:
        raise HTTPException(status_code = 500, detail=f"Error processing document for salary estimation: {str(e)}")