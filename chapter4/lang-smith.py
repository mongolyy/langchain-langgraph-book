from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
output = llm.invoke("Hello, world!")
print(output)
