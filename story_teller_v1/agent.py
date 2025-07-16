from google.adk.agents import Agent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse

MODEL_NAME = "gemini-2.0-flash-001"

def _save_story_part(
    callback_context: CallbackContext,
    llm_response: LlmResponse,
) -> LlmResponse:
    if not llm_response.content or not llm_response.content.parts:
        return llm_response

    for idx, part in enumerate(llm_response.content.parts):
        try:
            filename = f"./story-{callback_context.agent_name}-{idx}.txt"
            print(f"Save story: {filename}")
            print(f"Save part: {part.text}")
            
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"{part.text}")
            print(f"Successfully saved text to '{filename}'")
        except IOError as e:
            print(f"Error saving file '{filename}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
    return llm_response

# --- AGENT DEFINITIONS ---

# 1. The Architect: Builds the initial story skeleton.
story_skeleton_agent = Agent(
    name="StorySkeletonAgent",
    model=MODEL_NAME,
    instruction="You are a master storyteller and architect. Based on the user's topic, found in the session state under the key 'topic', create a compelling story skeleton, including a title, key plot points, and character sketches. You create wonderfull story in French in 6 chapters.",
    output_key="story_skeleton",
    after_model_callback=_save_story_part
)

# --- AGENT ASSEMBLY ---

# The Root Agent that starts the entire process.
# It first creates the skeleton, then hands off to the creative loop.
root_agent = SequentialAgent(
    name="SimpleStoryGenerator",
    description="The main agent that orchestrates the entire story generation from topic to finished product.",
    sub_agents=[story_skeleton_agent],
)
