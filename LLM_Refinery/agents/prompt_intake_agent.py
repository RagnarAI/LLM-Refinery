class PromptIntakeAgent:
  def __init__(self):
      self.name = "PromptIntakeAgent"

  def run(self, user_input: dict) -> dict:
      structured_prompt = {
          "goal": user_input.get("goal", "refine"),
          "domain": user_input.get("domain", "general"),
          "tone": user_input.get("tone", "neutral"),
          "style": user_input.get("style", "default"),
          "character": user_input.get("character", "assistant"),
          "original_input": user_input.get("original_input", "")
      }
      return structured_prompt
