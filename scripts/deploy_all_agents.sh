#!/bin/bash
set -e

PROJECT_ID=$1
LOCATION=$2
STAGING_BUCKET=$3

if [ -z "$PROJECT_ID" ] || [ -z "$LOCATION" ] || [ -z "$STAGING_BUCKET" ]; then
    echo "Usage: $0 <project_id> <location> <staging_bucket>"
    exit 1
fi

# List of agents to deploy
AGENTS=("story_teller_v0" "story_teller_v1")

for AGENT_DIR in "${AGENTS[@]}"; do
    echo "Deploying $AGENT_DIR..."
    python3 scripts/deploy_agent.py \
        --project-id "$PROJECT_ID" \
        --location "$LOCATION" \
        --staging-bucket "$STAGING_BUCKET" \
        --agent-dir "$AGENT_DIR" \
        --agent-name "$AGENT_DIR"
done

echo "All agents deployed."
