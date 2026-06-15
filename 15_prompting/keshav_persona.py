from dotenv import load_dotenv
from openai import OpenAI

from keshav_chats import keshav_chats

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = f"You are an AI persona name Keshav. You are acting on based on Keshav sharma who is 23 years old Tech enthusiastic and dotnet intern. your main tech stack is java full stack and you are learning genAI python. Learn from these chats of keshav : {keshav_chats}"

response = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'Hey keshav, tu rahul ke bare mein kya sochta hai' },
    ]
)

print(response.choices[0].message.content)