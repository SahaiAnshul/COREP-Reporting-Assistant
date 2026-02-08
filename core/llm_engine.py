from openai import OpenAI
import json

client = OpenAI()

def generate_corep_output(scenario, retrieved_rules):

    prompt = f"""
You are a COREP regulatory assistant.

Scenario:
{scenario}

Rules:
{retrieved_rules}

Return JSON in this format:

{{
  "CET1": value,
  "Tier1": value,
  "Total_Own_Funds": value,
  "Capital_Ratio": value,
  "audit": {{
      "CET1": rule used,
      "Tier1": rule used,
      "Total_Own_Funds": rule used,
      "Capital_Ratio": rule used
  }}
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return json.loads(response.choices[0].message.content)
