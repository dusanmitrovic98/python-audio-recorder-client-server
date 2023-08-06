import socket
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"

