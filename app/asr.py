from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class TranscriptSegment:
    start: float
    end: float
    speaker: str
    text: str


class Transcriber(Protocol):
    def transcribe(self, audio_path: str) -> list[TranscriptSegment]: ...


class WhisperTranscriber:
    """Adapter boundary for a Whisper-compatible ASR provider."""

    def __init__(self, client):
        self.client = client

    def transcribe(self, audio_path: str) -> list[TranscriptSegment]:
        with open(audio_path, "rb") as audio:
            response = self.client.audio.transcriptions.create(model="whisper-1", file=audio)
        text = getattr(response, "text", str(response))
        return [TranscriptSegment(0.0, 0.0, "unknown", text)]
