# Speech-to-Text (Python)

A small command-line prototype that captures speech from the microphone and prints the transcription.

## How it works

- `speech_recognition.Microphone` captures audio. Microphone access requires **PyAudio** to be installed.
- The audio is transcribed with Google's online Web Speech API via `recognize_google()`, so an **internet connection is required**. This is not an offline speech model.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

On macOS, PyAudio may first need PortAudio, for example:

```bash
brew install portaudio
```

## Run

```bash
python speech_to_text.py
```

Then speak when prompted. The script prints what it heard, or a clear error if the speech was not understood, the service could not be reached, or no microphone was available.

## Limitations

- Single utterance per run; no continuous listening, no saved transcript file.
- Accuracy depends on microphone quality and background noise.
- No offline mode.
