from google.adk.agents import Agent

MODEL_NAME = "gemini-2.0-flash-001"

root_agent = Agent(
    name="StoryAgent",
    model=MODEL_NAME,
    instruction="You are a master storyteller. Based on the user's topic, create a compelling story in French.",
)
