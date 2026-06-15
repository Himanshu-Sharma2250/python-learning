from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional
import requests
import json
import os

load_dotenv()

client = OpenAI()

def run_command(cmd: str):
    result = os.system(cmd)
    return result


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url=url)

    if response.status_code == 200:
        return f"Weather of {city} is {response.text}"
    
    return "Something went wrong"

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command
}

SYSTEM_PROMPT = """
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN, OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give the OUTPUT.
    You can also call a tool if required from the list of tools.
    For every tool call wait for the observe step which is the output from the called tool.

    Rules: 
    - Strictly Follow the given JSON output format
    - Only run one step at a time
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and 

    Output JSON Format:
    { 'step': "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string" }

    Available Tools:
    - get_weather(city: str): Takes city name as an input string and returns the weather info about the city.
    - run_command(cmd: str): Takes a system Linux command as string and executes the command on user's system and returns the output from that command

    Example 1: 
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BOSMAS" }
    PLAN: { "step": "PLAN", "content": "Yes, the BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN", "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN", "content": "now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN", "content": "we must perform divide that is 15 / 10 = 1.5" }
    PLAN: { "step": "PLAN", "content": "now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN", "content": "now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN", "content": "Great, we have solved and finally left with answer which is 3.5" }
    PLAN: { "step": "OUTPUT", "content": "3.5" }
    
    Example 2: 
    START: What is the weather of Delhi?
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in getting Delhi's weather" }
    PLAN: { "step": "PLAN", "content": "Lets see if we have any available tool from the list of available tools" }
    PLAN: { "step": "PLAN", "content": "Great we have get_weather tool available for this query" }
    PLAN: { "step": "PLAN", "content": "I need to call get_weather tool for delhi as input for city" }
    PLAN: { "step": "TOOL", "tool": "get_weather", "input": "city" }
    PLAN: { "step": "OBSERVE", "tool": "get_weather", "output": "The temperature of Delhi is cloudy with 20 deg C" }
    PLAN: { "step": "PLAN", "content": "Great, I got the weather info of Delhi" }
    PLAN: { "step": "OUTPUT", "content": "The current weather of Delhi is Cloudy and temperature of 20 deg C" }
""" 

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The Id of the step. Example, START, PLAN, TOOL, OUTPUT, etc")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The Id of the tool to call")
    input: Optional[str] = Field(None, description="The input params for the tool")

message_history = [
    { "role": "system", "content": SYSTEM_PROMPT }
]

while True:
    user_query = input("👤 >")
    message_history.append({ 'role': 'user', 'content': user_query })

    while True:
        response = client.chat.completions.parse(
            model='gpt-4o-mini',
            response_format=MyOutputFormat,
            messages=message_history # type: ignore
        )

        raw_result = response.choices[0].message.content
        message_history.append({ "role": "assistant", "content": raw_result }) # type: ignore

        parsed_output = response.choices[0].message.parsed # type: ignore

        if parsed_output.step == "START": # type: ignore
            print("🔥", parsed_output.content) # type: ignore
            continue

        if parsed_output.step == "TOOL": # type: ignore
            tool_to_call = parsed_output.tool # type: ignore
            tool_input = parsed_output.input # type: ignore
            print(f"🔨: {tool_to_call} ({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input) # type: ignore
            print(f"🔨: {tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append(
                { "role": "developer", "content": json.dumps(
                    { "step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response }
                ) }
            )
            continue

        if parsed_output.step == "PLAN": # type: ignore
            print("🧠", parsed_output.content) # type: ignore
            continue

        if parsed_output.step == "OUTPUT": # type: ignore
            print("🤖", parsed_output.content) # type: ignore
            break

    print('\n\n')

