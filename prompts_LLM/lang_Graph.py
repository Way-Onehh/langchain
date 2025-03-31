from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
# from langchain_openai.chat_models.base import BaseChatOpenAI

# from langchain_core.messages import SystemMessage
# from langchain_core.messages import HumanMessage
# from langchain_core.messages import AIMessage

# import io 
# import json

# Path="./config/key"
# with io.open(Path,'r') as file:
#     josn_data_text=file.read()
# json_data=json.loads(josn_data_text)


# #初始化
# llm = BaseChatOpenAI(
#     model='deepseek-reasoner',  # 使用DeepSeek聊天模型
#     openai_api_key=json_data["deepseek_key"],  # 替换为你的API易API密钥
#     openai_api_base='https://api.deepseek.com',  # API易的端点
#     max_tokens=1024  # 设置最大生成token数
#     )

from Chat_Robot import *
# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {"messages": response}


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}

query = "Hi! I'm Bob."

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()  # output contains all messages in state

query = "What's my name?"

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()

#注意线程id变了
config = {"configurable": {"thread_id": "abc123"}}

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()