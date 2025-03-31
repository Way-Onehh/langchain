# # 安装必要的库 
# # pip install langchain chromadb sentence-transformers 
 
# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings 
# from langchain.text_splitter  import CharacterTextSplitter 
# from langchain_community.document_loaders import TextLoader
 
# # 1. 初始化嵌入模型（使用 Sentence Transformers）
# embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
 
# # 2. 加载文本数据（例如从文件中加载）
# loader = TextLoader("config\斗破苍穹.txt")   # 替换为你的文本文件路径 
# documents = loader.load() 
 
# # 3. 分割文本 
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# texts = text_splitter.split_documents(documents) 
 
# # 4. 初始化 Chroma 客户端并添加数据 
# vectorstore = Chroma.from_documents( 
#     documents=texts,
#     embedding=embeddings,
#     persist_directory="./chroma_db"  # 持久化存储目录 
# )
 
 
# # 6. 从 Chroma 中检索数据 
# query = "萧炎妹妹"
# results = vectorstore.similarity_search(query,  k=2)
 
# # 7. 输出检索结果 
# for result in results:
#     print(result.page_content) 


 
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings 
 
# 1. 初始化嵌入模型（与存储数据库时使用的模型一致）
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
 
# 2. 初始化 Chroma 客户端并加载已存储的数据库 
persist_directory = "./chroma_db"  # 替换为你的数据库存储目录 
vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embeddings 
)
 
# 3. 执行检索操作 
query = ""
results = vectorstore.similarity_search(query,  k=2)

# 4. 输出检索结果 
for result in results:
    print(result.page_content) 