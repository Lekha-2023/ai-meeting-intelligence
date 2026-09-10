from app.pipeline import parse_transcript, extract_actions, analyze

def test_parse_transcript():
    segments=parse_transcript("Alice: Hello\nBob: I will send the report by Friday")
    assert len(segments)==2
    assert segments[0].speaker=="Alice"

def test_actions_include_owner_and_due_date():
    result=analyze("Bob: I will send the report by Friday")
    assert result["action_items"][0]["owner"]=="Bob"
    assert result["action_items"][0]["due"]=="Friday"
