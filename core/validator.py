def validate(data, scenario):

    errors = []

    expected_total = scenario["tier1"] + scenario["tier2"]

    if abs(data["Total_Own_Funds"] - expected_total) > 0.01:
        errors.append("Total Own Funds calculation mismatch")

    if data["Tier1"] < data["CET1"]:
        errors.append("Tier1 cannot be less than CET1")

    return errors
