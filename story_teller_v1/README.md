# Story Teller v1

This directory contains a more advanced version of the story-writing agent. This version of the agent is designed to create a structured story skeleton, which can then be used to generate a complete story.

## Agent

*   **`agent.py`**: This file defines the `StorySkeletonAgent`, which is a `SequentialAgent`. This agent takes a user-provided topic and generates a story skeleton with a title, key plot points, and character sketches. The story is written in French and is structured into six chapters. The generated story is saved to a `story.txt` file.

## Deployment

*   **`deployment/`**: This directory contains scripts for deploying the `v1` agent.
