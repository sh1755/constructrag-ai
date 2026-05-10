import pandas as pd

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# Load CSV file
df = pd.read_csv("data/products.csv")

documents = []

# Convert rows into LangChain documents
for _, row in df.iterrows():

    text = f"""
    Product ID: {row['product_id']}
    Name: {row['name']}
    Category: {row['category']}
    Supplier: {row['supplier']}
    Price: £{row['price']}
    Description: {row['description']}
    Compatible With: {row['compatible_with']}
    """

    doc = Document(
        page_content=text,
        metadata={
            "name": row["name"],
            "supplier": row["supplier"]
        }
    )

    documents.append(doc)


# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Create FAISS vector database
vectorstore = FAISS.from_documents(
    documents,
    embedding_model
)


# Save vector database
vectorstore.save_local("vectorstore/faiss_index")


print("Vector database created successfully.")