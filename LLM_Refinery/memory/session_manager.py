class SessionManager:
  def __init__(self):
      self.sessions = {}

  def create_session(self, session_id: str):
      if session_id not in self.sessions:
          self.sessions[session_id] = {
              "history": [],
              "user_profile": {}
          }

  def log_interaction(self, session_id: str, input_text: str, output_text: str):
      if session_id in self.sessions:
          self.sessions[session_id]["history"].append({
              "input": input_text,
              "output": output_text
          })

  def update_profile(self, session_id: str, profile: dict):
      if session_id in self.sessions:
          self.sessions[session_id]["user_profile"].update(profile)

  def get_session(self, session_id: str) -> dict:
      return self.sessions.get(session_id, {})
