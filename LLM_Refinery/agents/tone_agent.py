# LLM_Refinery/agents/tone_agent.py

from LLM_Refinery.core.llm_agent_core import call_llm

class ToneAgent:
    def __init__(self, tone: str):
        self.tone = tone

    def process(self, text: str) -> str:
        prompt = f"Rewrite the following in a {self.tone} tone:\n\n{text}"
        return call_llm(prompt, system_prompt="You adjust tone in writing.")
