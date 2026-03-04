
from datetime import datetime
from fastapi import HTTPException

from setup.model_setup import llm
from setup.data_loader import check_document, extract_file
from setup.schema import ResumeCritique, resume_parser



# 5A. RESUME CRITIQUE 
def resume_critique(file_path: str) -> ResumeCritique:

    try:

        # LOAD DOCUMENTS 
        resume_content = check_document(file_path = file_path)

        # CURRENT DATE (CURRENT REQUEST TIME)
        current_date = datetime.now().strftime(format="%B %Y")
        
        # PROMPT
        prompt_template = """You are a brutally strict senior technical recruiter performing a full resume writing audit.
                                                    Current date: {current_date}
                                                    Your task: Critique EVERY writing weakness in the resume.
                                                    
                                                    Rules: - Do NOT limit the number of suggestions. 
                                                        - Scan section by section.
                                                        - Scan bullet by bullet.
                                                        - If something is weak, vague, unquantified, structurally wrong, or unclear → critique it.
                                                        - If something is already strong and correct → do NOT invent criticism.
                                                        - Continue listing suggestions until no further writing improvements can be made.
                                                        
                                                    Focus strictly on: - PRAQ structure
                                                                    - Quantification gaps
                                                                    - Weak verbs
                                                                    - Missing business impact
                                                                    - Structural ordering issues
                                                                    - Section misplacement
                                                                    - ATS clarity
                                                                    - Formatting inconsistencies
                                                                    - Redundant wording
                                                                    - Vague technical descriptions
                                                                    - Overly long bullets
                                                                    - Missing role clarity
                                                                    - Skill misprioritization
                                                                    
                                                    DO NOT: - Give career advice
                                                            - Talk about recruiters reviewing code
                                                            - Suggest generic improvements
                                                            
                                                    Severity definition: HIGH = blocks hiring decision
                                                                        MEDIUM = important improvement
                                                                        LOW = polish
                                                                        
                                                    Format strictly: 
                                                    HIGH 
                                                    <recommendation>
                                                    
                                                    MEDIUM
                                                    <recommendation>
                                                    
                                                    LOW
                                                    <recommendation>
                                                    
                                                    Continue until fully audited.
                                                    {format_instructions}"""

        # INJECT RESUME INTO PROMPT 
        injected_prompt = prompt_template.format(current_date = current_date, format_instructions = resume_parser.get_format_instructions())


        # EXTRACT FILE (WHETHER ITS TEXT OR IMAGE)
        human_message = extract_file(file_content = resume_content, prompt = injected_prompt)

        # RUN LLM 
        results = llm.invoke([human_message])
        
        # PARSE OUTPUT
        parsed_output = resume_parser.parse(results.content)
        return parsed_output

    except Exception as e:
        raise HTTPException(status_code = 500, detail=f"Error processing document: {str(e)}")