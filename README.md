# AI Meeting Intelligence

A meeting-processing pipeline that transforms a transcript into structured notes, decisions, and action items. It is designed around a provider-neutral transcription interface so Whisper or another speech-to-text service can be integrated without coupling the business logic to a vendor.

## Pipeline

`Audio -> Transcription -> Segmentation -> Summary -> Decisions + Action Items`

## Highlights

- Transcript normalization and segment timestamps
- Topic/decision extraction
- Action-item detection with owner and due-date fields when present
- Structured JSON output for downstream systems
- Testable local pipeline with no API keys required

## Run

```bash
pip install -e '.[dev]'
python -m app.pipeline
pytest -q
```

The repository intentionally keeps speech recognition behind an adapter boundary. This makes it easy to connect OpenAI Whisper or another ASR provider later while keeping tests deterministic.
