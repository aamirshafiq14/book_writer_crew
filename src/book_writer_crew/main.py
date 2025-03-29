from .agents import BookWriterAgents
from .task import MyTask
from crewai import Crew

#Initialize BookWriterAgents and MyTask
agents = BookWriterAgents()
tasks = MyTask()

out_liner = agents.outliner()
bookwriter = agents.book_writer()

out_liner_T= tasks.Out_line_T(
    agent = out_liner,
    topic = "Machine Learning"
)

book_writer_T = tasks.book_writer_T(
    agent = bookwriter,
    context = [out_liner_T],
)

crew = Crew(
    agents=[out_liner, bookwriter],
    tasks= [out_liner_T, book_writer_T],

    verbose= True,
)

def main():
    result = crew.kickoff()
    print(f"Final Result: {result}")