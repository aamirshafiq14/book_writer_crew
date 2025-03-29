from crewai import Task

from dotenv import load_dotenv

load_dotenv()

class MyTask:
    def Out_line_T (self, agent, topic):
        return Task(
            description=f"""Write a detailed outline of a book, it must contain 5 chapters 
            and each chapter headline should be descriptive""",
            parameter= {"topic": topic},
            expected_output= """Your outline should be according to the below mentioned structure
                            1. Introduction (100 words)
                            2. Theoretical Framework (100 words)
                            3.Literature Review (100 words)
                            4. Research Methodology (100 words)
                            5. Results and Conclusion (100 words)
                            """,
            agent=agent,
    )

    def book_writer_T (self, agent, context):
        return Task(
            description=f"""Write a comprehensive book according to the provided outline, it must be descriptive.
                        The book should be formatted according to International standards.""",
            parameter= {"context" : context},
            expected_output = """Your outline should be according to the below mentioned structure
                            1. Introduction (150 words)
                            2. Theoretical Framework (150 words)
                            3.Literature Review (150 words)
                            4. Research Methodology (150 words)
                            5. Results and Conclusion (150 words)
                            """,
            agent=agent,
            async_execution= True
    )