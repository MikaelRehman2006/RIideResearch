from crewai import Agent

def run_agent(task_prompt: str) -> str:
    agent = Agent()
    result = agent.run(task_prompt)
    return result
