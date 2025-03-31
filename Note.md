finished llm embeding prompts vectorstores 
continued load->pdf
          embeding using gpu
          vectorstores persistence

1.how to get a llm and to chat
    Chat_Robot.py 
        基础结构
            Chat_Robot=llm + chatMessages
                                =SystemMessage + HumanMessage +  AIMessage
            #使用deepseek openai的兼容api
2.how to generate a prompt 
    use ChatPromptTemplate   =   SystemMessagePromptTemplate  
                                +HumanMessagePromptTemplate 
                                +AIMessagePromptTemplate
                    (
                        1use this method from_messages to combined
                        2use keyvalue to replace key
                        3use this method invoke to generate
                    )

