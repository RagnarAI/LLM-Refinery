class AgentComposer:
  def __init__(self):
      self.name = "AgentComposer"

  def select_agents(self, context_enriched_prompt: dict) -> list:
      goal = context_enriched_prompt.get("goal", "").lower()
      tone = context_enriched_prompt["context"].get("tone", "").lower()
      style = context_enriched_prompt["context"].get("style", "").lower()
      domain = context_enriched_prompt["context"].get("domain", "").lower()

      agents_to_run = []

      # Tone Agent Triggers
      if any(kw in goal for kw in ["tone", "emotion", "conviction", "passion", "confident"]) or \
         any(kw in tone for kw in ["confident", "friendly", "formal", "assertive", "casual", "inspirational"]):
          agents_to_run.append("ToneAgent")

      # Grammar Agent Triggers
      if any(kw in goal for kw in ["grammar", "correct", "clean", "fix typos", "refine"]) or \
         any(kw in tone for kw in ["professional", "polished"]):
          agents_to_run.append("GrammarAgent")

      # Vocabulary Agent Triggers
      if any(kw in goal for kw in ["vocabulary", "simplify", "make clear", "clarify"]) or \
         any(kw in domain for kw in ["public", "speech", "message", "story"]):
          agents_to_run.append("VocabularyAgent")

      # Compression Agent Triggers
      if any(kw in goal for kw in ["shorten", "summarize", "compress"]):
          agents_to_run.append("CompressionAgent")

      # Style Agent Triggers
      if any(kw in style for kw in ["bullet", "creative", "wise", "structured", "storytelling", "poetic", "academic", "relaxed"]):
          agents_to_run.append("StyleAgent")

      # Fallback: default to GrammarAgent if nothing matches
      if not agents_to_run:
          agents_to_run.append("GrammarAgent")

      return agents_to_run
