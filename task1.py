import re

def simple_chatbot(user_input):
    user_input = user_input.lower()
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I help you today?"
    elif re.search(r'\b(who are you|what are you)\b', user_input):
        return "I'm a simple chatbot created to demonstrate basic natural language processing."
    elif re.search(r'\b(how are you|how are you doing)\b', user_input):
        return "I'm functioning well, thank you for asking! How about you?"
    elif re.search(r'\b(help|support)\b', user_input):
        return "I can help with basic questions. What do you need assistance with?"
    elif re.search(r'\b(thank you|thanks)\b', user_input):
        return "You're welcome! Is there anything else I can help you with?"
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase or ask something else?"

# Main loop to run the chatbot
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)