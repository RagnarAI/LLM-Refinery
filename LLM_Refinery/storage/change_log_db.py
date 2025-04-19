import uuid
import json
import os
from datetime import datetime

class ChangeLogDB:
    def __init__(self, path="LLM_Refinery/storage/changelog.json"):
        self.path = path
        self.logs = self._load()

    def _load(self) -> dict:
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return {}

    def _save(self):
        with open(self.path, "w") as f:
            json.dump(self.logs, f, indent=4)

    def log_change(self, session_id: str, input_text: str, output_text: str,
                   agents_used: list, evaluation_score: float, approved: bool) -> str:
        entry_id = str(uuid.uuid4())
        self.logs[entry_id] = {
            "timestamp": datetime.utcnow().isoformat(),
            "session_id": session_id,
            "input": input_text,
            "output": output_text,
            "agents": agents_used,
            "evaluation_score": evaluation_score,
            "approved": approved
        }
        self._save()
        return entry_id

    def get_log(self, entry_id: str) -> dict:
        return self.logs.get(entry_id, {})

    def list_all(self) -> dict:
        return self.logs
