import streamlit as st
from llm import get_chain
from retriever import setup_retriever

def run_instruction(instruction: str):
    retriever = setup_retriever()
    chain = get_chain()

    context_docs = retriever.invoke(instruction)
    context = "\n\n".join([doc.page_content for doc in context_docs])

    result = chain.invoke({"question": instruction, "context": context})
    return result.content.strip()

def save_jsx(code, filename="generated_code.jsx"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

st.set_page_config(page_title="React + MUI Code Generator", layout="wide")
st.title("🛠️ React JS + Material UI Code Generator")

instruction = st.text_area("Enter your instruction:", height=150, placeholder="E.g., Create a responsive navbar using Material UI")

if st.button("Generate JSX Code"):
    if instruction:
        with st.spinner("Generating code..."):
            code = run_instruction(instruction)
            st.code(code, language="jsx")
            save_jsx(code)
            st.success("Code generated successfully!")
            st.download_button("⬇️ Download JSX File", code, file_name="generated_code.jsx", mime="text/plain")
    else:
        st.warning("Please enter an instruction.")
