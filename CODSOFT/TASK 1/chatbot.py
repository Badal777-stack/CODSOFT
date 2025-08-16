
import re

def simple_chatbot():
    print("Bot: Hello! I'm a simple rule-based chatbot. How can I help you today? \n     how are you today?")
    
    while True:
        user_input = input("\nYou: ").strip().lower()
    
        if not user_input:
            print("Bot: Please type something so we can chat!")
            continue
        
        # Exit conditions
        if re.search(r'\b(exit|quit|bye|go to hell|goodbye)\b', user_input):
            print("Bot: Goodbye! Feel free to chat again anytime.     \n Thank you .")
            break
        
        # hello pattern
        elif re.search(r'\b(hello|hi|hey|greetings|hola)\b', user_input):
            print("Bot: Hello there! How can I assist you today?")
        
        # Intro pattern
        elif re.search(r'\b(name|who are you|what are you)\b', user_input):
            print("Bot: I'm ChatBot v1.0. Just a simple rule-based assistant!\n     Is there anything that i can help you with? You're free to ask!")
        
        # How are you pattern
        elif re.search(r'\b(how are you|hows it going|how do you do)\b', user_input):
            print("Bot: I'm just a program, but I'm functioning perfectly! How about you?")
        
        # Weather forcast pattern
        elif re.search(r'\b(weather|forecast|outside|temperature)\b', user_input):
            print("Bot: I don't have real-time weather data. You might want to check a weather service! try checking on your device")
        
        # Time/date pattern
        elif re.search(r'\b(time|date|day|today)\b', user_input):
            print("Bot: I don't have clock access. Try checking your device's clock!")
        
        # Thank you pattern
        elif re.search(r'\b(thanks|thank you|appreciate it|thx)\b', user_input):
            print("Bot: You're welcome! Is there anything else I can help with?")

        #founded
        elif re.search(r'\b(who made you| who is your founder|your owner|when you were made)\b', user_input):
            print("Bot:Im a simple chatbot v1.0. And i was founded by MR.BADAL NAHAL in 2025 ")

        #about owner
        elif re.search(r'\b(so he made you| he was your founder)\b', user_input):
            print("Bot:Yes he made me . And Im gratefull that he made me  ")
        
        # Help 
        elif re.search(r'\b(help|what can you do|help me |support)\b', user_input):
            print("Bot: I can respond to greetings, tell you about myself, ")
            print("answer about weather/time (though I don't have real data), ")
            print("and have simple conversations. Try asking about my name or saying hello!")
        
        # Default response if no match was found
        else:
            print("Bot: I'm still learning! Could you try rephrasing that?")
            print("(Type 'help' to see what I can do or 'bye' to exit)")

# Starting the chatbot
if __name__ == "__main__":
    simple_chatbot()