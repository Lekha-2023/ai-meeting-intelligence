from dataclasses import dataclass, field
import re


@dataclass
class MeetingInsights:
    summary: str
    decisions: list[str] = field(default_factory=list)
    action_items: list[dict[str, str]] = field(default_factory=list)


def extract_insights(transcript: str) -> MeetingInsights:
    lines = [x.strip() for x in transcript.splitlines() if x.strip()]
    decisions = [x for x in lines if re.search(r"\b(decided|decision|agreed)\b", x, re.I)]
    actions: list[dict[str, str]] = []
    for line in lines:
        match = re.search(r"(?:action|todo|follow up)[:\- ]+(.*)", line, re.I)
        if match:
            actions.append({"task": match.group(1).strip()})
    summary = " ".join(lines[:3])
    return MeetingInsights(summary=summary, decisions=decisions, action_items=actions)
