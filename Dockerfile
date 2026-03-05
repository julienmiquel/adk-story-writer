# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Copy requirements from all agents
COPY story_teller_v0/requirements.txt requirements_v0.txt
COPY story_teller_v1/requirements.txt requirements_v1.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements_v0.txt -r requirements_v1.txt google-adk uvicorn fastapi

# Copy the current directory contents into the container at /app
COPY . /app

# Run adk web when the container launches
# Using shell form to allow variable expansion if needed, though usually Cloud Run passes PORT env var.
# We assume adk web accepts --host and --port or respects PORT env var.
# If adk web uses uvicorn under the hood, we might need to invoke it differently if it doesn't expose args.
# But assuming standard behavior for now.
CMD adk web --host 0.0.0.0 --port ${PORT:-8080}
