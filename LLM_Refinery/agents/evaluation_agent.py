class EvaluationAgent:
  def __init__(self):
      self.name = "EvaluationAgent"

  def run(self, original: str, refined: str, goal: str) -> dict:
      if original != refined:
          score = 8.5  # Placeholder scoring logic
          passed = True
      else:
          score = 5.0
          passed = False
      return {
          "score": score,
          "passed": passed,
          "goal_matched": goal in refined
      }
