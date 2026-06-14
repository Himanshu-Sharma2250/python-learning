from openai import OpenAI
import dotenv

dotenv.load_dotenv()

client = OpenAI()

# One Shot Prompting : The model is given a direct question or task without prior examples

SYSTEM_PROMPT = 'You should only and only answer coding related problems. if ask about other problems say sorry. '

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'Hey there!' },
    ]
)

print(response.choices[0].message.content)