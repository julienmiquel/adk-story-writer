import pytest
from google.adk.evaluation.agent_evaluator import AgentEvaluator
from google.adk.evaluation.eval_config import EvalConfig

@pytest.mark.asyncio
async def test_agent_eval():
    """Evaluate the agent using the ADK evaluator."""
    await AgentEvaluator.evaluate(
        agent_module="story_teller_v0.agent",
        eval_dataset_file_path_or_dir="tests/eval_dataset.test.json",
    )
