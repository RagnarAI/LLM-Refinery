# LLM_Refinery/agents/style_agent.py

from LLM_Refinery.core.llm_agent_core import call_llm

class StyleAgent:
    def __init__(self, style: str):
        self.style = style

    def run(self, text: str) -> str:
        prompt = (
            f"Rewrite the following text using a style that feels {self.style}.\n\n{text}"
        )
        return call_llm(prompt, system_prompt="You specialize in editing writing style.")
