#Reporting Assistant Prototype
#Version: 1.0
#Author: [Anshul Sahai]
from fastapi import FastAPI
from pydantic import BaseModel
from openpyxl import Workbook

# Safely read rules.txt at startup
with open("data/rules.txt") as f:

    rules = f.read()

app = FastAPI()

class Scenario(BaseModel):
    cet1: float
    tier1: float
    tier2: float
    rwa: float

def calculate_corep(data: Scenario):
    total_own_funds = data.tier1 + data.tier2
    capital_ratio = total_own_funds / data.rwa if data.rwa != 0 else 0

    audit = {
        "rules_used": rules,
        "CET1": "Reported from scenario input",
        "Tier1": "Reported from scenario input",
        "Total_Own_Funds": "Tier1 + Tier2",
        "Capital_Ratio": "Total Own Funds / RWA"
    }

    return {
        "CET1": data.cet1,
        "Tier1": data.tier1,
        "Total_Own_Funds": total_own_funds,
        "Capital_Ratio": round(capital_ratio, 3),
        "audit": audit
    }

def render_template(result, errors):
    template = f"""
COREP TEMPLATE EXTRACT
CET1 Capital: {result['CET1']}
Tier 1 Capital: {result['Tier1']}
Total Own Funds: {result['Total_Own_Funds']}
Capital Ratio: {result['Capital_Ratio']}
Validation: {errors if errors else "No errors"}
Audit Trail: {result['audit']}
"""
    return template

def validate(data):
    errors = []
    if data["Tier1"] < data["CET1"]:
        errors.append("Tier1 cannot be less than CET1")
    if data["Capital_Ratio"] < 0.08:
        errors.append("Capital ratio below regulatory threshold")
    return errors

def export_excel(result):
    wb = Workbook()
    ws = wb.active
    ws.title = "COREP"
    ws.append(["Field", "Value"])
    ws.append(["CET1", result["CET1"]])
    ws.append(["Tier1", result["Tier1"]])
    ws.append(["Total Own Funds", result["Total_Own_Funds"]])
    ws.append(["Capital Ratio", result["Capital_Ratio"]])
    wb.save("corep_report.xlsx")

@app.get("/")
def home():
    return {"message": "COREP assistant running"}

@app.post("/scenario")
def submit_scenario(data: Scenario):
    result = calculate_corep(data)
    errors = validate(result)
    template = render_template(result, errors)
    # Call the export_excel function to save the Excel file
    export_excel(result)
    return {
        "corep_output": result,
        "validation_errors": errors,
        "template": template,
        "excel_file": "corep_report.xlsx created"
    }
