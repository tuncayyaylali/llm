from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model=ChatOpenAI(model="gpt-4", temperature=0.5)
messages = [
    HumanMessage("Hi! How are you?"), 
    SystemMessage(content="Translate the following from English to German")
    ]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(f"AI: {response.content}")