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

# Configurar PyAudio para la captura de audio en tiempo real
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=125000, input=True, frames_per_buffer=1024)

# Transcribir el audio en tiempo real
while True:
    data, addr = sock.recvfrom(1024)
    audio_tensor = torch.from_numpy(np.frombuffer(data, dtype=np.int16)).float()
    input_values = tokenizer(audio_tensor, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]
    print(transcription)

stream.stop_stream()
stream.close()
audio.terminate()
