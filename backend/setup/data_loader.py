
import os
import base64
import docx

from langchain_core.messages import HumanMessage
from langchain_community.document_loaders import PyPDFLoader

# THIS DOCUMENT IS FOCUSED TO ACCEPT DOCUMENT/FILE FROM USER

# 3A. CREATE PDF LOADER FUNCTION
def load_pdf(pdf_path : str):
    
    # LOAD PDF
    pdf_loader = PyPDFLoader(pdf_path)
    pages = pdf_loader.load()

    # MERGE ALL PAGES IN RESUME
    resume_text = "\n".join([page.page_content for page in pages])
    return resume_text


# 3B. CREATE TXT LOADER
def load_txt(txt_path : str):

    # LOAD .txt FILE
    with open(txt_path, mode = 'r', encoding='utf-8') as file:
        return file.read()


# 3C. CREATE DOCUMENTS LOADER
def load_docs(doc_path : str):

    # LOAD .docx
    docs = docx.Document(doc_path)
    return "\n".join([parag for parag in docs.paragraphs])  # --> # MERGE ALL PARAGRAPHS


# 3D. CHECK WHAT TYPE OF THE DOCUMENT
def check_document(file_path : str):

    # GET EXTENSION
    extension = os.path.splitext(file_path)[1].lower()

    # IF FILE IS A PICTURE
    if extension in [".jpg", ".jpeg", ".png", ".webp"]:

        # EXTRACT PICTURE
        with open(file_path, mode = 'rb') as file:
            image_data = base64.b64encode(file.read()).decode("utf-8")

        # FORMAT
        return {"type" : "image_url",
                "image_url" : {"url" : f"data:image/jpeg;base64,{image_data}"}}
        

    # LOAD FILE BASED ON THE EXTENSION
    if extension   == '.pdf' : return load_pdf(file_path)  # --> IF THE FILE IS PDF, THEN CALL load_pdf FUNCTION!
    elif extension == '.txt' : return load_txt(file_path)
    elif extension == '.docx': return load_docs(file_path)
    else : raise ValueError(f"Unsupported Extension {extension}")


# ====================================================

# 4. EXTRACT FILE
def extract_file(file_content, prompt):

    # IF RESUME IS A PICTURE
        if isinstance(file_content, dict):

            message = HumanMessage(content = [{"type" : "text", "text" : prompt}, 
                                               file_content])  # --> BASE64 PICTURE
            
        # IF RESUME IS A TEXT FILE (.pdf, .txt, .docx)
        else:

            # SEND PROMPT + TEXT RESUME
            message = HumanMessage(content = [{"type" : "text", 
                                               "text" : f"{prompt}\n\nResume Content:\n{file_content}"}])
            
        return message
