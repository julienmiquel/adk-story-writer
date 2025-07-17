from story_teller_v1.agent import root_agent


def test_root_agent_name():
    """Test the root agent's name."""
    assert root_agent.name == "SimpleStoryGenerator"
