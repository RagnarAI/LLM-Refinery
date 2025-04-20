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

from LLM_Refinery.memory.memory_handler import MemoryHandler
from LLM_Refinery.memory.session_manager import SessionManager
from LLM_Refinery.storage.change_log_db import ChangeLogDB
from LLM_Refinery.storage.model_registry import ModelRegistry



def run_pipeline(config, session_id="session_001"):
    user_input = config["original_input"]

    # ✅ Move AGENT_MAP here, after config is available
    AGENT_MAP = {
        "GrammarAgent": GrammarAgent(),
        "VocabularyAgent": VocabularyAgent(),
        "ToneAgent": ToneAgent(config.get("tone", "neutral")),
        "StyleAgent": StyleAgent(),
        "CompressionAgent": CompressionAgent()
    }

    # === Initialize system components ===
    memory = MemoryHandler()
    session = SessionManager()
    changelog = ChangeLogDB()
    registry = ModelRegistry()

    # ...rest of pipeline...


    session.create_session(session_id)

    # === Intake, Context, Refine Prompt ===
    intake = PromptIntakeAgent().run(config)
    context = ContextAnalyzerAgent().run(intake)
    refined_prompt = PromptRefinerAgent().run(context)

    # === Decide agents to activate ===
    selected_agents = AgentComposer().select_agents(context)

    # === Apply selected refinement agents ===
    current_output = refined_prompt
    revision_stack = []

    for agent_name in selected_agents:
        agent = AGENT_MAP.get(agent_name)
        if agent:
            current_output = agent.run(current_output)
            revision_stack.append(current_output)

    # === Synthesize final version ===
    final_response = ResponseSynthesizerAgent().run(revision_stack)

    # === Evaluate result ===
    evaluation = EvaluationAgent().run(refined_prompt, final_response, context["goal"])
    proxy_feedback = ProxyUserAgent().run(evaluation)

    # === Log everything ===
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

    # === Optional loop if failed ===
    if not proxy_feedback["approved"]:
        print(f"\n⚠️  Output rejected by proxy agent: {proxy_feedback['feedback']}")
        print(f"Change Log ID: {changelog_id}")
    else:
        print(f"\n✅ Final Output Approved! Saved to Change Log.\nChange Log ID: {changelog_id}")

    return final_response, evaluation, proxy_feedback
