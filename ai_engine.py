def generate_coaching_report(objections, results):

    report = {
        "strengths": [],
        "weaknesses": [],
        "recommendations": []
    }

    # Identify strengths
    for category, matched, score in results:

        if score > 0:
            report["strengths"].append(
                category + ": Positive indicators detected."
            )

    # Identify weaknesses
    for category, matched, score in results:

        if score == 0:
            report["weaknesses"].append(
                category + ": No positive indicators detected."
            )

    # Generate recommendations based on objections
    for category, keyword, message in objections:

        if category == "Price":
            report["recommendations"].append(
                "Explain the value of the product and "
                "relate it to the customer's budget."
            )

        elif category == "Timing":
            report["recommendations"].append(
                "Understand the customer's timeline "
                "and discuss a suitable follow-up."
            )

        elif category == "Trust":
            report["recommendations"].append(
                "Provide relevant evidence and "
                "explain how the product works."
            )

        elif category == "Need":
            report["recommendations"].append(
                "Explore the customer's requirements "
                "and explain relevant benefits."
            )

        elif category == "Authority":
            report["recommendations"].append(
                "Offer to provide information "
                "that the customer can share with their decision-maker."
            )

    return report


