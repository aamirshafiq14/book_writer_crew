from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

model = LLM(model = 'gemini/gemini-2.0-flash')

class BookWriterAgents:
    def outliner(self):
        return Agent(
            role= "outliner",
            goal= "Write a detailed outline for the book.",
            backstory= "I am an expert book outline writer with an experience of more than 10 years.",
            verbose= True,
            llm= model,
        )