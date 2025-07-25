from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return ChatOpenAI(
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        model=os.getenv("OPENROUTER_MODEL")
    )

def get_chain():
    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template="""
You are an expert React developer with extensive experience in Material-UI.

Your task is to generate clean, efficient, and production-ready JSX code using React and Material-UI based on the following context and user instruction.

Context:
{context}

Instruction:
{question}

Guidelines:
- Code Quality: Clean, modular, and adheres to React + MUI best practices
- Error Handling: Add error boundaries or input validation where relevant
- Prop Validation: Use PropTypes if applicable
- Comments: Include comments for non-trivial logic
- Responsiveness: Ensure layout works well across screen sizes
- Accessibility: Use ARIA roles, labels, and semantic HTML where appropriate

Output:
Only return the complete JSX (and necessary JS code). No explanations or text outside the code block.

"""
    )
    return prompt | get_llm()
