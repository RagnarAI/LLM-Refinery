# LLM_Refinery/agents/proxy_user_agent.py

from LLM_Refinery.core.llm_agent_core import call_llm

class ProxyUserAgent:
    def __init__(self):
        self.name = "ProxyUserAgent"

    def run(self, evaluation: dict) -> dict:
        feedback_prompt = (
            f"The following evaluation result was returned:\n\n"
            f"{evaluation.get('raw_feedback')}\n\n"
            f"Write user-friendly feedback for the author about whether their prompt was approved and why."
        )
        feedback = call_llm(feedback_prompt, system_prompt="You are a review agent who delivers concise approval feedback.")

        return {
            "approved": "yes" in evaluation.get("raw_feedback", "").lower(),
            "feedback": feedback
        }
