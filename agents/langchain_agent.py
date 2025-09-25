from langchain_openai import OpenAI

def run_agent(task_prompt: str) -> str:
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
    return llm(task_prompt)
