class StyleAgent:
  def __init__(self):
      self.name = "StyleAgent"

  def run(self, text: str) -> str:
      # Converts to a bullet-point structure for business-style outputs
      if "first," in text:
          text = text.replace("first,", "- First:")
      if "second," in text:
          text = text.replace("second,", "- Second:")
      return text
