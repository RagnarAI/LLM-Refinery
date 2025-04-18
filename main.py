from LLM_Refinery.core.agent_pipeline import run_pipeline

def get_user_input():
    print("=== Welcome to the LLM Refinery Interface ===")
    print("Customize how you'd like the model to behave:\n")

    user_prompt = input("Enter your raw text or prompt:\n> ")

    goal = input("\nGoal? (e.g., summarize, clarify, rewrite, professional tone):\n> ")
    tone = input("Tone? (e.g., formal, casual, assertive):\n> ")
    style = input("Style? (e.g., academic, creative, bullet points):\n> ")
    character = input("Persona? (e.g., teacher, lawyer, CEO):\n> ")
    domain = input("Domain? (e.g., marketing, legal, business):\n> ")

    return {
        "original_input": user_prompt,
        "goal": goal,
        "tone": tone,
        "style": style,
        "character": character,
        "domain": domain
    }

if __name__ == "__main__":
    while True:
        user_config = get_user_input()
        response, evaluation, feedback = run_pipeline(user_config)

        print("\n=== Final Output ===\n")
        print(response)

        print("\n=== Evaluation ===")
        print(evaluation)

        print("\n=== Proxy Agent Feedback ===")
        print(feedback)

        again = input("\nWould you like to run another task? (y/n): ")
        if again.lower() != "y":
            print("\nGoodbye 👋")
            break


