from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought
    You work on START, PLAN and OUTPUT steps
    You need to first PLAN what needs to be done. The PLAN can be multiple steps
    Once you think enough PLAN has been done, finally you can give an OUTPUT

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time
    - The sequence of steps is START (where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is going to the displayed to the user)

    Output JSON format:
    { 'step : "START" | "PLAN" | "OUTPUT", "content": "string"} 
"""

message_history = [
    { "role": "system", "content": SYSTEM_PROMPT }
]

user_query = input("👤")
message_history.append({ 'role': 'user', 'content': user_query })

while True:
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        response_format={ "type": "json_object" },
        messages=message_history # type: ignore
    )

    raw_result = response.choices[0].message.content
    message_history.append({ "role": "assistant", "content": raw_result }) # type: ignore

    parsed_output = json.loads(raw_result) # type: ignore

    if parsed_output.get("step") == "START":
        print("🔥", parsed_output.get("content"))
        continue

    if parsed_output.get("step") == "PLAN":
        print("🧠", parsed_output.get("content"))
        continue

    if parsed_output.get("step") == "OUTPUT":
        print("🤖", parsed_output.get("content"))
        break

# response = client.chat.completions.create(
#     model='gpt-4o-mini',
#     response_format={ "type": "json_object" },
#     messages=[
#         { 'role': 'system', 'content': SYSTEM_PROMPT },
#         { 'role': 'user', 'content': 'Hey there! can you write a python code for a + b whole square' },
#     ]
# )

print(response.choices[0].message.content)