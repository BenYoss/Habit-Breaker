from langchain_nvidia_ai_endpoints import ChatNVIDIA,NVIDIAEmbeddings

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class Persona:
   def __init__(self, _personality, _data):

    self.personality_prompt = "You are an expert in reminding users of their deadlines. You have the personality of a " + _personality + """
    . When speaking, provide motivational feedback to encourage the user to perform work. Have a sense of humor and be witty and brief with responses.
     Be sure to use the content in brackets as a reference to remind the user of deadlines. [""" + _data + "]"
    self.llm = ChatNVIDIA(model="microsoft/phi-3-mini-128k-instruct", nvidia_api_key=os.getenv("PHI_3_LLM_KEY"), max_tokens=200)
    result = self.llm.invoke(self.personality_prompt)
    print(result.content)
   def input_text(self, text):
      result = self.llm.invoke(text)
      print(result.content)

if __name__ == "__main__":
    builder = Persona("A pirate that lisps.", "{title: 'Homework study for CPST class.', current_time: '3:40', event_start_time: '3:45'}")
    import pdb; pdb.set_trace()