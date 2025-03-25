from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

model = LLM(model = gemini/gemini-2.0-flash-exp)

class BookWriterAgent