from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# response = client.responses.create(
#     model='gpt-4o-mini',
#     input="Hey there!"
# )

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        { 'role': 'system', 'content': 'You are an expert in Maths and only and only ans Math related questions. if i ask any question other than maths problem then say sorry.'},
        { 'role': 'user', 'content': 'Write a python code to add two sums'}
    ]
)

print(response.choices[0].message.content)