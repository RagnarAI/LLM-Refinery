import sys
import os

# Make sure the root LLM_Refinery folder is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from LLM_Refinery.storage.change_log_db import ChangeLogDB

def display_log_entry(log):
    print("\n=== Log Entry ===")
    print(f"🕒 Timestamp   : {log.get('timestamp')}")
    print(f"🆔 Session ID  : {log.get('session_id')}")
    print(f"🧠 Agents Used : {', '.join(log.get('agents', []))}")
    print(f"📊 Evaluation  : {log.get('evaluation_score')}")
    print(f"✅ Approved?   : {'✅ Yes' if log.get('approved') else '❌ No'}")

    print("\n--- 📝 Input ---")
    print(log.get("input", ""))

    print("\n--- 📤 Output ---")
    print(log.get("output", ""))
    print("\n")

def main():
    log_db = ChangeLogDB()
    logs = log_db.list_all()

    if not logs:
        print("📭 No logs found.")
        return

    log_ids = list(logs.keys())
    print("🧠 Refinery Logs:")
    for i, log_id in enumerate(log_ids):
        print(f"[{i}] Log ID: {log_id}")

    choice = input("\nSelect a log number to view (or press Enter to quit): ")
    if choice.strip().isdigit():
        index = int(choice)
        if 0 <= index < len(log_ids):
            selected_log = logs[log_ids[index]]
            display_log_entry(selected_log)
        else:
            print("❌ Invalid selection.")
    else:
        print("👋 Exiting viewer.")

if __name__ == "__main__":
    main()
