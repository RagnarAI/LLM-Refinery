# LLM_Refinery/agents/evaluation_agent.py

from LLM_Refinery.core.llm_agent_core import call_llm

class EvaluationAgent:
    def __init__(self):
        self.name = "EvaluationAgent"

    def run(self, original: str, refined: str, goal: str) -> dict:
        eval_prompt = (
            f"Compare the following two prompts.\n\n"
            f"Original:\n{original}\n\n"
            f"Refined:\n{refined}\n\n"
            f"Determine if the refined version aligns with the user's goal: '{goal}'. "
            f"Provide a numerical score (0-10), a yes/no decision, and a one-sentence justification."
        )

        result = call_llm(eval_prompt, system_prompt="You are a writing evaluator scoring goal alignment.")
        
        # Expected output format (you may later refine parser here)
        return {
            "raw_feedback": result
        }
