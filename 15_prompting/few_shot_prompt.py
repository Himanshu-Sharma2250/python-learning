from openai import OpenAI
import dotenv

dotenv.load_dotenv()

client = OpenAI()

# Few Shot Prompting : The model is given a direct question or task with prior examples
SYSTEM_PROMPT1 = """
You should only and only answer coding related problems. if ask about other problems say sorry.

Q. Can you explain the a + b whole square?
A. Sorry, I can help with Coding related problems.

Q. Write a program in python for adding two number.
A. def add(a, b):
        return a + b
"""

SYSTEM_PROMPT2 = """
You should only and only answer coding related problems. if ask about other problems say sorry.

Output: {{
    "code": "string" or null,
    "isCodingQuestion": boolean
}}

Q. Can you explain the a + b whole square?
A. {{
    "code": null,
    "isCodingQuestion": False
}}

Q. Write a program in python for adding two number.
A. {{ "code": "def add(a, b):
        return a + b", "isCodingQuestion": True }}
"""

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT2 },
        { 'role': 'user', 'content': 'Hey there! can you write a python code for a + b whole square' },
    ]
)

print(response.choices[0].message.content)