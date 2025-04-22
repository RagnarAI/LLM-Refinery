# LLM_Refinery/agents/goal_agent.py

from LLM_Refinery.core.llm_agent_core import call_llm

class GoalAgent:
    def __init__(self, goal: str):
        self.goal = goal

    def run(self, text: str) -> str:
        prompt = (
            f"Rewrite the following instruction so it clearly conveys a writing goal.\n\n"
            f"Instruction: {self.goal}\n\n"
            f"Then, rewrite the following message to achieve this improved goal:\n{text}"
        )
        return call_llm(prompt, system_prompt="You are a helpful editor who clarifies writing goals.")
