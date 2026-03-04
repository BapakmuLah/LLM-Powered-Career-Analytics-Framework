import os
import tempfile

import docx
import base64
from io import BytesIO
from PIL import Image

from datetime import datetime
from typing import Literal, List

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_community.document_loaders import PyPDFLoader

from setup.model_setup import llm
from setup.data_loader import check_document, extract_file
from setup.schema import ResumeCritique, jobPrediction, ProjectRecommendationList, ProjectRequest, SalaryEstimation
from module.resume_critique import resume_critique
from module.career_recommendation import job_prediction
from module.salary_estimation import salary_estimation
from module.project_recommendation import recommend_portfolio


# DEFINE FAST API MODEL
app = FastAPI(title="AI Resume Critique API", 
              description="Endpoint untuk melakukan audit CV menggunakan Gemini dan LangChain", 
              version="1.0.0")

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


# =======================================================

# 6. API ENDPOINT


# ALLOWED EXTENSIONS
ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.jpg', '.jpeg', '.png', '.webp'}


# 6A. CHECK STATUS
@app.get(path = '/')
def running():
    return "Full API Documentation : https://sandking-indonesian-job-salary-predictor.hf.space/"


# 6B. CRITIQUE RESUME ENDPOINT
@app.post("/critique-resume", response_model = ResumeCritique)
async def resume_critique_endpoint(file: UploadFile = File(...)):

    # GET UPLOADED FILE EXTENSION
    extension = os.path.splitext(file.filename)[1].lower()

    # IF USER UPLOADED NOT SUPPORTED EXTENSION
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code = 400, detail = f"{extension} File is not Supported Anymore!")

    # CREATE TEMPORARY FIL TO SAVE UPLOADED FILE
    with tempfile.NamedTemporaryFile(delete=False, suffix = extension) as tmp:
        
        # READ UPLOADED FILE
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        # RUN MAIN FUNCTION
        result = resume_critique(tmp_path)
        
        # SORT BY SEVERITY ON DESCENDING
        severity_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
        result.suggestions = sorted(result.suggestions, key=lambda x: severity_order[x.severity])
        
        return result
        
    finally:
         
        # DELETE TEMPORARY FILE AFTER COMPLETION (TO RELEASE MEMORY)
         if os.path.exists(tmp_path):
            os.remove(tmp_path)




# 6C. JOB PREDICTION ENDPOINT
@app.post(path = '/cv-job-prediction', response_model = jobPrediction)
async def job_prediction_endpoint(file : UploadFile = File(...)):

    # GET UPLOADED FILE EXTENSION
    extension = os.path.splitext(file.filename)[1].lower()

    # IF USER UPLOADED NOT PDF
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code = 400, detail = f"{extension} File is not Supported Anymore!")
    
    # CREATE TEMPORARY FIL TO SAVE UPLOADED PDF
    with tempfile.NamedTemporaryFile(delete = False, suffix = extension) as tmp:
        
        # READ UPLOADED FILE
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name
    

    try:
        # -------------RUN MAIN FUNCTION -----------
        results = job_prediction(tmp_path)

        # DISPLAY MOST HIGH PROBABILITY JOBS
        results.jobs = sorted(results.jobs, key = lambda x: x.probability, reverse = True)
        return results
        

    finally:

        # DELETE TEMPORARY FILE AFTER COMPLETION (TO RELEASE MEMORY)
        if os.path.exists(path = tmp_path):
            os.remove(tmp_path)


# 6D. SALARY ESTIMATION ENDPOINT
@app.post(path='/salary-estimation', response_model = SalaryEstimation)
async def salary_estimation_endpoint(file: UploadFile = File(...)):

    # GET UPLOADED FILE EXTENSION
    extension = os.path.splitext(file.filename)[1].lower()

    # IF USER UPLOADED NOT SUPPORTED EXTENSION
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code = 400, detail = f"{extension} File is not Supported Anymore!")
    
    # CREATE TEMPORARY FILE TO SAVE UPLOADED FILE
    with tempfile.NamedTemporaryFile(delete = False, suffix = extension) as tmp:
        
        # READ UPLOADED FILE
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        # ------ RUN MAIN FUNCTION ---------
        results = salary_estimation(tmp_path)
        return results
        
    finally:
        # DELETE TEMPORARY FILE AFTER COMPLETION (TO RELEASE MEMORY)
        if os.path.exists(path = tmp_path):
            os.remove(tmp_path)


# 6E. PORTFOLIO PROJECT RECOMMENDER ENDPOINT
@app.post(path='/recommend-portfolio', response_model = ProjectRecommendationList)
async def recommend_portfolio_endpoint(request: ProjectRequest):
    """
    THIS ENDPOINT CURRENTLY DOESNT ACCEPT A FILE.
    """
    try:
        # ------ RUN MAIN FUNCTION ---------
        results = recommend_portfolio(target_role = request.target_role, missing_skills = request.missing_skills)
        return results
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))