# 🤖 Kai — AI Chatbot

> A modern AI chatbot built with **Python, Streamlit, LangChain, Groq, and OpenAI APIs**.

Kai is a simple and interactive AI chatbot that allows users to communicate with different Large Language Models (LLMs) through a clean Streamlit interface.

The project is designed for students, developers, and beginners who want to understand how an AI chatbot can be built using Python and modern LLM APIs.

---

## 📌 About Kai

**Kai** is a personal AI chatbot application that provides a conversational interface for interacting with AI models.

The application uses **Streamlit** for the user interface and **LangChain** to connect the application with different AI model providers.

Kai supports AI models through providers such as:

* 🟢 Groq
* 🔵 OpenAI

Users can select the available provider/model from the application and start chatting with the AI.

### What Kai Can Do

* 💬 Interactive AI conversations
* ⚡ Streaming AI responses
* 🔄 Multiple AI model/provider support
* 🧠 Conversation history
* 🎨 Simple Streamlit interface
* 🔐 Environment-based API key configuration
* 🐍 Python-based implementation
* 🔗 LangChain integration

---

# ✨ Features

| Feature            | Description                                       |
| ------------------ | ------------------------------------------------- |
| 💬 AI Chat         | Chat with an AI model                             |
| ⚡ Streaming        | Responses appear progressively                    |
| 🔄 Model Selection | Select different supported models                 |
| 🧠 Chat History    | Maintains conversation during the session         |
| 🔐 Secure API Keys | API keys are loaded through environment variables |
| 🎨 Streamlit UI    | Simple and interactive web interface              |
| 🔗 LangChain       | Easy integration with LLM providers               |

---

# 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Groq API**
* **OpenAI API**
* **python-dotenv**

---

# 📂 Project Structure

```text
Kai/
│
├── chatbot.py
├── README.md
├── pyproject.toml
├── requirements.txt
├── .env
├── .gitignore
│
└── .venv/


# 🔑 API Key Setup

To use Kai, you need an API key from the AI provider you want to use.

You can use:

* Groq
* OpenAI

---

## 🟢 Option 1 — Groq API Key

Create a Groq API key from the Groq developer platform.

After obtaining your key, create a file named:

```text
.env
```

in the root directory of the project.

Add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx


## 🔵 Option 2 — OpenAI API Key

Create an OpenAI API key.

Inside your `.env` file add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Example:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

# 🔐 Using Multiple API Keys

If the chatbot supports both providers, you can configure both keys in the same `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

Kai can then use the provider selected by the application.

---

# 💻 How to Add the API Key in Any Code Editor

You can use any code editor such as:

* Visual Studio Code
* PyCharm
* Sublime Text
* Notepad++
* Cursor
* Any other editor

The process is almost the same.

### Step 1 — Open the Project

Open the Kai project folder in your code editor.

Example:

```text
Kai/
```

### Step 2 — Create `.env`

Inside the project folder create:

```text
.env
```

### Step 3 — Add Your API Key

For Groq:

```env
GROQ_API_KEY=your_api_key_here
```

For OpenAI:

```env
OPENAI_API_KEY=your_api_key_here
```

### Step 4 — Save the File

Save the `.env` file.


# 🐍 How API Keys Work in Python

The project uses environment variables instead of directly writing the API key inside Python code.

The application can load variables from `.env` using:

```python
from dotenv import load_dotenv
import os

load_dotenv()
```

Then the API key can be accessed using:

```python
api_key = os.getenv("GROQ_API_KEY")
```

For OpenAI:

```python
api_key = os.getenv("OPENAI_API_KEY")
```

### Why use `.env`?

Instead of doing this:

```python
api_key = "gsk_xxxxxxxxxxxxxxxxx"
```

use:

```python
api_key = os.getenv("GROQ_API_KEY")
```

This keeps your secret outside your source code.


# 🚀 Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project:

