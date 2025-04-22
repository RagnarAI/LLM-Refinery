# LLM_Refinery/agents/compression_agent.py

from LLM_Refinery.core.llm_agent_core import call_llm

class CompressionAgent:
    def __init__(self):
        self.name = "CompressionAgent"

    def run(self, text: str) -> str:
        prompt = (
            "Please compress the following message to be shorter and more concise without losing meaning:\n\n"
            f"{text}"
        )
        return call_llm(prompt, system_prompt="You are a summarization assistant optimizing brevity and clarity.")
