
from scoring import calculate_score

categories = {

    "Customer Discovery": [
        "what challenges",
        "what are your needs",
        "could you tell me",
        "what are you looking for",
        "how can i help you",
        "what problems",
        "tell me about your business"
    ],

    "Communication": [
        "thank you",
        "please",
        "certainly",
        "i understand",
        "happy to help",
        "of course",
        "you're welcome"
    ],

    "Objection Handling": [
        "understand your concern",
        "fair point",
        "let me explain",
        "we can address",
        "we can discuss pricing",
        "i understand your concern",
        "let me clarify"
    ],

    "Follow-up and Closing": [
        "next meeting",
        "follow up",
        "schedule a call",
        "shall we proceed",
        "when can we meet",
        "move forward",
        "next steps"
    ]
}



def analyze_conversation(conversation):

    results = []

    # Combine only salesperson messages

    sales_text = ""

    for speaker, message in conversation:

        if speaker == "Salesperson":
            sales_text = sales_text + " " + message.lower()

    for category, keywords in categories.items():

        matched = []

        for word in keywords:

            if word in sales_text:
                matched.append(word)

        total_keywords = len(keywords)

        score = calculate_score(matched, total_keywords)

        results.append((category, matched, score))

    return results

def get_conversation_stats(conversation):

    total_messages = len(conversation)

    salesperson_messages = 0
    customer_messages = 0

    for speaker, message in conversation:

        if speaker == "Salesperson":
            salesperson_messages += 1

        elif speaker == "Customer":
            customer_messages += 1

    salesperson_percentage = (salesperson_messages / total_messages) * 100
    customer_percentage = (customer_messages / total_messages) * 100

    return total_messages, salesperson_messages, customer_messages, salesperson_percentage, customer_percentage


objection_categories = {

    "Price": [
        "too expensive",
        "too costly",
        "outside our budget",
        "can't afford"
    ],

    "Timing": [
        "not the right time",
        "maybe next year",
        "not ready yet",
        "need more time"
    ],

    "Trust": [
        "not sure if it will work",
        "don't trust",
        "not convinced",
        "no guarantee"
    ],

    "Need": [
        "don't need this",
        "already have a solution",
        "not interested",
        "not necessary"
    ],

    "Authority": [
        "need to ask my manager",
        "need approval",
        "discuss with my team",
        "not my decision"
    ]
}
def detect_objections(conversation):

    objections = []

    for speaker, message in conversation:

        if speaker == "Customer":

            message = message.lower()

            for category, keywords in objection_categories.items():

                for word in keywords:

                    if word in message:

                        objections.append((category, word, message))

    return objections
