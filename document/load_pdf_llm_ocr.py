#文字提取+llm修复
#Tesseract-OCR
#poppler-24.08.0

import fitz  # PyMuPDF 
from pdf2image import convert_from_path 
import pytesseract 
from PIL import Image, ImageFilter 
from langchain_openai.chat_models.base import BaseChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import io 
import json

pdf_path = "config/5.pdf"  # 替换为您的PDF文件路径 

#extract txt
txt_text = ""
doc = fitz.open(pdf_path) 
for page_num in range(len(doc)):
    page = doc.load_page(page_num) 
    txt_text += page.get_text("text")  + "\n"
print(txt_text)

#extract image txt
images_text = ""
images = convert_from_path(pdf_path,dpi=900)
index=0
for image in images:
    image_path="config/image"
    #图片预处理：灰度化、锐化、二值化 
    image = image.convert('L')   # 灰度化 
    image = image.filter(ImageFilter.SHARPEN)   # 锐化 
    image = image.point(lambda  x: 0 if x < 128 else 255, '1')  # 二值化 
    image.save(image_path+str(index)+".png", "PNG")
    # 使用OCR提取文字 
    ocr_text = pytesseract.image_to_string(image,  lang='chi_sim')
    print(ocr_text)
    images_text += ocr_text + "\n"
    index+=1

#generate a prompt 
SystemMessagePromptT="你是一个图片提取文字的修复工具，根据用户的上下文，合理推断修复提取的文本。输出格式为{format}"
HumanMessagePromptT="我提取的文字为{txt}"
ChatPromptT= ChatPromptTemplate.from_messages([
    ("system", SystemMessagePromptT),
    ("user",HumanMessagePromptT)
    ])

#call llm by prompt
Path="./config/key"
with io.open(Path,'r') as file:
    josn_data_text=file.read()
json_data=json.loads(josn_data_text)
llm = BaseChatOpenAI(
    model='deepseek-reasoner',  # 使用DeepSeek聊天模型
    openai_api_key=json_data["deepseek_key"],  # 替换为你的API易API密钥
    openai_api_base='https://api.deepseek.com',  # API易的端点
    max_tokens=1024,  # 设置最大生成token数
    temperature=0.0
    )
langchain= ChatPromptT | llm |StrOutputParser()
langchain.invoke({"format":"<修复的文本>","txt":images_text})