from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()




client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_bot_response(user_input):
    """
    Get response from Groq API
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chat():
    """
    Main chat loop
    """
    print("Bot: Hello! I'm a chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye!")
            break
            
        response = get_bot_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chat()