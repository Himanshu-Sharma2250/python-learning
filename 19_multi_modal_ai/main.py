from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        { 'role': 'user', 'content': 
            [ 
                { 'type': 'text', 'text': "What is this image" }, 
                { 
                    'type': 'image_url', 
                    'image_url': { 
                        'url': 'https://images.pexels.com/photos/20680840/pexels-photo-20680840.jpeg?_gl=1*1f5t7ia*_ga*MTc1OTUzOTY5Mi4xNzgxNjcxNTAw*_ga_8JE65Q40S6*czE3ODE2NzE1MDAkbzEkZzEkdDE3ODE2NzE1MTYkajQ0JGwwJGgw' 
                    } 
                }
            ] 
        }
    ]
)

print(response.choices[0].message.content)