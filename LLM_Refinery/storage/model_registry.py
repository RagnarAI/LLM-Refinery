class ModelRegistry:
  def __init__(self):
      self.models = {}

  def register_model(self, version_name: str, metadata: dict):
      self.models[version_name] = metadata

  def get_model(self, version_name: str) -> dict:
      return self.models.get(version_name, {})

  def list_versions(self) -> dict:
      return self.models
