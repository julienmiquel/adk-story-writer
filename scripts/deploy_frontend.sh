#!/bin/bash
set -e

SERVICE_NAME=${1:-adk-agent-frontend}
REGION=${2:-us-central1}

echo "Deploying $SERVICE_NAME to Cloud Run in region $REGION..."

# Build and deploy using the Dockerfile in the current directory
gcloud run deploy "$SERVICE_NAME" \
  --source . \
  --region "$REGION" \
  --allow-unauthenticated

echo "Deployment complete."
