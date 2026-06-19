import asyncio
import speech_recognition as sr
from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()

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

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source: # Mic Access
        recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 2

        SYSTEM_PROMPT = f"""
            You're an expert voice agent.
            You're given the transcript of what user has said using voice.
            You need to output as if you are an voice agent and whatever you speak will be converted to audio using AI and played back to user.
        """

        messages = [
            { "role": "system", "content": SYSTEM_PROMPT }
        ]
        while True:
            print("Speak Something 🎙️")
            audio = recognizer.listen(source)

            print("Processing audio...") # STT
            stt = recognizer.recognize_google(audio) # type: ignore

            print("You said: ", stt)
            messages.append(
                { "role": "user", "content": stt }
            )

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages # type: ignore
            )
        
            print("AI : ", response.choices[0].message.content)

            asyncio.run(tts(response.choices[0].message.content)) # type: ignore

main()
