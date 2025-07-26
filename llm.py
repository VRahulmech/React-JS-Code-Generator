import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
import requests

load_dotenv()

def mistral_api_call(prompt_string):
    prompt_text = str(prompt_string)  # Convert LangChain object to plain string

    messages = [
        {"role": "system", "content": "You are an expert React + Material UI developer."},
        {"role": "user", "content": prompt_text}
    ]

    headers = {
        "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": os.getenv("MISTRAL_MODEL"),
        "messages": messages
    }

    response = requests.post(os.getenv("MISTRAL_URL"), headers=headers, json=json_data)
    response.raise_for_status()
    return {"content": response.json()["choices"][0]["message"]["content"]}

def get_llm():
    return RunnableLambda(mistral_api_call)

def get_chain():
    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template="""
        You are an expert React developer specialized in Material UI (v5+). 
        You are given documentation and an instruction.

        Your task is to generate a clean, functional React component using modern best practices:
        - Use only React functional components.
        - Use Material UI components with the `@mui/material` library.
        - Apply styles using the `sx` prop (do NOT use `@mui/styles` or `makeStyles`).
        - Return only the valid JSX/JavaScript code. Do not include any explanation.

        If the instruction is ambiguous, make reasonable assumptions.

        Documentation (Context):
        {context}

        Instruction:
        {question}
        """
    )
    return prompt | get_llm()
