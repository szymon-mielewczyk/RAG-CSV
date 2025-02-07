# Store Assistant Project

## Overview
Store Assistant is a project designed to implement Retrieval Augmented Generation (RAG) for question answering using a grocery store dataset. This project leverages powerful tools from the LangChain ecosystem to facilitate document processing, vector storage, and interactive querying. An API key is required for OpenAI services, and an optional API key can be used for LangSmith. 

Project written in Python

## Required Libraries
Ensure the following libraries are installed to run the project:

- `langchain-text-splitters`
- `langchain-community`
- `langgraph`
- `langchain-openai`
- `langchain-core`
- `beautifulsoup4`


## Project Files

- **RAG-txt.ipynb**: Implements a simple RAG using a text data derived from a CSV.
- **RAG-CSV-with_memory.ipynb**: RAG implementation using a CSV file with conversation memory support.
- **RAG-txt-with_memory.ipynb**: RAG implementation using a text file with conversation memory support.
- **download_data.py**: Script to download the dataset from Kaggle.

## Dataset
The dataset is sourced from Kaggle:

[Kaggle Grocery Store Dataset](https://www.kaggle.com/datasets/bhavikjikadara/grocery-store-dataset/data)

Ensure you have Kaggle API credentials configured to download the dataset.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/szymon-mielewczyk/Titanic-Kaggle.git
   ```

2. **Install Required Libraries**
   Install the necessary libraries as listed above.

3. **Set Up API Keys**
   - **OpenAI API Key** (required):
     ```bash
     OPENAI_API_KEY='your_openai_api_key'
     ```
   - **LangSmith API Key** (optional):
     ```bash
     LANGSMITH_API_KEY='your_langsmith_api_key'
     ```

4. **Download Dataset**
   Run the data download script:
   ```bash
   python download_data.py
   ```

5. **Run the Notebooks**
   Use Jupyter Notebook or any compatible environment to open and run the provided `.ipynb` files.

## Credentials
   - For RAG tutorial from LangChain:
     Instructions provided in the [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/).
   
   - For QA with Chat History tutorial from LangChain:
     Refer to the [LangChain QA Chat History Tutorial](https://python.langchain.com/docs/tutorials/qa_chat_history/).

## Usage

- **RAG-txt.ipynb**: Ideal for simple retrieval tasks.
- **RAG-CSV-with_memory.ipynb** & **RAG-txt-with_memory.ipynb**: Use these for enhanced interactions with memory support, providing more context-aware responses.



Feel free to fork the repository.
