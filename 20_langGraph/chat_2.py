from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatBot(state: State):
    print("state of chatBot node: ", state)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            { 'role': 'user', 'content': state.get("user_query") }
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

def evaluate_response(state: State) -> Literal["chatBot_gemini", "endNode"]:
    # print("state of evaluate_response node: ", state)

    print(f"Response of chatBot: ", state.get("llm_output"))
    print("Is this response of llm good for you")
    user_response = input("Type Yes or No: ")

    if user_response.lower() == "yes":
        return "endNode"
    
    return "chatBot_gemini"

def chatBot_gemini(state: State):
    print("state of chatBot_gemini node: ", state)
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            { 'role': 'user', 'content': state.get("user_query") }
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

def endNode(state: State):
    print("state of endNode node: ", state)
    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatBot", chatBot)
graph_builder.add_node("evaluate_response", evaluate_response)
graph_builder.add_node("chatBot_gemini", chatBot_gemini)
graph_builder.add_node("endNode", endNode)

graph_builder.add_edge(START, "chatBot")
graph_builder.add_conditional_edges("chatBot", evaluate_response) 
graph_builder.add_edge("chatBot_gemini", "endNode")
graph_builder.add_edge("endNode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({ "user_query": "what is 2+2" })) # type: ignore

print("updated state: ", updated_state)