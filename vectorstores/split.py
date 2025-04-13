from langchain.text_splitter  import RecursiveCharacterTextSplitter 
from transformers import BertTokenizer, BertForSequenceClassification, pipeline 
 
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain.text_splitter  import CharacterTextSplitter 
from langchain_community.document_loaders import TextLoader
 

#加载文本数据（例如从文件中加载）
loader = TextLoader("config\斗破苍穹.txt")   # 替换为你的文本文件路径 
documents = loader.load() # 1. 切割文本 

# 定义中文分隔符（句号、问号、感叹号、换行符等）
separators = ["。", "！", "？", "；", "，", "、", "（", "）", "《", "》", "……", "—"]
# 1.递归分割
text_splitter = RecursiveCharacterTextSplitter(
    separators=separators,
    chunk_size=400, chunk_overlap=100, length_function=len 
)
splits = text_splitter.split_documents(documents) 
print(splits)

# 2. 加载BERT模型 
tokenizer = BertTokenizer.from_pretrained("config\model\chinese_L-12_H-768_A-12") 
model = BertForSequenceClassification.from_pretrained("config\model\chinese_L-12_H-768_A-12") 
nlp = pipeline("text-classification", model=model, tokenizer=tokenizer)
 
# 3. 处理每个片段 
results = [nlp(segment) for segment in splits]
final_result = max(results, key=lambda x: x[0]["score"])