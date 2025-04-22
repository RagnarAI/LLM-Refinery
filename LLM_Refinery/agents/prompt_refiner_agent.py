# LLM_Refinery/agents/prompt_refiner_agent.py

from LLM_Refinery.core.llm_agent_core import call_llm

class PromptRefinerAgent:
    def __init__(self):
        self.name = "PromptRefinerAgent"

    def run(self, context_enriched_prompt: dict) -> str:
        goal = context_enriched_prompt.get("goal", "refine").strip()
        domain = context_enriched_prompt.get("domain", "general").strip()
        tone = context_enriched_prompt["context"].get("tone", "neutral").strip()
        style = context_enriched_prompt["context"].get("style", "default").strip()
        persona = context_enriched_prompt["context"].get("persona", "assistant").strip()
        user_input = context_enriched_prompt.get("original_input", "").strip()

        base_instruction = (
            f"Rewrite the following message with the goal of: {goal}.\n"
            f"Use a tone that is {tone}, and a style that feels {style}.\n"
            f"Write as if you are a {persona}, addressing the audience in the context of {domain}.\n\n"
            f"Original message:\n{user_input}"
        )

        return call_llm(base_instruction, system_prompt="You are an expert in writing transformation and prompt preparation.")
