from .agents import BookWriterAgents
from .task import MyTask
from crewai import Crew

#Initialize BookWriterAgents and MyTask
agents = BookWriterAgents()
tasks = MyTask()

out_liner = agents.outliner()
out_liner_T= tasks.Out_line_T(
    agent = out_liner,
    topic = "Machine Learning"
)

crew = Crew(
    agents=[out_liner],
    tasks= [out_liner_T],
    verbose= True,
)

def main():
    result = crew.kickoff()
    print(f"Final Result: {result}")