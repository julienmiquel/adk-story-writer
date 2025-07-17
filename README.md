# ADK Story Writer Tutorial

This repository contains a story-writing agent that uses the Google Generative AI ADK (Agent Development Kit) to generate stories based on user input. This project is presented as a tutorial to demonstrate the capabilities of the ADK.

## Project Overview

The project consists of two versions of a story-writing agent:

*   **v0:** A simplified version of the agent.
*   **v1:** A more advanced version of the agent that creates a structured story skeleton.

## Features

*   **Story Generation:** Creates a story skeleton based on a user-defined topic.
*   **Gemini 2.0 Flash Model:** Utilizes the Gemini 2.0 Flash model for text generation.
*   **French Language:** The generated stories are in French.
*   **Structured Output:** The story is organized into a title, plot points, character sketches, and six chapters.
*   **File Output:** The generated story is saved to a `story.txt` file.

## How it Works

The `agent.py` file in each version's directory defines the agent. The `v0` agent is a simple agent, while the `v1` agent is a `SequentialAgent` that performs multiple steps to create a story.

## Getting Started

To run the agents, you will need to have the Google Generative AI ADK installed. It is recommended to use a virtual environment to manage dependencies.

### Setup

1.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
    ```

2.  **Install the dependencies for the desired version:**

    For `v0`:

    ```bash
    pip install -r story_teller_v0/requirements.txt
    ```

    For `v1`:

    ```bash
    pip install -r story_teller_v1/requirements.txt
    ```

### Running the Agent

You can then execute the `agent.py` file in either the `story_teller_v0` or `story_teller_v1` directory to start the story generation process.

**Note:** This project is an example of how to use the Google Generative AI ADK and may require further development to be used in a a production environment.