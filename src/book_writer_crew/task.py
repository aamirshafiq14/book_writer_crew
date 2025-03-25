from crewai import Task

from dotenv import load_dotenv

load_dotenv()

class MyTask:
    def Out_line_T (self, agent, topic):
        return Task(
            description=f"""Write a detailed outline of a book, it must contain 5 chapters 
            and each chapter headline should be descriptive""",
            parameter= {"topic" == topic},
            expected_output= f"""Your outline should be according to the below mentioned structure
                            1. Introduction (100 words)
                            2. Theoretical Framework (100 words)
                            3.Literature Review (100 words)
                            4. Research Methodology (100 words)
                            5. Results and Conclusion (100 words)
                            """,
            agent=agent,
    )