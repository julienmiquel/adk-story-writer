import os
import base64
from google import genai
from google.genai import types
from google.adk.tools import FunctionTool
from .config import IMAGE_GENERATION_MODEL, IMAGE_UPSCALING_MODEL, OUTPUT_DIR

def _get_client():
    """Returns a GenAI client."""
    # Attempt to initialize client.
    # It requires API_KEY or VERTEXAI params.
    # We will prioritize Vertex AI if environment variables are set.
    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")

    if project:
        return genai.Client(
            vertexai=True,
            project=project,
            location=location
        )
    else:
        # Fallback to API Key
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
             # If no auth found, let it fail or provide instructions
             # But for tool, we just let it raise error
             pass
        return genai.Client(api_key=api_key)


def generate_image(prompt: str) -> str:
    """Generates an image based on the prompt using Gemini 3 / Imagen 3 model.

    Args:
        prompt: The description of the image to generate.

    Returns:
        The file path of the generated image, or an error message.
    """
    print(f"Generating image for prompt: {prompt}")
    try:
        client = _get_client()

        # Ensure output directory exists
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        response = client.models.generate_images(
            model=IMAGE_GENERATION_MODEL,
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
            )
        )

        if not response.generated_images:
            return "Error: No image generated."

        image = response.generated_images[0]
        # Image bytes
        image_data = image.image.image_bytes

        # Create a filename based on prompt hash or simple counter.
        # Using base64 of prompt start to be somewhat unique but safe
        safe_prompt = "".join([c for c in prompt if c.isalnum()])[:20]
        filename = os.path.join(OUTPUT_DIR, f"gen_{safe_prompt}.png")

        with open(filename, "wb") as f:
            f.write(image_data)

        print(f"Image saved to {filename}")
        return filename

    except Exception as e:
        return f"Error generating image: {e}"


def upscale_image(image_path: str) -> str:
    """Upscales an image using Imagen model.

    Args:
        image_path: The path to the image file to upscale.

    Returns:
        The file path of the upscaled image, or an error message.
    """
    print(f"Upscaling image: {image_path}")
    try:
        client = _get_client()

        if not os.path.exists(image_path):
            return f"Error: File {image_path} does not exist."

        with open(image_path, "rb") as f:
            image_bytes = f.read()

        # Upscale
        # The signature is (model, image, upscale_factor, config) based on inspection
        response = client.models.upscale_image(
            model=IMAGE_UPSCALING_MODEL,
            image=types.Image(image_bytes=image_bytes),
            upscale_factor="x2", # Defaulting to x2
            # config=types.UpscaleImageConfig()
        )

        if not response.generated_images:
             return "Error: No upscaled image returned."

        upscaled_image = response.generated_images[0]
        upscaled_data = upscaled_image.image.image_bytes

        path, ext = os.path.splitext(image_path)
        new_filename = f"{path}_upscaled{ext}"

        with open(new_filename, "wb") as f:
            f.write(upscaled_data)

        print(f"Upscaled image saved to {new_filename}")
        return new_filename

    except Exception as e:
        return f"Error upscaling image: {e}"

# Wrap tools
generate_image_tool = FunctionTool(generate_image)
upscale_image_tool = FunctionTool(upscale_image)
