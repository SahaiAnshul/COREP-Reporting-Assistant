def render_template(output):

    template = f"""
COREP TEMPLATE EXTRACT

CET1 Capital: {output['CET1']}
Tier 1 Capital: {output['Tier1']}
Total Own Funds: {output['Total_Own_Funds']}
Capital Ratio: {output['Capital_Ratio']}

Audit Trail:
{output['audit']}
"""

    return template
