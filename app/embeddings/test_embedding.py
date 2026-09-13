from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(
    model="bge-m3"
)

text = "Employees are entitled to annual leave."

vector = embeddings.embed_query(text)

print("Embedding generated successfully.")
print("Vector dimension:", len(vector))
print("First 10 values:", vector[:10])