# LLM_Refinery/core/agent_pipeline.py

from LLM_Refinery.agents.prompt_intake_agent import PromptIntakeAgent
from LLM_Refinery.agents.context_analyzer_agent import ContextAnalyzerAgent
from LLM_Refinery.agents.prompt_refiner_agent import PromptRefinerAgent
from LLM_Refinery.agents.agent_composer import AgentComposer
from LLM_Refinery.agents.grammar_agent import GrammarAgent
from LLM_Refinery.agents.vocabulary_agent import VocabularyAgent
from LLM_Refinery.agents.tone_agent import ToneAgent
from LLM_Refinery.agents.style_agent import StyleAgent
from LLM_Refinery.agents.compression_agent import CompressionAgent
from LLM_Refinery.agents.response_synthesizer_agent import ResponseSynthesizerAgent
from LLM_Refinery.agents.evaluation_agent import EvaluationAgent
from LLM_Refinery.agents.proxy_user_agent import ProxyUserAgent
from LLM_Refinery.agents.goal_agent import GoalAgent
from LLM_Refinery.memory.memory_handler import MemoryHandler
from LLM_Refinery.memory.session_manager import SessionManager
from LLM_Refinery.storage.change_log_db import ChangeLogDB
from LLM_Refinery.storage.model_registry import ModelRegistry


def run_pipeline(config: dict, session_id="session_001", yield_mode=False):
    memory = MemoryHandler()
    session = SessionManager()
    changelog = ChangeLogDB()
    registry = ModelRegistry()

    session.create_session(session_id)

    AGENT_MAP = {
    "GoalAgent": GoalAgent(config.get("goal", "refine")),
    "GrammarAgent": GrammarAgent(),
    "VocabularyAgent": VocabularyAgent(),
    "ToneAgent": ToneAgent(config.get("tone", "neutral")),
    "StyleAgent": StyleAgent(),
    "CompressionAgent": CompressionAgent()
}


    # === Intake, Context, Refine ===
    intake = PromptIntakeAgent().run(config)
    context = ContextAnalyzerAgent().run(intake)
    refined_prompt = PromptRefinerAgent().run(context)

    if yield_mode:
        yield ("PromptIntakeAgent", str(intake))
        yield ("ContextAnalyzerAgent", str(context))
        yield ("PromptRefinerAgent", refined_prompt)

    selected_agents = AgentComposer().select_agents(context)

    current_output = refined_prompt
    revision_stack = []

    for agent_name in selected_agents:
        agent = AGENT_MAP.get(agent_name)
        if agent:
            current_output = agent.run(current_output)
            revision_stack.append(current_output)

            if yield_mode:
                yield (agent_name, current_output)

    final_response = ResponseSynthesizerAgent().run(revision_stack)

    if yield_mode:
        yield ("ResponseSynthesizerAgent", final_response)

    evaluation = EvaluationAgent().run(refined_prompt, final_response, context["goal"])
    proxy_feedback = ProxyUserAgent().run(evaluation)

    changelog_id = changelog.log_change(
        session_id=session_id,
        input_text=refined_prompt,
        output_text=final_response,
        agents_used=selected_agents,
        evaluation_score=evaluation["score"],
        approved=proxy_feedback["approved"]
    )

    session.log_interaction(session_id, refined_prompt, final_response)
    memory.store("last_result", final_response)

    if not yield_mode:
        return final_response, evaluation, proxy_feedback
