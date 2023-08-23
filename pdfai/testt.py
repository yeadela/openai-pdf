import env
from langchain.chat_models import ChatOpenAI 
from langchain.schema import (HumanMessage, SystemMessage)

env.init()

chat = ChatOpenAI(temperature=0)
message =[HumanMessage(content="hello world")]

print(chat(message).content)