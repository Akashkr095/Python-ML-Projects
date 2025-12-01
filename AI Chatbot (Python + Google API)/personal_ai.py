import google.generativeai as genai
import os


# import API

GOOGLE_API_KEY = "GOOGLE_API_KEY"  ## Replace with your actual API key

# Configure the genai libery with my api
genai.configure(api_key=GOOGLE_API_KEY)


# List of avliable model for my google api

print("-------List of avliable model for my google api-------")

model_name_with_generate_content = []
try:
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(f"- {m.name} (Supports generateContent)\n")
            model_name_with_generate_content.append(m.name)
        else:
            print(f"- {m.name} (Does NOT support generateContent for direct use)\n")

except Exception as e:
    print(f"Error listing models: {e}")

print("-----------------------------------------------------------------------------------------------------------\n")

## model choice
model_name_to_use = 'models/gemini-pro-latest'

if model_name_to_use not in model_name_with_generate_content:
    print(f"ERROR: The chosen model '{model_name_to_use}' was not found in the list of available models supporting generateContent.")
else:
    print(f"The chosen model '{model_name_to_use}' is valid and supports generateContent.\n")


# Initialize the Gemini model for text generation
model = genai.GenerativeModel(model_name_to_use)
print(f"Successfully initialized model: {model_name_to_use}\n")

# Global variables for maintaining chat history

messages = []
chat_session = None

def chat_with_gemini(user_input):

    global messages
    global chat_session

    if chat_session is None:
        chat_session = model.start_chat(history=[])
        print("Python_Gemini: Started new chat session.")

    # Append user message to chat history
    messages.append(
        {
            "role" : "user",
            "content" : user_input
        }
    )

    # Send user input to Gemini model and get response
    python_gemini_response = ""
    response = chat_session.send_message(user_input)

    if response.text:
        python_gemini_response = response.text
    else:
        python_gemini_response = "I'm sorry, I received an empty response from the AI."


    # Append Gemini's response to chat history
    messages.append(
        {
            "role" : "Python_gemini",
            "content" : python_gemini_response
        }
    )

    print(f"python_Gemini: {python_gemini_response}")


## main function

if __name__ == "__main__":
    print(f"Python_Gemini: Hi! I am PyTHON_GEM, powered by Google Gemini. How may I help you today?\n")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
            print("Jarvis: Goodbye! It was a pleasure assisting you.")

            # SAVE file
            from datetime import datetime

            with open("chat_history.txt", "w", encoding="utf-8") as f:
                for msg in messages:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"{timestamp} - {msg['role'].upper()}: {msg['content']}\n")

            break
        
        chat_with_gemini(user_input)
            



    
