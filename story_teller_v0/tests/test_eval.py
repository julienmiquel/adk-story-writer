from google.adk.evaluation.agent_evaluator import AgentEvaluator
from google.adk.evaluation.eval_set import EvalSet
from google.adk.evaluation.eval_config import EvalConfig
from google.adk.evaluation.eval_case import EvalCase, Invocation, SessionInput
from google.adk.evaluation.eval_rubrics import Rubric, RubricContent
from google.genai import types as genai_types
import asyncio

async def main():
    eval_set = EvalSet(
        eval_set_id="test_eval",
        name="Story Teller Evals",
        eval_cases=[
            EvalCase(
                eval_id="cat_story",
                conversation=[
                    Invocation(
                        user_content=genai_types.Content(parts=[genai_types.Part.from_text(text="Generate a short story about a cat.")]),
                    )
                ],
                rubrics=[
                    Rubric(
                        rubric_id="rubric_1",
                        rubric_content=RubricContent(text_property="The story should be about a cat.")
                    )
                ],
                session_input=SessionInput(app_name="story", user_id="1", state={"topic": "A cat who wants to go to space"})
            )
        ]
    )

    await AgentEvaluator.evaluate_eval_set(
        agent_module="story_teller_v0.agent",
        eval_set=eval_set,
        eval_config=EvalConfig(),
        num_runs=1
    )

if __name__ == "__main__":
    asyncio.run(main())
