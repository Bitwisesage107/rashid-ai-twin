# 🤖 My AI Twin - Interactive Resume

An advanced, interactive AI clone designed to answer questions about my career, skills, and projects in real-time. Built using **Retrieval-Augmented Generation (RAG)**, this AI Twin acts as a 24/7 personal recruiter interface.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT_Models-green?logo=openai&logoColor=white)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![Modal](https://img.shields.io/badge/Deployment-Modal_Serverless-black?logo=modal)

### 🚀 Live Demo: [https://rashidhusain217--rashid-ai-twin-serve.modal.run](https://rashidhusain217--rashid-ai-twin-serve.modal.run)
---

## ✨ Key Features
- **Retrieval-Augmented Generation (RAG):** The AI answers questions dynamically by running a semantic vector search across a custom knowledge base (my Resume, Projects, and Work Experience).
- **Agentic Tool Calling:** If a recruiter wants to reach out, they can simply say *"Here is my email: name@example.com"*. The AI intelligently triggers a background function to instantly ping my phone with a **Pushover push notification**.
- **Serverless Edge Deployment:** Hosted on **Modal**, meaning the app runs entirely in the cloud with near-instant cold-starts, zero idle costs, and rapid horizontal scaling.
- **Modern UI:** A beautiful, responsive chat interface built with **Gradio** featuring custom CSS, dark mode support, and interactive suggested questions.

## 🧠 Architecture
1. **Embedding Layer:** Uses `nvidia/llama-nemotron-embed-vl-1b-v2:free` (via OpenRouter) to convert my resume and project history into high-dimensional vector embeddings.
2. **Semantic Search:** When a user asks a question, the app calculates cosine similarity between the question's embedding and the knowledge base to pull the exact factual context needed.
3. **LLM Generation:** The context is fed into a large language model (`openai/gpt-oss-120b` via OpenRouter) to construct a conversational, personalized response in the first person.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/rashid-ai-twin.git
   cd rashid-ai-twin
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   OPENROUTER_API_KEY=your_key
   TELEGRAM_BOT_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```
4. **Launch the application:**
   ```bash
   python app.py
   ```
   Open `http://localhost:8000` in your browser.

## ☁️ Deployment
This project is configured for one-click serverless deployment on [Modal](https://modal.com/).
```bash
modal deploy app.py
```
This command automatically containerizes the Python environment, mounts the knowledge base, injects the secrets securely, and publishes the live HTTPS endpoint.
