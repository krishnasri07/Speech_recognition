import pyaudio
import numpy as np
import wave
from faster_whisper import WhisperModel
import threading

# Set up parameters for real-time audio recording
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1  # Mono audio
RATE = 16000  # Sampling rate (Whisper models typically use 16000 Hz)
CHUNK = 1024  # Number of audio samples per buffer
RECORD_SECONDS = 10  # Duration for each recording chunk (adjust as necessary)

# Initialize Faster Whisper model (using CPU)
model = WhisperModel("small", device="cpu")  # You can use "tiny" for even faster performance on low-end CPUs


def transcribe_audio(audio_data):
    """Function to run Whisper on captured audio"""
    print("Transcribing audio...")
    # Transcribe the real-time audio input
    segments, _ = model.transcribe(audio_data, language="en")  # Change language code if needed
    s = ""
    # Print the transcription results
    for segment in segments:
        print(f"[{segment.start:.2f}s - {segment.end:.2f}s]: {segment.text}")
        # s+=segment
    print(s)


def record_audio(stream, wave_file):
    """Capture audio in real time"""
    print("Recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished.")

    # Save the recorded audio to a WAV file (optional)
    wf = wave.open(wave_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Convert audio frames to NumPy array and normalize for Whisper input
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16).astype(np.float32) / 32768.0
    transcribe_audio(audio_data)


# Initialize PyAudio for real-time audio capture
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Start real-time recording and transcription in a loop
try:
    while True:
        # Run in a separate thread to avoid blocking the main thread
        t = threading.Thread(target=record_audio, args=(stream, "output.wav"))
        t.start()
        t.join()

except KeyboardInterrupt:
    # print(s)
    print("Stopping...")

finally:
    # Close the audio stream
    stream.stop_stream()
    stream.close()
    p.terminate()
