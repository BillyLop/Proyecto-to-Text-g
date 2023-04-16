import pyaudio
import socket
import numpy as np
import torch
import torchaudio
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

# Definir el modelo y el tokenizer
tokenizer = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-xlsr-53-spanish")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-xlsr-53-spanish")

# Configurar el socket UDP para recibir el audio
UDP_IP = "192.168.1.12"
UDP_PORT = 2000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

import pyaudio
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
# RATE = 19000
# A frame must be either 10, 20, or 30 ms in duration for webrtcvad
FRAME_DURATION = 30
# FRAMES_PER_BUFFER = 3200
FRAMES_PER_BUFFER = int(RATE * FRAME_DURATION / 1000)
RECORD_SECONDS = 50

# Configurar PyAudio para la captura de audio en tiempo real
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
   channels=CHANNELS,
   rate=RATE,
   input=True,
   frames_per_buffer=FRAMES_PER_BUFFER)

# Transcribir el audio en tiempo real
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

while data != '':
    #stream.write(data)
    audio_tensor = torch.from_numpy(np.frombuffer(data, dtype=np.int16)).float()
    input_values = tokenizer(audio_tensor, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]
    print(transcription)
    data, addr = sock.recvfrom(2048)

stream.stop_stream()
stream.close()
audio.terminate()
