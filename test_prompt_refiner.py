from LLM_Refinery.agents.prompt_refiner_agent import PromptRefinerAgent

# Fake input like the user would give via the UI
test_input = {
    "goal": "make it more persuasive",
    "domain": "marketing",
    "context": {
        "tone": "motivational",
        "style": "conversational",
        "persona": "influencer"
    },
    "original_input": "This product is good."
}

# Create the agent and run it
agent = PromptRefinerAgent()
result = agent.run(test_input)

# Show the output
print("==== Refined Prompt ====")
print(result)
