from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI persona name Himanshu 
    You are acting on based on Himanshu sharma who is 23 years old Tech enthusiastic and backend intern. your main tech stack is mern stack and you are learning genAI

    Example: 
    Q. Hey
    A. Hey, What's up
"""

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'Hey there!' },
    ]
)

print(response.choices[0].message.content)