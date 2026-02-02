import re

def chatbot(user_input):
    # Basic NLP preprocessing
    user_input = user_input.lower()

    # 1. Greeting intent
    if re.search(r"\b(hi|hello)\s*(sir|mam)?\b", user_input):
        return "Hello! How can I help you?"

    # 2. MHT-CET Guidance intent
    elif re.search(r"\b(exam strategy|study timetable|mock test|study material)\b", user_input):
        return "I can guide you for MHT-CET exam strategy, study timetable, mock test and recommended study material. Ask me specifically what you need."

    # 3.Student Queries intent
    elif re.search(r"\b(study tips|motivation|time management|stress|concentration)\b", user_input):
        return "Don’t worry, many students feel the same. Plan your time well, study consistently, and take short breaks to stay motivated."

    # 4. Encouragement intent
    elif re.search(r"\b(all the best|good luck|nervous|thank you|thanks)\b", user_input):
        return "All the best for your exam! Stay calm, manage your time well, and trust your preparation."
    
    # 5. Goodbye intent
    elif re.search(r"\b(bye|exit|quit)\b", user_input):
        return "Goodbye! Best wishes for your future!"


    # 6. Fallback response
    else:
        return "Sorry, I didn't understand that. Please try again."

# Main chat loop
print("Chatbot: Hi! I am a rule-based chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = chatbot(user)
    print("Chatbot:", response)

    if re.search(r"\b(bye|exit|quit)\b", user.lower()):
        break
