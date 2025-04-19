from LLM_Refinery.core.llm_agent_core import LLMRewriteCore

class ToneAgent:
    def __init__(self):
        self.name = "ToneAgent"
        self.rewriter = LLMRewriteCore()

    def run(self, text: str, context: dict = {}) -> str:
        return self.rewriter.rewrite(
            text=text,
            goal=context.get("goal", ""),
            tone=context.get("tone", "neutral"),
            style=context.get("style", ""),
            persona=context.get("persona", ""),
            domain=context.get("domain", "")
        )
