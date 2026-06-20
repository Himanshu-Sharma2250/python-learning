from openai import OpenAI, AsyncOpenAI
from openai.helpers import LocalAudioPlayer
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional
import speech_recognition as sr
import requests
import asyncio
import json
import os

load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()
recognizer = sr.Recognizer()

async def tts(speech: str):
    instructions = """Affect/personality: A cheerful guide \n\nTone: Friendly, clear, and reassuring, creating a calm atmosphere and making the listener feel confident and comfortable.\n\nPronunciation: Clear, articulate, and steady, ensuring each instruction is easily understood while maintaining a natural, conversational flow.\n\nPause: Brief, purposeful pauses after key instructions (e.g., \"cross the street\" and \"turn right\") to allow time for the listener to process the information and follow along.\n\nEmotion: Warm and supportive, conveying empathy and care, ensuring the listener feels guided and safe throughout the journey."""

    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="sage",
        input=speech,
        instructions=instructions,
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)

class ToolInput(BaseModel):
    city: Optional[str] = Field(None, description="City name, for get_weather")
    cmd: Optional[str] = Field(None, description="Shell command, for run_command")
    root_dir: Optional[str] = Field(None, description="Root directory to search in, for find_and_read_file")
    query: Optional[str] = Field(None, description="Partial filename to search for, for find_and_read_file")

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The Id of the step. Example, START, PLAN, TOOL, OUTPUT, etc")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The Id of the tool to call")
    input: Optional[ToolInput] = Field(None, description="The input params for the tool")

# TOOLS
def run_command(cmd: str):
    result = os.system(cmd)
    return result

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url=url, timeout=10)

    if response.status_code == 200:
        return f"Weather of {city} is {response.text}"

    return "Something went wrong"

def find_files(root_dir, query, max_results=20, ignore_dirs=None, case_sensitive=False):
    """
    Recursively search a directory for files matching a name/pattern.
    Skips common noise folders.
    """
    if ignore_dirs is None:
        ignore_dirs = ['node_modules', '.git', 'dist', 'build', '.next', '__pycache__', 'venv', '.venv']

    results = []
    normalized_query = query if case_sensitive else query.lower()

    def walk(directory):
        if len(results) >= max_results:
            return
        try:
            entries = os.scandir(directory)
        except (PermissionError, FileNotFoundError, NotADirectoryError):
            return # permission denied, missing dir, etc — skip silently

        for entry in entries:
            if len(results) >= max_results:
                return
            if entry.is_dir(follow_symlinks=False):
                if entry.name not in ignore_dirs:
                    walk(entry.path)
            else:
                name = entry.name if case_sensitive else entry.name.lower()
                if normalized_query in name:
                    results.append(entry.path)

    walk(root_dir)
    return results

def read_file_safe(file_path, max_bytes=500_000):
    """
    Read a file's content safely, with size limits.
    """
    size = os.path.getsize(file_path)
    if size > max_bytes:
        raise ValueError(f"File too large ({size} bytes): {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def find_and_read_file(root_dir, query):
    """
    The "agent tool" — combines find + read in one call.
    This is what you'd expose to the LLM as a function/tool.
    """
    matches = find_files(root_dir, query)

    if not matches:
        return {
            "found": False,
            "message": f'No file matching "{query}" found under {root_dir}'
        }

    if len(matches) == 1:
        return {
            "found": True,
            "path": matches[0],
            "content": read_file_safe(matches[0])
        }

    # Multiple matches — let the agent/LLM decide, or just return the list
    return {
        "found": True,
        "multiple": True,
        "candidates": matches,
        "message": f"Found {len(matches)} matches — specify which one."
    }

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command,
    "find_and_read_file": find_and_read_file
}

