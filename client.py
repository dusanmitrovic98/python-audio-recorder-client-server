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
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    print("Streaming audio...")

    while True:
        try:
            data = stream.read(CHUNK)
            client_socket.sendall(data)
        except KeyboardInterrupt:
            break

    print("Streaming finished.")

    client_socket.close()
    stream.stop_stream()
