from app.insights import extract_insights


def test_extracts_decisions_and_actions():
    text = "We agreed to ship Friday.\nAction: Priya will update the API docs.\nThe team reviewed the release."
    result = extract_insights(text)
    assert result.decisions
    assert result.action_items[0]["task"] == "Priya will update the API docs."
    assert result.summary.startswith("We agreed")
