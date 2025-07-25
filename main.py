from llm import get_chain
from retriever import setup_retriever
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def main():
    retriever = setup_retriever()
    chain = get_chain()

    print("💬 Give your frontend instruction:")
    user_input = input("> ")

    context_docs = retriever.invoke(user_input)  # updated method
    context = "\n\n".join([doc.page_content for doc in context_docs])

    result = chain.invoke({"question": user_input, "context": context})
    print("\n🧠 Generated React + MUI Code:\n")
    print(result.content)

if __name__ == "__main__":
    main()
