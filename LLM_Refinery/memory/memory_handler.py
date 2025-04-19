class MemoryHandler:
  def __init__(self):
      self.global_memory = {}

  def store(self, key: str, value: any):
      self.global_memory[key] = value

  def retrieve(self, key: str) -> any:
      return self.global_memory.get(key, None)

  def all_memory(self) -> dict:
      return self.global_memory
