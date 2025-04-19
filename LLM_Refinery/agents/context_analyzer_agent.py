class ContextAnalyzerAgent:
  def __init__(self):
      self.name = "ContextAnalyzerAgent"

  def run(self, structured_prompt: dict) -> dict:
      context = {
          "intent": "refinement",
          "domain": structured_prompt.get("domain", "general"),
          "tone": structured_prompt.get("tone", "neutral"),
          "style": structured_prompt.get("style", "default"),
          "persona": structured_prompt.get("character", "assistant")
      }
      structured_prompt["context"] = context
      return structured_prompt
