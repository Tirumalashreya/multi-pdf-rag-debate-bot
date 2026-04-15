from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import CrossEncoder

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def get_db(name):
    return Chroma(
        collection_name=name,
        embedding_function=embedding_model,
        persist_directory="./chroma_db"
    )


def retrieve(query, collection_name, k=10):

    db = get_db(collection_name)

    # Step 1: vector search
    docs = db.similarity_search(query, k=k)

    # Step 2: rerank
    pairs = [(query, d.page_content) for d in docs]
    scores = reranker.predict(pairs)

    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)

    return [doc for doc, _ in ranked[:5]]