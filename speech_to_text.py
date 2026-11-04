"""Speech-to-Text (Python).

A small command-line prototype: capture speech from the microphone and
print the transcription.

How it works
------------
- `speech_recognition.Microphone` captures audio. Microphone access in
  SpeechRecognition requires PyAudio to be installed (see requirements.txt).
- The audio is sent to Google's online Web Speech API through
  `recognizer.recognize_google()`, so an internet connection is required.
  This is not an offline speech model.

Run
---
    python speech_to_text.py
"""

import speech_recognition as sr


def main() -> None:
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Speak something...")
            # Calibrate for ambient noise for about one second.
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        print("You said:", text)

    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as error:
        print(f"Speech service error (check your internet connection): {error}")
    except OSError as error:
        # No microphone found, microphone busy, or PyAudio is missing.
        print(f"Microphone/audio device error: {error}")
        print("Make sure a microphone is connected and PyAudio is installed.")


if __name__ == "__main__":
    main()
