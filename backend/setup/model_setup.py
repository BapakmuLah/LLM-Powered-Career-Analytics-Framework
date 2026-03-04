import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. SETUP ENVIRONMENT & GEMINI MODEL
load_dotenv()
if not os.getenv('GEMINI_API_KEY'):
    raise RuntimeError("GEMINI_API_KEY not Found")

llm = ChatGoogleGenerativeAI(model='models/gemma-3-27b-it', temperature=0.1)