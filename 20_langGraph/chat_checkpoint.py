from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langgraph.checkpoint.mongodb import MongoDBSaver

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

graph_builder = StateGraph(State)

graph_builder.add_node("chatBot", chatBot)

graph_builder.add_edge(START, "chatBot")
graph_builder.add_edge("chatBot", END)

graph = graph_builder.compile()

def compile_graph_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)

DB_URI = "mongodb://admin:admin@localhost:27017"
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer = compile_graph_checkpointer(checkpointer=checkpointer)

    config = {
        "configurable": {
            "thread_id": "himanshu"
        }
    }

    for chunk in graph_with_checkpointer.stream(State({"messages": ["Hi, who am I"]}), config, stream_mode="values"): # type: ignore
        chunk["messages"][-1].pretty_print() # type: ignore

# START -> chatBot -> sampleNode -> END

# state : { messages: ["hey"] }
# node run : chatbot(state: ["hey"]) -> ["Hi, this is from chatbot"]
# state: { messages: ["hey", "Hi, this is from chatbot"] }