# AI Research Assistant

A lightweight AI-powered research assistant that answers user queries by combining real-time web search with Large Language Models (LLMs). Instead of relying solely on an LLM's pretrained knowledge, the application retrieves relevant information from the web and generates grounded, up-to-date responses.

## Features

* 🔍 Real-time web search for current information
* 🤖 LLM-powered answer generation
* 🌐 Clean and responsive web interface
* 📄 Context-aware responses based on retrieved sources
* ⚡ Fast inference using Groq APIs
* 🧩 Modular backend for easy extension

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python
* FastAPI

### APIs & Services

* Groq API
* Tavily Search API

## How It Works

1. The user enters a research query.
2. The backend sends the query to the Tavily Search API.
3. Relevant web content is retrieved.
4. The retrieved context is passed to the Groq LLM.
5. The LLM synthesizes the information into a concise, coherent answer.
6. The generated response is displayed on the webpage.


## Installation

1. Clone the repository.

```
git clone <repository-url>
cd <repository-folder>
```

2. Create a virtual environment.

```
python -m venv venv
```

3. Activate the environment.

Windows:

```
venv\Scripts\activate
```

Linux/macOS:

```
source venv/bin/activate
```

4. Install the required packages.

```
pip install -r requirements.txt
```

5. Create a `.env` file and add your API keys.

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

6. Run the application.

```
python app.py
```

7. Open your browser and visit:

```
http://localhost:5000
```

## Future Improvements

* Conversation history
* Streaming responses
* Citation support
* Source ranking and reranking
* Multi-agent research workflow
* PDF upload and document querying
* Persistent chat sessions
* Retrieval-Augmented Generation (RAG) with a vector database

## Learning Outcomes

This project demonstrates:

* Integration of LLM APIs into web applications
* REST API integration
* Backend development using FastAPI
* End-to-end deployment of an AI application

## License

This project is intended for educational and learning purposes.
