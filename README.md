LLM‑Assisted PRA COREP Reporting Assistant (Prototype)
Overview
This project is a prototype AI-assisted regulatory reporting tool designed to simulate how Large Language Models (LLMs) can support UK banks preparing COREP submissions.

The system accepts capital data and generates structured COREP-style outputs, applies validation checks, produces an audit trail, and exports a reporting template.

It demonstrates an end‑to‑end pipeline:

User input → COREP engine → Validation → Audit → Template → Excel export

This aligns with the assignment objective of simulating automated regulatory reporting.

Features
COREP capital calculations
Validation checks for regulatory consistency
Audit trail explaining rule usage
Template rendering (human-readable output)
Excel report export
Simple Streamlit UI
Modular backend architecture
System Flow
User enters capital values (CET1, Tier1, Tier2, RWA)
Backend computes COREP metrics
Validation engine checks data consistency
Audit trail records applied rules
COREP template is generated
Excel report is exported
This simulates an AI-assisted regulatory workflow.

Project Structure
corep-assistant/
│
├── app.py                  # FastAPI backend entry point
├── README.md
├── requirements.txt
│
├── core/                   # Core logic modules
│   ├── schemas.py          # Data models
│   ├── validator.py        # Validation rules
│   ├── template_renderer.py# COREP template builder
│   ├── llm_engine.py       # Simulated AI engine
│   ├── retrieval.py        # Regulatory text retrieval
│
├── data/
│   └── rules.txt           # Regulatory rule dataset
│
├── ui/
│   └── ui.py               # Streamlit frontend
│
└── output/
    └── corep_report.xlsx   # Generated reports
Installation
1. Install Python
Requires Python 3.10+

Check version:

python --version
2. Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
Running the Backend API
Start FastAPI server:

python -m uvicorn app:app --reload
Open browser:

http://127.0.0.1:8000/docs
You can test API requests directly from this interface.

Running the UI
python -m streamlit run ui/ui.py
This launches a simple browser interface.

Example Input
CET1: 120
Tier1: 150
Tier2: 50
RWA: 900
The system generates:

COREP-style output
Validation messages
Audit trail
Excel report
Troubleshooting
If uvicorn not found:

pip install uvicorn
If Streamlit not found:

pip install streamlit
If file path errors occur, verify that:

rules.txt is inside the data/ folder
ui.py is inside the ui/ folder
Purpose of Prototype
This system demonstrates how LLM-assisted tooling could:

Reduce manual regulatory reporting effort
Improve consistency and traceability
Link outputs to rule-based audit logic
Provide explainable reporting pipelines
It is a simulation for educational purposes.

Author
Assignment prototype project.
