
from elevenlabs.client import ElevenLabs
from elevenlabs import play

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ELEVEN_API_KEY")

audio = ElevenLabs(api_key = api_key).generate(
    text = "Ahoy matey! Ye've got a bit o' time till yer CPST class starts, just 5 minutes to be exact! Don't ye be slackin', start yer homework study now! Remember, a pirate never procrastinates, and neither should ye! Yarrr, let's get to it and make yer grades shine brighter than a treasure chest full o' gold doubloons!",
    voice = "Yko7PKHZNXotIFUBG7I9"
)

play(audio)