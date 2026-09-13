from langchain_community.document_loaders import PyMuPDFLoader


FILE_PATH = "data/documents/employee_handbook.pdf"


loader = PyMuPDFLoader(FILE_PATH = "C:\\Users\\kshit\\Documents\\Data Science\\Project- AI-Document-Intelligence-Agent\\L-8 Building Blocks in Economies.pdf")

documents = loader.load()

print("Number of pages:", len(documents))

for document in documents[:2]:
    print("\n--- PAGE ---")
    print(document.page_content[:1000])
    print("\nMetadata:")
    print(document.metadata)