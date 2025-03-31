from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings 
# Initialize with an embedding model
model_name = "sentence-transformers/all-MiniLM-L6-v2"
vector_store = InMemoryVectorStore(embedding=HuggingFaceEmbeddings(model_name=model_name))

from langchain_core.documents import Document

document_1 = Document(
    page_content="I had chocalate chip pancakes and scrambled eggs for breakfast this morning.",
    metadata={"source": "tweet"},
)

document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
)

documents = [document_1, document_2]

vector_store.add_documents(documents=documents)
auto =vector_store.similarity_search("weather")
print(auto)