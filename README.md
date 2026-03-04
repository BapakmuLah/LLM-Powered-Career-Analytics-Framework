# 🧑‍💼 KarirMind  - Large Language Model–Powered Career Analytics Framework  

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## 🏦 Build. Fix. Price. Land. — The Complete AI Career Acceleration System 🪜

KarirMind is a Large Language Model (LLM)–based ecosystem designed to help candidates understand, refine, and strategically elevate their career positioning.

---

## 📺 Live Demo

**🔗 Frontend Demo (UI) : [Live Demo on Vercel](https://karirmind.vercel.app/main.html)** <br>
**🔗 Backend Demo (API) : [Live Demo on Hugging Face Spaces](https://sandking-llm-career-analytics-framework.hf.space/docs)**

## 🚀 Overview

This project is a modular AI career analytics platform consisting of four integrated systems:

1. **Job Role Recommender**
2. **Resume Audit Engine**
3. **Salary Estimation Engine**
4. **Portfolio Project Architect**

Each module processes resume data and produces structured, consistent outputs using Pydantic schemas.

---

## 🧠 System Architecture

The ecosystem follows a structured LLM pipeline:

- Resume Upload (PDF / TXT / DOCX / Image formats)
- Content Extraction
- Prompt Injection with Role-Specific Instructions
- Gemini LLM Inference
- Structured Output Parsing (Pydantic)
- JSON Response for downstream processing

The system is designed for modular expansion and integration into larger platforms.

---


## 💼 Business Model

KarirMind is designed as an AI-powered Career Intelligence SaaS with multiple monetization streams:

### 1️⃣ Tiered Subscription Model
- Free Tier → Basic resume analysis
- Pro Tier → Full ecosystem access (salary insights, portfolio review, advanced critique)
- Premium Tier → Unlimited analysis + advanced negotiation strategies 💰

### B2B Model
- Integration with bootcamps & edtech platforms
- White-label solutions for career coaching providers
- API-based integration for HR Tech startups

----


## 📌 Modules

### 1️⃣ **Job Role Recommender**
Analyzes resume content and recommends the most suitable job roles based on skills, experience, and impact.

**Output Includes:**
- Recommended roles
- Reasoning behind role matching

---

### 2️⃣ **Resume Audit Engine**
Performs a detailed section-by-section and bullet-by-bullet evaluation of the resume.

**Output Includes:**
- Identified weaknesses
- Severity classification (HIGH / MEDIUM / LOW)
- Actionable improvement suggestions
- Structured response format

---

### 3️⃣ **Salary Estimation Engine**
Estimates annual salary range (USD) based on global remote / US tech market standards.

**Output Includes:**
- Detected seniority level
- Estimated salary range
- Justification based on skills and experience
- 3–5 personalized salary negotiation strategies

---

### 4️⃣ **Portfolio Project Architect**
Generates enterprise-level portfolio project recommendations based on target role and identified skill gaps.

**Output Includes:**
- Professional project name
- Business problem description
- Detailed tech stack
- Step-by-step development roadmap
- Resume-ready PRAQ-style bullet point

---

## 🛠 Tech Stack

- Python
- Gemini LLM 
- LangChain
- Pydantic
- FastAPI (API Layer)
- Hugging Face Spaces

---

## 🎯 Key Design Principles

- Structured LLM outputs for reliability
- Role-based prompt engineering
- Modular architecture for scalability
- Business-impact-driven evaluation logic
- Resume-to-decision transformation pipeline

---

## 📊 Use Cases

- Career path planning
- Resume optimization
- Salary benchmarking
- Portfolio strategy development
- AI-driven career advisory systems

---

## 🔌 API Endpoints

| Method | Endpoint                | Description                                      | Response Model                     |
|--------|-------------------------|--------------------------------------------------|-------------------------------------|
| GET    | `/`                     | Health check / API status                        | Status message                      |
| POST   | `/critique-resume`      | Perform structured resume audit & critique       | `ResumeCritique`                    |
| POST   | `/cv-job-prediction`    | Recommend suitable job roles from resume         | `jobPrediction`                     |
| POST   | `/salary-estimation`    | Estimate seniority & salary range (USD)          | `SalaryEstimation`                  |
| POST   | `/recommend-portfolio`  | Generate strategic portfolio project plans       | `ProjectRecommendationList`         |

----


## 🔮 Future Roadmap — KarirMind Ecosystem Expansion

### 1️⃣ AI Interview Simulation Engine
- Role-based technical and behavioral interview simulations with adaptive questioning.  
- Real-time feedback and personalized performance improvement reports.  

### 2️⃣ Skill Gap Intelligence Dashboard
- Visual skill gap analysis mapped to target roles and market demand.  
- Personalized upskilling roadmap with certification recommendations.  

### 3️⃣ Company-Specific Resume Optimizer
- Resume alignment and ATS keyword scoring based on specific job descriptions.  
- Company-tailored rewriting suggestions with match percentage insights.  

### 4️⃣ Career Risk & Stability Analyzer
- Industry volatility and career transition risk assessment.  
- Data-driven pivot recommendations for long-term career stability.  

### 5️⃣ Career Performance Tracking System
- Resume version tracking and career progression timeline.  
- Salary growth monitoring and promotion readiness scoring.  


---


## 💰 Future Business Model 

### 1️⃣ Modular Subscription Model
- Users subscribe to individual modules based on career needs.  
- Tiered pricing with premium analytics and automation features.  

### 2️⃣ B2B Enterprise Licensing
- White-label and API solutions for bootcamps and HR Tech platforms.  
- Internal career mobility analytics tools for enterprises.  

### 3️⃣ Proprietary Career Intelligence Score
- Exclusive hireability and growth potential scoring system.  
- Premium feature differentiating KarirMind from competitors.  

### 4️⃣ Premium AI Career Coach Tier
- Adaptive AI mentor with monthly strategy planning.  
- Advanced negotiation scripts and promotion blueprints.  

### 5️⃣ Career Marketplace Integration
- Connect users with recruiters and career mentors.  
- Platform-based ecosystem monetization model.  


## 🎯 Positioning

KarirMind is not just a resume analyzer.

KarirMind is a Career Intelligence Framework that empowers candidates to:

- Build the right skills.
- Correct positioning mistakes.
- Price themselves accurately in the job market.
- Land the right role — not just any role. 🚀

## 📄 License

This project is intended for educational, research, and portfolio purposes.

---
