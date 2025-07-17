"""This module defines the StoryAgent."""

from google.adk.agents import Agent
from config import MODEL_NAME

root_agent: Agent = Agent(
    name="StoryAgent",
    model=MODEL_NAME,
    instruction=(
        "You are a master storyteller. Based on the user's topic, create a "
        "compelling story in French."
    ),
)
