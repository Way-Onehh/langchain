from langchain_openai.chat_models.base import BaseChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
import io 
import json

#初始化
Path="./config/key"
with io.open(Path,'r') as file:
    josn_data_text=file.read()
json_data=json.loads(josn_data_text)
llm = BaseChatOpenAI(
    model='deepseek-reasoner',  # 使用DeepSeek聊天模型
    openai_api_key=json_data["deepseek_key"],  # 替换为你的API易API密钥
    openai_api_base='https://api.deepseek.com',  # API易的端点
    max_tokens=1024  # 设置最大生成token数
    )

# if __name__ == "__main__":
#     # 使用llm
#     chatMessages=[]
#     chatMessages.append(SystemMessage(content="你是一个人工智能助手,请使用中文回答问题，注意回答是纯文本避免使用“**”、“** 字符串 **”、“-”、等让人疑惑的符号"))
#     chatMessages.append(HumanMessage(content="你好"))
#     while True:
#         response = llm.invoke(chatMessages)
#         print(f"ai:{response.content}")
#         chatMessages.append(response)
#         input_str=input("usr:")
#         chatMessages.append(HumanMessage(content=input_str))



if __name__ == "__main__":
    # 使用llm
    chatMessages=[]
    chatMessages.append({"role":"system","content": "你是一个人工智能助手,请使用中文回答问题，注意回答是纯文本避免使用“**”、“** 字符串 **”、“-”、等让人疑惑的符号"})
    chatMessages.append({"role":"user","content":"你好"})
    while True:
        response = llm.invoke(chatMessages)
        print(f"ai:{response.content}")
        chatMessages.append(response)
        input_str=input("user:")
        chatMessages.append({"role":"user","content":input_str})