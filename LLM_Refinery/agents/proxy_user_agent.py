class ProxyUserAgent:
  def __init__(self):
      self.name = "ProxyUserAgent"

  def run(self, evaluation: dict) -> dict:
      approved = evaluation.get("passed", False) and evaluation.get("score", 0) > 7
      feedback = "Approved" if approved else "Needs revision"
      return {
          "approved": approved,
          "feedback": feedback
      }
