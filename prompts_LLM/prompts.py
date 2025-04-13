from langchain_core.prompts import ChatPromptTemplate
from Chat_Robot import llm
# from langchain_core.prompts import SystemMessagePromptTemplate
# from langchain_core.prompts import HumanMessagePromptTemplate
# from langchain_core.prompts import AIMessagePromptTemplate

#note this block code use str type
SystemMessagePromptT="你是一个代码生成工具，根据用户的需求，生成{programming_language}代码"
print(SystemMessagePromptT)
HumanMessagePromptT="我的需求是{Demand_scenarios}"
print(HumanMessagePromptT)


#generate a prompt 
ChatPromptT= ChatPromptTemplate.from_messages([("system", SystemMessagePromptT),("user",HumanMessagePromptT)])
print(ChatPromptT)
prompt=ChatPromptT.invoke({"programming_language":"c++","Demand_scenarios":"实现一个hello world"})
print(prompt)
ret= llm.invoke(prompt)
print(ret.content)

