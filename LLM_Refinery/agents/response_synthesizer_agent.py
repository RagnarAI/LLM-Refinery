class ResponseSynthesizerAgent:
  def __init__(self):
      self.name = "ResponseSynthesizerAgent"

  def run(self, revised_versions: list[str]) -> str:
      # Simple merge logic — prioritize last agent's version
      return revised_versions[-1] if revised_versions else ""
