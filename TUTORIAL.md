# Tutorial: Creating an Image Generation and Upscaling Agent with Google ADK

This tutorial guides you through creating a Google ADK (Agent Development Kit) agent that generates an image using the Gemini 3 image model (Imagen 3) and upscales it using the Imagen model.

## Prerequisites

*   Python 3.10+
*   Google Cloud Project with Vertex AI enabled OR Google AI Studio API Key.
*   `google-adk`, `google-genai` libraries installed.

## Step 1: Project Setup

Create a new directory for your agent, for example, `image_agent`.

```bash
mkdir image_agent
cd image_agent
```

## Step 2: Configuration

Create a `config.py` file to store your model names and configuration.

```python
# image_agent/config.py

# Text generation model for the agent (Gemini 2.0 Flash)
TEXT_MODEL_NAME = "gemini-2.0-flash-001"

# Image generation model (Imagen 3)
IMAGE_GENERATION_MODEL = "imagen-3.0-generate-001"

# Image upscaling model (Imagen 2 Upscale)
IMAGE_UPSCALING_MODEL = "imagen-2.0-upscale-001"

# Output directory for images
OUTPUT_DIR = "./output_images"
```

## Step 3: Define Tools

We need two tools: one for generating images and one for upscaling them. We'll use the `google.genai` SDK to interact with the models. Create `image_agent/tools.py`.

```python
# image_agent/tools.py
import os
from google import genai
from google.genai import types
from google.adk.tools import FunctionTool
from .config import IMAGE_GENERATION_MODEL, IMAGE_UPSCALING_MODEL, OUTPUT_DIR

def _get_client():
    """Returns a GenAI client."""
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")

    if project:
        return genai.Client(vertexai=True, project=project, location=location)
    else:
        return genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

def generate_image(prompt: str) -> str:
    """Generates an image based on the prompt."""
    print(f"Generating image for prompt: {prompt}")
    try:
        client = _get_client()
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        response = client.models.generate_images(
            model=IMAGE_GENERATION_MODEL,
            prompt=prompt,
            config=types.GenerateImagesConfig(number_of_images=1)
        )

        if not response.generated_images:
            return "Error: No image generated."

        image_data = response.generated_images[0].image.image_bytes
        filename = os.path.join(OUTPUT_DIR, "generated_image.png") # simplified name

        with open(filename, "wb") as f:
            f.write(image_data)

        return filename
    except Exception as e:
        return f"Error: {e}"

def upscale_image(image_path: str) -> str:
    """Upscales an image."""
    print(f"Upscaling image: {image_path}")
    try:
        client = _get_client()
        with open(image_path, "rb") as f:
            image_bytes = f.read()

        response = client.models.upscale_image(
            model=IMAGE_UPSCALING_MODEL,
            image=types.Image(image_bytes=image_bytes),
            upscale_factor="x2"
        )

        if not response.generated_images:
             return "Error: No upscaled image returned."

        upscaled_data = response.generated_images[0].image.image_bytes
        new_filename = image_path.replace(".png", "_upscaled.png")

        with open(new_filename, "wb") as f:
            f.write(upscaled_data)

        return new_filename
    except Exception as e:
        return f"Error: {e}"

# Wrap tools
generate_image_tool = FunctionTool(generate_image)
upscale_image_tool = FunctionTool(upscale_image)
```

## Step 4: Define the Agents

Now, create `image_agent/agent.py` to define the agents and chain them together.

```python
# image_agent/agent.py
from google.adk.agents import Agent, SequentialAgent
from .config import TEXT_MODEL_NAME
from .tools import generate_image_tool, upscale_image_tool

# Agent 1: Generates the image
image_generation_agent = Agent(
    name="ImageGenerationAgent",
    model=TEXT_MODEL_NAME,
    instruction=(
        "You are an expert digital artist. Generate an image based on the user's request "
        "using the `generate_image` tool. Return the file path."
    ),
    tools=[generate_image_tool],
    output_key="image_path"
)

# Agent 2: Upscales the image
image_upscaling_agent = Agent(
    name="ImageUpscalingAgent",
    model=TEXT_MODEL_NAME,
    instruction=(
        "You are an image enhancement specialist. Upscale the image found in the previous step "
        "using the `upscale_image` tool. Return the upscaled file path."
    ),
    tools=[upscale_image_tool],
    output_key="upscaled_image_path"
)

# Sequential Agent: Pipelines the process
image_pipeline_agent = SequentialAgent(
    name="ImagePipelineAgent",
    description="Generates an image and then upscales it.",
    sub_agents=[image_generation_agent, image_upscaling_agent]
)
```

## Step 5: Running the Agent

You can run this agent using the ADK web interface or by integrating it into your application.

1.  **Set Environment Variables:**
    ```bash
    export GOOGLE_API_KEY="your-api-key"
    # OR
    export GOOGLE_CLOUD_PROJECT="your-project-id"
    export GOOGLE_CLOUD_LOCATION="us-central1"
    ```

2.  **Run with ADK Web:**
    (Assuming `image_agent` is in your python path or configured in ADK)
    ```bash
    adk web
    ```
    Then select the `ImagePipelineAgent`.

## Conclusion

You have successfully created a multi-step agent using Google ADK that leverages Gemini/Imagen models for image generation and upscaling.
