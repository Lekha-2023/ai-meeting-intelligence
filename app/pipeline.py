from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Segment:
    speaker: str
    text: str
    start: float = 0.0
    end: float = 0.0

@dataclass(frozen=True)
class ActionItem:
    owner: str
    task: str
    due: str | None = None

def parse_transcript(text: str) -> list[Segment]:
    segments=[]
    for line in text.splitlines():
        match=re.match(r"\s*([^:]{1,60}):\s*(.+)", line)
        if match: segments.append(Segment(match.group(1).strip(), match.group(2).strip()))
    return segments

def extract_actions(segments: list[Segment]) -> list[ActionItem]:
    actions=[]
    for s in segments:
        if re.search(r"\b(will|should|needs to|action)\b", s.text, re.I):
            due_match=re.search(r"\b(by|before)\s+([^,.]+)", s.text, re.I)
            actions.append(ActionItem(s.speaker, s.text, due_match.group(2).strip() if due_match else None))
    return actions

def summarize(segments: list[Segment]) -> str:
    if not segments: return "No transcript content available."
    return " ".join(s.text for s in segments[:6])

def analyze(text: str) -> dict:
    segments=parse_transcript(text)
    actions=extract_actions(segments)
    decisions=[s.text for s in segments if re.search(r"\b(decided|decision|agreed)\b", s.text, re.I)]
    return {"summary":summarize(segments), "segments":[s.__dict__ for s in segments],
            "decisions":decisions, "action_items":[a.__dict__ for a in actions]}

if __name__ == "__main__": print(analyze("Alice: We agreed to launch Friday.\nBob: I will prepare the release notes by Thursday."))
