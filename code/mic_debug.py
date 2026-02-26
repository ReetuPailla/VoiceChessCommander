# mic_debug.py
# Debugging tool for microphone + SpeechRecognition (Windows)
# Save and run: python mic_debug.py

import speech_recognition as sr
import wave
import sys
import time
import math
import os

def list_mics():
    print("Available microphones:")
    names = sr.Microphone.list_microphone_names()
    for i, n in enumerate(names):
        print(f"  {i}: {n}")
    return names

def save_wav(filename, sample_rate, audio_data):
    # audio_data is an instance of sr.AudioData
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)  # SpeechRecognition provides mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.get_wav_data())

def show_energy_levels(recognizer, source, duration=3.0):
    """
    Listen to small chunks and print RMS energy levels for duration seconds.
    Useful to see whether the mic picks up your voice.
    """
    print("\n--- Showing short live energy levels (speak loudly now) ---")
    start = time.time()
    seconds = duration
    chunk = source.CHUNK
    sample_rate = source.SAMPLE_RATE
    frames_needed = int(sample_rate / chunk * seconds)
    # We'll read frames by using source.stream.read in a safe loop
    try:
        for i in range(frames_needed):
            data = source.stream.read(chunk, exception_on_overflow=False)
            # compute RMS
            if not data:
                rms = 0.0
            else:
                # 16-bit signed little-endian
                count = len(data) // 2
                format = "%dh" % count
                import struct
                shorts = struct.unpack(format, data)
                sum_squares = 0.0
                for s in shorts:
                    n = s / 32768.0
                    sum_squares += n * n
                rms = math.sqrt(sum_squares / count) if count else 0.0
            bar = "#" * int(rms * 60)
            print(f"{rms:0.4f} {bar}")
            time.sleep(0.01)
    except Exception as e:
        print("[Energy] Exception while reading stream:", e)
    print("--- End energy levels ---\n")

def test_capture(recognizer, device_index, sample_rate, chunk_size, dynamic_energy, energy_threshold):
    print("\n== Starting capture test ==")
    try:
        with sr.Microphone(device_index=device_index,
                           sample_rate=sample_rate,
                           chunk_size=chunk_size) as source:
            print(f"Microphone opened: device_index={device_index}, sample_rate={source.SAMPLE_RATE}, chunk_size={source.CHUNK}")
            recognizer.dynamic_energy_threshold = dynamic_energy
            if not dynamic_energy:
                recognizer.energy_threshold = energy_threshold
                print(f"Set fixed energy_threshold = {recognizer.energy_threshold}")
            else:
                print(f"Using dynamic_energy_threshold = True (initial threshold {recognizer.energy_threshold})")

            # show live energy levels for a few seconds so you can speak
            show_energy_levels(recognizer, source, duration=2.5)

            print("Calibrating (adjust_for_ambient_noise)...")
            recognizer.adjust_for_ambient_noise(source, duration=1.0)
            print("Calibration complete. energy_threshold =", recognizer.energy_threshold)

            print("Now recording (listen and speak a short phrase).")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recording complete.")
    except Exception as e:
        print("Error opening microphone or during recording:", e)
        return None

    # Save the captured audio to a WAV to play back
    outname = "debug_capture.wav"
    try:
        save_wav(outname, sample_rate, audio)
        print(f"Saved captured audio to: {outname}  (play this file in Windows to confirm)")
        print("Captured frames length:", len(audio.frame_data))
    except Exception as e:
        print("Failed to save WAV:", e)

    # Try recognition
    try:
        print("Sending to Google Speech Recognition...")
        text = recognizer.recognize_google(audio)
        print("Google recognized:", text)
    except sr.UnknownValueError:
        print("Google could not understand the audio (UnknownValueError).")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("Recognition error:", e)

    return audio

def interactive():
    names = list_mics()
    if len(names) == 0:
        print("No microphones found by speech_recognition. Make sure your device is connected.")
        return

    # Suggest default index 1 if present
    default_index = 1 if len(names) > 1 else 0
    try:
        device_index = int(input(f"\nEnter mic index to test [default {default_index}]: ") or default_index)
    except ValueError:
        device_index = default_index

    # advanced params
    try:
        sample_rate = int(input("Enter sample_rate for Microphone (e.g., 16000 or press Enter for 16000): ") or 16000)
    except ValueError:
        sample_rate = 16000
    try:
        chunk_size = int(input("Enter chunk_size (frames per buffer) [default 1024]: ") or 1024)
    except ValueError:
        chunk_size = 1024

    dyn = input("Use dynamic_energy_threshold? (y/n) [y]: ") or "y"
    dynamic_energy = dyn.strip().lower().startswith("y")

    energy_threshold = 300
    if not dynamic_energy:
        try:
            energy_threshold = int(input("Set energy_threshold (e.g. 200-800) [300]: ") or 300)
        except ValueError:
            energy_threshold = 300

    print("\nStarting mic test with these settings:")
    print(f" device_index={device_index}, sample_rate={sample_rate}, chunk_size={chunk_size}, dynamic_energy={dynamic_energy}, energy_threshold={energy_threshold}")
    print("Speak clearly after the prompts. You will get a saved WAV 'debug_capture.wav' to play back.")

    test_capture(sr.Recognizer(), device_index, sample_rate, chunk_size, dynamic_energy, energy_threshold)

if __name__ == "__main__":
    print("MIC DEBUG TOOL - speech_recognition")
    interactive()
    print("\nDone. If the WAV file is empty or you still see zero energy levels, try different device_index or sample_rate.")
