import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SERVER_IP = "localhost"  # Replace with your PC's IP address
SERVER_PORT = 12345

def send_audio():
    p = pyaudio.PyAudio()
