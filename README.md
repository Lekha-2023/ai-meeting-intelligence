# AI Meeting Intelligence

A meeting-processing pipeline that transforms speech transcripts into structured notes, decisions, and action items. It separates speech recognition from downstream business logic so the application can swap ASR providers without redesigning the pipeline.

## Pipeline

```text
Audio -> ASR Adapter -> Transcript Segments -> Insight Extraction
                                             |-> Summary
                                             |-> Decisions
                                             `-> Action Items
```

## Engineering features

- Provider-neutral transcription interface
- Whisper-compatible ASR adapter
- Timestamp/speaker-aware transcript model
- Structured decision and action-item extraction
- JSON-friendly output for downstream workflow systems
- Deterministic local tests without API credentials

## Run

```bash
pip install -e '.[dev]'
python -m app.pipeline
pytest -q
```

The default tests use text transcripts. Configure an actual ASR client only when running audio ingestion.
