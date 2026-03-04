
from fastapi import HTTPException

import setup.schema
from setup.model_setup import llm
from setup.data_loader import check_document, extract_file


# 5B. CV JOB PREDICTION FUNCTION
def job_prediction(file_path : str):

    try:
        # LOAD PDF
        resume_content = check_document(file_path = file_path)

        PROMPT = """You are an AI Career Analyst system. Analyze the following resume text and determine list of most suitable job positions (job titles) 
                    for this candidate based on their skills, experience, and education.
                    Rules: - Return multiple job predictions.
                           - Probability must be between 1-100.
                           - Base reasoning strictly on resume evidence.
                           - PERFORM SKILL GAP ANALYSIS: Compare their current resume against industry standards for each predicted role. Tell them exactly what technical skills, keywords, or project experiences they are missing to hit a >95% match rate.
                           - Do NOT include any text outside the required format.        
                    {format_instructions}"""
        
        # INJECT RESUME INTO PROMPT 
        injected_prompt = PROMPT.format(format_instructions = setup.schema.job_parser.get_format_instructions())

        # EXTRACT FILE (WHETHER ITS TEXT OR IMAGE)
        human_message = extract_file(file_content = resume_content, prompt = injected_prompt) 
        
        # RUN LLM
        results = llm.invoke([human_message])

        # PARSE OUTPUT
        parsed_output = setup.schema.job_parser.parse(results.content)
        return parsed_output
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail = f"Error Preprocessing Document : {str(e)}")