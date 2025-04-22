from LLM_Refinery.core.llm_agent_core import call_llm
import json

class AgentComposer:
    def __init__(self):
        self.name = "AgentComposer"

    def select_agents(self, context_enriched_prompt: dict) -> list:
        context_summary = json.dumps(context_enriched_prompt, indent=2)

        prompt = f"""
You are an AI system managing a refinement pipeline of text agents.

Given the following user input and its context, return a list of agents (from the options below) that should process it:
- GoalAgent
- ToneAgent
- GrammarAgent
- VocabularyAgent
- CompressionAgent
- StyleAgent


Only return a JSON list of the agents you would activate. No explanation needed.

Context:
{context_summary}
        """

        system = "You are a smart task router. You decide which text-refinement agents to activate for a user’s prompt."
        
        try:
            response = call_llm(prompt, system_prompt=system)
            agents = json.loads(response)
            if isinstance(agents, list):
                return agents
        except Exception as e:
            print(f"[⚠️ AgentComposer Error] {e}")

        # Fallback
        return ["GrammarAgent"]