with sr.Microphone() as source: # Mic Access
    recognizer.adjust_for_ambient_noise(source)
    recognizer.pause_threshold = 2

    SYSTEM_PROMPT = """
        You're an expert voice agent.
        You're given the transcript of what user has said using voice.
        You need to output as if you are an voice agent and whatever you speak will be converted to audio using AI and played back to user.
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
        - find_and_read_file(root_dir: str, query: str): Search for a file by partial name/path within a project, then read its contents. Use when the user references a file without giving the exact path.

        If a tool returns an error, acknowledge it in your next PLAN step and decide whether to retry with corrected input or give up and explain the issue in OUTPUT.

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
        PLAN: { "step": "TOOL", "tool": "get_weather", "input": {"city": "Delhi"} }
        PLAN: { "step": "OBSERVE", "tool": "get_weather", "output": "The temperature of Delhi is cloudy with 20 deg C" }
        PLAN: { "step": "PLAN", "content": "Great, I got the weather info of Delhi" }
        PLAN: { "step": "OUTPUT", "content": "The current weather of Delhi is Cloudy and temperature of 20 deg C" }

        Example 3:
        START: Can you find and read the cursor.py file?
        PLAN: { "step": "PLAN", "content": "User wants me to locate and read a specific file" }
        PLAN: { "step": "PLAN", "content": "I have find_and_read_file tool available for this" }
        PLAN: { "step": "TOOL", "tool": "find_and_read_file", "input": {"root_dir": ".", "query": "cursor.py"} }
        PLAN: { "step": "OBSERVE", "tool": "find_and_read_file", "output": "{...file content...}" }
        PLAN: { "step": "PLAN", "content": "Got the file content, now I can summarize or answer" }
        PLAN: { "step": "OUTPUT", "content": "..." }
    """ 

    message_history = [
        { "role": "system", "content": SYSTEM_PROMPT }
    ]

    while True:
        print("Speak Something 🎙️")
        try:
            audio = recognizer.listen(source)
        except Exception as e:
            print(f"❌ Failed to capture audio: {e}")
            continue

        print("Processing audio...") # STT
        try:
            user_query = recognizer.recognize_google(audio)  # type: ignore
        except sr.UnknownValueError:
            print("❌ Could not understand audio, please try again.")
            continue
        except sr.RequestError as e:
            print(f"❌ Speech recognition service error: {e}")
            continue
        except Exception as e:
            print(f"❌ Unexpected error during speech recognition: {e}")
            continue

        print("You said: ", user_query)

        message_history.append({ 'role': 'user', 'content': user_query })

        while True:
            try:
                response = client.chat.completions.parse(
                    model='gpt-4o-mini',
                    response_format=MyOutputFormat,
                    messages=message_history # type: ignore
                )
            except Exception as e:
                print(f"❌ Failed to get response from model: {e}")
                # Drop back out to listen again rather than looping forever
                break

            raw_result = response.choices[0].message.content
            message_history.append({ "role": "assistant", "content": raw_result }) # type: ignore

            try:
                parsed_output = response.choices[0].message.parsed # type: ignore
            except Exception as e:
                print(f"❌ Failed to parse model output: {e}")
                break

            if parsed_output is None:
                print("❌ Model returned no parsed output, skipping this turn.")
                break

            if parsed_output.step == "START": # type: ignore
                print("🔥", parsed_output.content) # type: ignore
                continue

            if parsed_output.step == "TOOL":  # type: ignore
                tool_to_call = parsed_output.tool # type: ignore
                tool_input = parsed_output.input.model_dump(exclude_none=True) if parsed_output.input else {} # type: ignore
                print(f"🔨: {tool_to_call} ({tool_input})")

                try:
                    if tool_to_call not in available_tools:
                        raise ValueError(f"Unknown tool '{tool_to_call}'")

                    tool_response = available_tools[tool_to_call](**tool_input) # type: ignore
                    print(f"🔨: {tool_to_call} ({tool_input}) = {tool_response}")

                except TypeError as e:
                    # Usually wrong/missing arguments from the model
                    tool_response = f"Error calling {tool_to_call} with {tool_input}: {e}"
                    print(f"❌ {tool_response}")

                except Exception as e:
                    tool_response = f"Error while running {tool_to_call}: {e}"
                    print(f"❌ {tool_response}")

                try:
                    observe_payload = json.dumps(
                        { "step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response }
                    )
                except (TypeError, ValueError) as e:
                    # In case tool_response isn't JSON-serializable
                    observe_payload = json.dumps(
                        { "step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": str(tool_response) }
                    )
                    print(f"⚠️ Tool output wasn't JSON-serializable, converted to string: {e}")

                message_history.append(
                    { "role": "developer", "content": observe_payload }
                )
                continue

            if parsed_output.step == "PLAN": # type: ignore
                print("🧠", parsed_output.content) # type: ignore
                continue

            if parsed_output.step == "OUTPUT": # type: ignore
                print("🤖", parsed_output.content) # type: ignore
                try:
                    asyncio.run(tts(response.choices[0].message.content)) # type: ignore
                except Exception as e:
                    print(f"❌ Failed to play back audio response: {e}")
                break

        print('\n\n')