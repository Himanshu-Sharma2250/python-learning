from dotenv import load_dotenv
from openai import OpenAI
from mem0 import Memory
import os
import json

load_dotenv()

client = OpenAI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEO4J_CONNECTION_URI = os.getenv("NEO4J_CONNECTION_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        },
    },
    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "gpt-4.1-mini"
        },
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": NEO4J_CONNECTION_URI,
            "username": NEO4J_USER,
            "password": NEO4J_PASSWORD,
        },
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        },
    },
}

mem_client = Memory.from_config(config)

while True:
    user_query = input("> ")

    search_memory = mem_client.search(user_query, filters={"user_id": "himanshu"})

    memories = [f"Id: {mem.get("id")}\nMemory: {mem.get("memory")}" for mem in search_memory.get("results")] # type: ignore

    SYSTEM_PROMPT = f"""
        Here is the context about user: 
        {json.dumps(memories)}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": user_query }
        ],
        temperature=1.0
    )

    ai_response = response.choices[0].message.content

    print("AI: ", ai_response)

    mem_client.add(
        user_id="himanshu",
        messages=[
            { "role": "user", "content": user_query },
            { "role": "assistant", "content": ai_response },
        ]
    )

    print("Memory has been saved...")