from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatBot(state: State):
    response = llm.invoke(state.get("messages"))
    return { "messages": [response] }

def sampleNode(state: State):
    response = llm.invoke(state.get("messages"))
    return { "messages": [response] }

graph_builder = StateGraph(State)

graph_builder.add_node("chatBot", chatBot)
graph_builder.add_node("sampleNode", sampleNode)

graph_builder.add_edge(START, "chatBot")
graph_builder.add_edge("chatBot", "sampleNode")
graph_builder.add_edge("sampleNode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi, I am invoking you"]}))
print("\n\nUpdated state: ", updated_state)

# START -> chatBot -> sampleNode -> END

# state : { messages: ["hey"] }
# node run : chatbot(state: ["hey"]) -> ["Hi, this is from chatbot"]
# state: { messages: ["hey", "Hi, this is from chatbot"] }