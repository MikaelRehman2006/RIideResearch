from autogen import AssistantAgent

def run_agent(task_prompt: str) -> str:
    assistant = AssistantAgent(name="autogen_eval")
    reply = assistant.chat(task_prompt)
    return reply
