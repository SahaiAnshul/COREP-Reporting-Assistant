System Flow
The prototype simulates an AI assistant that helps prepare COREP regulatory reports.

Flow:

User input → API → COREP engine → Validation → Template → Excel export
Step-by-step:

User enters capital data (CET1, Tier1, Tier2, RWA)

Backend calculates COREP values

Validation checks regulatory consistency

System generates audit trail

COREP template is rendered

Excel report is exported

This demonstrates automated regulatory reporting logic.

2. Clean Project Structure
Reorganize your folder like this:

corep-assistant/
│
├── app.py
├── README.md
├── requirements.txt
│
├── core/
│   ├── schemas.py
│   ├── validator.py
│   ├── template_renderer.py
│   ├── llm_engine.py
│   ├── retrieval.py
│
├── data/
│   └── rules.txt
│
├── ui/
│   └── ui.py
│
└── output/
    └── corep_report.xlsx
--------------------------------------------------------------------------------------------------
# LLM-Assisted PRA COREP Reporting Assistant

## Overview
This prototype demonstrates an AI-assisted regulatory reporting tool for COREP submissions.

It converts financial scenarios into structured COREP outputs with validation and audit trail.

## Features
- COREP capital calculations
- Regulatory validation
- Audit trail generation
- Template rendering
- Excel export
- Simple UI

## How to run

Install dependencies:

pip install -r requirements.txt

Run API:

python -m uvicorn app:app --reload

Open:

http://127.0.0.1:8000/docs

Run UI (optional):

streamlit run ui/ui.py

## Project Structure
core/ → logic modules  
data/ → regulatory rules  
ui/ → frontend  
output/ → generated reports
