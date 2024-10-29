from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.tools import tool
import os
import requests

base_url = os.getenv("OLLAMA_HOST")
api_endpoint = "http://127.0.0.1:8200/jumia/search"  # Replace with your API endpoint

# PROMPT_TEMPLATE = """
# You are an assistant with two modes:
# 1. If the user asks a question without the word "search," answer based only on your internal knowledge base.
# 2. If the user includes the word "search," do not answer directly. Instead, pass the terms following "search" as an input to an external API and return the API's response.

# Question: {question}
# """

PROMPT_TEMPLATE = """
You are an assistant with two modes:
1. If the user asks a question without the word "search," respond as an assistant, answering based only on your internal knowledge base.
2. If the user includes the word "search," do not answer directly. Instead, pass the terms following "search" as an input to an external API and return the API's response.

Question: {question}
"""

@tool
def api_request_tool(query: str):
    """Make an API request based on user query"""
    try:
        response = requests.post(api_endpoint, json={"query": query})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        return {"error": str(e)}

def query_llm(query_text: str):
    """Query the LLM for a specific question and make an API request if 'search' is in the query"""

    # Check if "search" is in the input to trigger the API tool
    if query_text.lower().startswith("search "):
        # Extract the search terms following "search"
        search_query = query_text[7:]
        api_response = api_request_tool.invoke(search_query)
        return {"response": f"API search results for '{search_query}', {api_response}"}

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(question=query_text)

    model = OllamaLLM(model="mistral", base_url=base_url)
    response_text = model.invoke(prompt)

    return {"response": response_text}