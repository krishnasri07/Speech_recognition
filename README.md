# Real-Time Speech Recognition

## Overview
This project captures real-time audio, processes it using the Faster Whisper speech recognition model, and transcribes the spoken words. It utilizes `pyaudio` for capturing audio, `numpy` for data processing, and `faster_whisper` for speech-to-text conversion.

## Features
- Real-time audio recording using PyAudio
- Speech-to-text transcription with Faster Whisper
- Supports English language transcription
- Saves recorded audio as a WAV file

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install pyaudio numpy faster-whisper
```

### Additional Requirements
- `portaudio` (for PyAudio, required on some systems)
  - Linux: `sudo apt install portaudio19-dev`
  - MacOS: `brew install portaudio`

## Usage
1. Clone the repository or copy the script.
2. Run the script:

```bash
python speech_recognition.py
```

3. Speak into your microphone, and the transcription will be displayed in real-time.
4. Press `CTRL+C` to stop the program.

## How It Works
- The script captures live audio using `pyaudio`.
- Audio data is stored in a WAV file.
- The Faster Whisper model processes the audio and transcribes speech.
- The transcription is displayed on the console.

## Code Explanation
- `record_audio()`: Captures and saves audio in real time.
- `transcribe_audio()`: Converts the recorded audio into text.
- `while True` loop: Continuously records and transcribes audio until interrupted.

## Notes
- The model runs on CPU by default. For better performance, use a GPU (`device='cuda'`).
- You can adjust the recording duration by modifying `RECORD_SECONDS`.

## License
This project is licensed under the MIT License.
