🚀 Python Gemini Chatbot

A simple Python-based chatbot using Google Gemini API.
This project allows continuous chat sessions, model selection, and automatic saving of chat history.

📌 Features

🌐 Uses Google Gemini (Generative AI) API

🤖 Creates a chat session with memory

📜 Saves entire chat history to chat_history.txt

🔍 Automatically lists all available models

🧠 Allows selection of models that support generateContent

🔄 Loop-based user interaction

🛑 Exit system with safe chat saving

    📁 Project Structure
    ├── personal_ai.py               # Your main chatbot script
    ├── chat_history.txt      # Auto-created on exit
    └── README.md             # Project documentation



2️⃣ Install Dependencie

    pip install google-generativeai

3️⃣ Add Your API Key

Replace the placeholder key inside the script:

    GOOGLE_API_KEY = "YOUR_API_KEY_HERE"


▶️ Run the Chatbot
python personal_ai.py

🧠 How It Works

When the script starts, it lists all available Gemini models.

Checks if your selected model supports chat responses.

A chat session is created using:

    chat_session = model.start_chat(history=[])


All chats are stored in a global list.

When you exit (exit, quit, bye), chat history is saved to a file.

📄 Chat History Output

A file like this will be generated:

    2025-12-01 12:30:00 - USER: Hello

    2025-12-01 12:30:01 - PYTHON_GEMINI: Hi! How can I help?


📌 Future Improvements

Add a GUI 

Integrate voice input/output

Store chat history in a database

