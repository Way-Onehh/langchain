# 加载本地文本文件 
from langchain_community.document_loaders import TextLoader
loader = TextLoader("config\斗破苍穹.txt") 
documents = loader.load() 

# 初始化切块器 
from langchain.text_splitter  import CharacterTextSplitter 
text_splitter = CharacterTextSplitter(
    separator="\n",  # 按换行符分割 
    chunk_size=512,  # 每块的最大字符数 
    chunk_overlap=200,  # 块与块之间的重叠字符数 
)
chunks = text_splitter.split_documents(documents) 

#嵌入模型+添加到数据库
from langchain_huggingface import HuggingFaceEmbeddings 
model_name = "sentence-transformers/all-MiniLM-L6-v2"
from langchain_core.vectorstores import InMemoryVectorStore
# Initialize with an embedding model
vector_store = InMemoryVectorStore(embedding=HuggingFaceEmbeddings(model_name=model_name))
vector_store.add_documents(documents=chunks)
auto=vector_store.similarity_search("萧炎")
for i  in auto:
    print(i.metadata)
    print(i.page_content)



# #初始化大模型
# from langchain_openai.chat_models.base import BaseChatOpenAI
# import io
# import json
# Path="./config/key"
# with io.open(Path,'r') as file:
#     josn_data_text=file.read()
# json_data=json.loads(josn_data_text)
# llm = BaseChatOpenAI(
#     model='deepseek-reasoner',  # 使用DeepSeek聊天模型
#     openai_api_key=json_data["deepseek_key"],  # 替换为你的API易API密钥
#     openai_api_base='https://api.deepseek.com',  # API易的端点
#     max_tokens=1024  # 设置最大生成token数
#     )