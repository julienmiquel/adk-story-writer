# ADK Story Writer

This repository contains a story-writing agent that uses the Google Generative AI ADK (Agent Development Kit) to generate stories based on user input.

## Project Overview

The project consists of a single agent, the "StorySkeletonAgent," which is designed to create a compelling story skeleton. The agent takes a user-provided topic and generates a story with a title, key plot points, and character sketches. The story is written in French and is structured into six chapters.

## Features

*   **Story Generation:** Creates a story skeleton based on a user-defined topic.
*   **Gemini 2.0 Flash Model:** Utilizes the Gemini 2.0 Flash model for text generation.
*   **French Language:** The generated stories are in French.
*   **Structured Output:** The story is organized into a title, plot points, character sketches, and six chapters.
*   **File Output:** The generated story is saved to a `story.txt` file.

## How it Works

The `agent.py` file defines the `StorySkeletonAgent`. This agent is a `SequentialAgent` that performs the following steps:

1.  **Receives a Topic:** The agent takes a topic from the user as input.
2.  **Generates a Story Skeleton:** It uses the Gemini 2.0 Flash model to generate a story skeleton, including a title, plot points, and character sketches.
3.  **Saves the Story:** The generated story is saved to a `story.txt` file.

## Getting Started

To run the agent, you will need to have the Google Generative AI ADK installed. You can then execute the `agent.py` file to start the story generation process.

**Note:** This project is an example of how to use the Google Generative AI ADK and may require further development to be used in a production environment.