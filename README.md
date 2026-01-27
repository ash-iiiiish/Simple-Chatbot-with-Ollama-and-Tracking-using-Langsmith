# Simple Chatbot with Ollama and LangSmith Tracking

## Introduction
This project demonstrates a **simple Streamlit-based chatbot** powered by **Ollama** using the **Gemma model**, with environment configuration handled via `python-dotenv`. The chatbot provides an interactive UI for asking questions and receiving responses from a locally running LLM.

The project is designed as a minimal, easy-to-understand example for developers experimenting with:
- Local LLMs using Ollama
- Streamlit for rapid UI development
- LangChain-compatible LLM interfaces
- (Optional) Experiment tracking concepts with LangSmith

---

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Example](#example)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

## Project Structure
```
Simple-Chatbot-with-Ollama-and-Tracking-using-Langsmith/
│
├── ollama.py              # Streamlit chatbot application
├── description.ipynb      # Notebook explaining the project
├── images/
│   └── image.png          # Project image/assets
└── README.md              # Project documentation
```

---

## Features
- Interactive chatbot UI built with **Streamlit**
- Uses **Ollama** to run LLMs locally
- Powered by the **Gemma** language model
- Simple and minimal codebase
- Environment variable support via `.env`

---

## Installation

### Prerequisites
- Python 3.9+
- Ollama installed and running locally
- Gemma model pulled in Ollama

```bash
ollama pull gemma3
```

### Clone the Repository
```bash
git clone https://github.com/ash-iiiiish/Simple-Chatbot-with-Ollama-and-Tracking-using-Langsmith.git
cd Simple-Chatbot-with-Ollama-and-Tracking-using-Langsmith
```

### Install Dependencies
```bash
pip install streamlit langchain langchain-community python-dotenv
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run ollama.py
```

Then open your browser at:
```
http://localhost:8501
```

Enter a question in the input box to interact with the chatbot.

---

## Configuration
Create a `.env` file in the project root if you plan to add API keys or LangSmith configuration:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
```

*(LangSmith usage is optional and can be extended further.)*

---

## Dependencies
- `streamlit`
- `langchain`
- `langchain-community`
- `python-dotenv`
- `ollama` (local runtime)

---

## Example
**Input:**
```
What is a large language model?
```

**Output:**
```
A large language model is an AI system trained on vast amounts of text data...
```

---

## Troubleshooting
- Ensure Ollama is running: `ollama serve`
- Verify the model name matches what is installed (`gemma3`)
- Check Python version compatibility
- Restart Streamlit if changes are not reflected

---

## 👨‍💻 Contributors
- [@ash-iiiiish](https://github.com/ash-iiiiish)

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

