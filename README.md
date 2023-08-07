## Audio Streaming with Sockets

### Audio Receiver

#### Description

This Python script sets up an audio receiver using sockets to receive audio data from a remote sender. The received audio data is then saved as a WAV file.

#### Requirements

- Python 3.x
- `pyaudio` library (`pip install pyaudio`)

#### Usage

1. Run the `receiver.py` script on the machine where you want to save the received audio.
2. The sender should run the corresponding `sender.py` script to send audio data to this receiver.

#### Configuration

- The receiver script binds to the IP address "0.0.0.0" and port 12345. If you want to change the listening address and port, modify the `server_socket.bind(("0.0.0.0", 12345))` line in the `receive_audio()` function.

### Audio Sender

#### Description

This Python script sets up an audio sender using sockets to stream audio data from the local machine to a remote receiver on a specified IP address and port.

#### Requirements

- Python 3.x
- `pyaudio` library (`pip install pyaudio`)

#### Usage

1. Run the `sender.py` script on the machine where the audio is being captured (sender).
2. Replace the `SERVER_IP` with the IP address of the remote receiver machine where the audio will be streamed.
