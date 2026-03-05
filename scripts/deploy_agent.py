import argparse
import vertexai
from vertexai.preview import reasoning_engines

def deploy_agent(project_id, location, staging_bucket, agent_dir, agent_name, entrypoint_object="root_agent"):
    vertexai.init(project=project_id, location=location, staging_bucket=staging_bucket)

    print(f"Deploying agent from {agent_dir}...")

    # Define source packages (agent directory and config.py)
    # config.py is included because agents import from it.
    source_packages = [agent_dir, "config.py"]

    # Entry point
    entrypoint_module = f"{agent_dir}.agent"

    # Requirements file
    requirements_file = f"{agent_dir}/requirements.txt"

    remote_agent = reasoning_engines.ReasoningEngine.create(
        source_packages=source_packages,
        entrypoint_module=entrypoint_module,
        entrypoint_object=entrypoint_object,
        requirements_file=requirements_file,
        display_name=agent_name,
        description=f"Agent deployed from {agent_dir}",
    )

    print(f"Agent deployed successfully!")
    print(f"Resource Name: {remote_agent.resource_name}")
    return remote_agent

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy an agent to Vertex AI Agent Engine.")
    parser.add_argument("--project-id", required=True, help="Google Cloud Project ID")
    parser.add_argument("--location", required=True, help="Google Cloud Region (e.g., us-central1)")
    parser.add_argument("--staging-bucket", required=True, help="GCS bucket for staging artifacts (e.g., gs://my-bucket)")
    parser.add_argument("--agent-dir", required=True, help="Directory containing the agent code (e.g., story_teller_v0)")
    parser.add_argument("--agent-name", required=True, help="Display name for the agent")
    parser.add_argument("--entrypoint-object", default="root_agent", help="Name of the agent object in agent.py (default: root_agent)")

    args = parser.parse_args()

    deploy_agent(
        args.project_id,
        args.location,
        args.staging_bucket,
        args.agent_dir,
        args.agent_name,
        args.entrypoint_object
    )
