from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    collection_name="paper_a",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

# Fetch all stored docs
docs = db.get()

print("\n🔍 RAW DB DATA:\n")
print("Total docs:", len(docs["documents"]))

for i in range(3):
    print(f"\n--- Stored Doc {i} ---")
    print(docs["documents"][i][:500])
    print("Metadata:", docs["metadatas"][i])