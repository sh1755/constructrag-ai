from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama


# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Load FAISS vector database
vectorstore = FAISS.load_local(
    "vectorstore/faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)


# Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# Load Ollama LLM
llm = Ollama(model="llama3.1")


# Main RAG function
def ask_construction_assistant(question):

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    # Combine retrieved content
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Prompt
    prompt = f"""
You are an AI assistant for construction products.

Use ONLY the provided information.

Construction product information:
{context}

User Question:
{question}

Give:
1. Recommendation
2. Product comparison
3. Compatibility
4. Price analysis
5. Sources
"""

    # Generate answer
    answer = llm.invoke(prompt)

    return answer, docs