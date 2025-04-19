class CompressionAgent:
  def __init__(self):
      self.name = "CompressionAgent"

  def run(self, text: str) -> str:
      # Basic compression: remove filler words
      fillers = ["just", "really", "basically", "actually"]
      for word in fillers:
          text = text.replace(f" {word} ", " ")
      return text
