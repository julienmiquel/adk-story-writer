
from google.adk.agents import Agent, SequentialAgent
from .config import TEXT_MODEL_NAME
from .tools import generate_image_tool, upscale_image_tool

# Agent to generate image
image_generation_agent = Agent(
    name="ImageGenerationAgent",
    model=TEXT_MODEL_NAME,
    instruction=(
        "You are an expert digital artist. Your goal is to generate an image "
        "based on the user's request. You MUST use the `generate_image` tool "
        "to create the image. The tool returns the path of the generated image. "
        "You should return this path as your answer."
    ),
    tools=[generate_image_tool],
    output_key="image_path"
)

# Agent to upscale image
image_upscaling_agent = Agent(
    name="ImageUpscalingAgent",
    model=TEXT_MODEL_NAME,
    instruction=(
        "You are an image enhancement specialist. You will find a path to an "
        "image in the previous steps output or context. You MUST use the "
        "`upscale_image` tool to upscale this image. "
        "The tool returns the path of the upscaled image. "
        "You should return this path as your final answer."
    ),
    tools=[upscale_image_tool],
    output_key="upscaled_image_path"
)

# Sequential agent
image_pipeline_agent = SequentialAgent(
    name="ImagePipelineAgent",
    description="Generates an image and then upscales it.",
    sub_agents=[image_generation_agent, image_upscaling_agent]
)

if __name__ == "__main__":
    import asyncio
    from google.adk.models import LlmResponse

    # Simple runner to demonstrate usage if executed directly
    print("This agent is designed to be run via ADK runner or integrated into an app.")
    print("Example invocation logic (pseudo-code):")
    print("  agent.run(prompt='A futuristic city skyline')")