```bash
cd Kai
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

# 📦 Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If your project uses `pyproject.toml`, you can install the project dependencies according to that configuration.

---

# ▶️ How to Run Kai

After installing the dependencies and configuring your API key, run:

```bash
streamlit run chatbot.py
```

You should see something similar to:

```text
Local URL: http://localhost:8501
```

Open the URL in your browser:

```text
http://localhost:8501
```

Your Kai chatbot should now be running.

---

# 🖥️ Running in VS Code

Open the project folder in VS Code.

Open the terminal:

```text
Terminal → New Terminal
```

Create the virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
GROQ_API_KEY=your_api_key_here
```

Finally run:

```bash
streamlit run chatbot.py
```

---

# 🧪 Example `.env`

Your `.env` file should look like:

```env
GROQ_API_KEY=gsk_your_key_here
OPENAI_API_KEY=sk_your_key_here
```

Replace the values with your actual API keys.

---

# 🔧 Troubleshooting

## ❌ `ModuleNotFoundError`

Example:

```text
ModuleNotFoundError: No module named 'streamlit'
```

Install the missing package:

```bash
pip install streamlit
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

---

## ❌ API Key Not Found

If you get an error related to the API key, check:

1. `.env` exists.
2. The variable name is correct.
3. There are no unnecessary quotes or spaces.
4. The `.env` file is in the project root.
5. You restarted the Streamlit application after changing the key.

Example:

```env
GROQ_API_KEY=gsk_xxxxxxxxx
```

---

## ❌ Streamlit Command Not Found

Try:

```bash
python -m streamlit run chatbot.py
```

This is especially useful when Streamlit is installed inside a virtual environment.

---

# 🔒 Security Best Practices

Follow these rules when working with API keys:

### ✅ DO

* Store API keys in `.env`
* Add `.env` to `.gitignore`
* Use environment variables
* Use different keys for development and production
* Rotate keys if they are accidentally exposed


# 🧠 How Kai Works

The basic architecture looks like this:

```text
             User
               │
               ▼
       ┌─────────────────┐
       │  Streamlit UI   │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │   Kai Chatbot   │
       └────────┬────────┘
                │
                ▼
          ┌───────────┐
          │ LangChain │
          └─────┬─────┘
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
   ┌─────────┐      ┌─────────┐
   │  Groq   │      │ OpenAI  │
   │   API   │      │   API   │
   └────┬────┘      └────┬────┘
        │                │
        └───────┬────────┘
                ▼
          AI Model Response
                │
                ▼
             User
```

---

# 🔄 Application Flow

```text
User enters message
        ↓
Streamlit receives message
        ↓
Chat history is updated
        ↓
Selected AI provider is identified
        ↓
API request is sent
        ↓
AI model processes the request
        ↓
Response is streamed
        ↓
Response displayed in Streamlit
```

---

# 🎯 Learning Objectives

This project can help you understand:

* Python application development
* Streamlit
* REST/API-based applications
* LLM integration
* LangChain
* Environment variables
* API authentication
* Git and GitHub
* Virtual environments
* Basic AI application architecture

---

# 🔮 Future Improvements

Possible improvements for Kai:

* 🌐 Web search integration
* 📄 PDF/document chatting
* 🧠 Long-term memory
* 🎤 Voice input
* 🔊 Text-to-speech
* 🖼️ Image understanding
* 🔐 User authentication
* 💾 Persistent conversation database
* 📱 Mobile-friendly interface
* ☁️ Cloud deployment

---

# ⚖️ Disclaimer

Kai is an educational AI chatbot project.

Users are responsible for keeping their API credentials secure and following the terms and usage policies of the respective AI service providers.

Do not use the application to perform illegal, harmful, or unauthorized activities.

---

# 👨‍💻 Author

**Ankit**

BCA — Cybersecurity & Forensics

Interested in:

* 🔐 Cybersecurity
* 🕵️ Digital Forensics
* 🤖 Artificial Intelligence
* 🐍 Python
* 🌐 Web Security
* 🧪 CTF & Security Research

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository
🍴 Fork the repository
🐛 Report bugs
💡 Suggest improvements

---

## 📜 License

This project is available for educational purposes.

You can add an appropriate open-source license such as **MIT License** if you want others to freely use and modify the project.
