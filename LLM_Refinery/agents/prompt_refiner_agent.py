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

        # Natural language instruction framing
        refined_prompt = (
            f"Rewrite the following message with the goal of: {goal}.\n"
            f"Use a tone that is {tone}, and a style that feels {style}.\n"
            f"Write as if you are a {persona}, addressing the audience in the context of {domain}.\n\n"
            f"Original message:\n{user_input}"
        )

        return refined_prompt
