import streamlit as st
from rag_chain import ask_construction_assistant


st.set_page_config(
    page_title="Construction RAG Assistant",
    page_icon="🏗️",
    layout="wide"
)


st.title("🏗️ Construction Product RAG Assistant")

st.write(
    "Ask questions about construction products, suppliers, prices, and compatibility."
)


question = st.text_input(
    "Enter your question:",
    placeholder="Example: Compare cement board and plasterboard for bathroom walls"
)


if st.button("Ask AI"):

    if question.strip():

        with st.spinner("Searching construction knowledge base..."):
            answer, docs = ask_construction_assistant(question)

        st.subheader("AI Answer")
        st.write(answer)

        st.subheader("Retrieved Sources")

        for i, doc in enumerate(docs, start=1):
            st.info(f"Source {i}\n\n{doc.page_content}")

    else:
        st.warning("Please enter a question first.")