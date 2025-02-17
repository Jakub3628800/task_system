from pathlib import Path
from openai import OpenAI

def create_tts_from_text(text: str) -> str:
    client = OpenAI()
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="sage",
        input=text,
    )
    response.stream_to_file(speech_file_path)
    return str(speech_file_path)


