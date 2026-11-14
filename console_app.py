from scoring import calculate_score
from analysis import analyze_conversation,get_conversation_stats,detect_objections
from ai_engine import generate_coaching_report
# AI SALES COACH
# Version 1.0 - Text Analysis

print("=" * 50)
print("          AI SALES COACH")
print("     Sales Conversation Analyser")
print("=" * 50)

# Collect conversation


conversation = []

print("\nEnter the conversation.")
print("Format: Salesperson: message")
print("        Customer: message")
print("Type END when finished.\n")

while True:

    line = input()

    if line.upper() == "END":
        break

    if line.startswith("Salesperson:") or line.startswith("Customer:"):

        speaker, message = line.split(":", 1)

        conversation.append((speaker.strip(), message.strip()))

    else:
        print("Invalid format! Include the speaker name.")
if len(conversation)==0:
    print("\nno conversation entered")

else:
    stats = get_conversation_stats(conversation)

    print("\n" + "=" * 50)
    print("          CONVERSATION STATISTICS")
    print("=" * 50)

    print("Total messages:", stats[0])
    print("Salesperson messages:", stats[1])
    print("Customer messages:", stats[2])

    print("Salesperson participation:", round(stats[3], 2), "%")
    print("Customer participation:", round(stats[4], 2), "%")

    objections = detect_objections(conversation)

    print("\n" + "=" * 50)
    print("          CUSTOMER OBJECTIONS")
    print("=" * 50)

    if len(objections) > 0:

        for category, keyword, message in objections:

            print("\nCategory:", category)
            print("Detected phrase:", keyword)
            print("Customer message:", message)

    else:
        print("No objections detected.")
    print("\n" + "=" * 50)
    print("             ANALYSIS REPORT")
    print("=" * 50)
    total_score = 0

    results = analyze_conversation(conversation)
    report = generate_coaching_report(objections, results)

    for category, matched, score in results:

        total_score = total_score + score

        print("\nCategory:", category)
        print("Score:", score, "/ 5")

        if len(matched) > 0:
            print("Positive indicators:", matched)
        else:
            print("No positive indicators detected.")

    # Calculate overall score

    percentage = (total_score / 20) * 100

    print("\n" + "=" * 50)
    print("OVERALL PERFORMANCE:", round(percentage, 2), "%")
    print("=" * 50)

    print("\n" + "=" * 50)
    print("          AI COACHING REPORT")
    print("=" * 50)

    print("\nSTRENGTHS:")
    for item in report["strengths"]:
        print("-", item)

    print("\nWEAKNESSES:")
    for item in report["weaknesses"]:
        print("-", item)

    print("\nRECOMMENDATIONS:")
    for item in report["recommendations"]:
        print("-", item)


