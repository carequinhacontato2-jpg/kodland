import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from deep_translator import MyMemoryTranslator
import random

duration = 10  # segundos de gravação
sample_rate = 44100

palavras = [
    "cachorro", "janela", "montanha", "computador", "foguete",
    "floresta", "telefone", "oceano", "escola", "relógio",
    "bicicleta", "chocolate", "avião", "espelho", "livro",
    "tempestade", "castelo", "girafa", "planeta", "violão",
    "sorvete", "praia", "robô", "dinossauro", "pirata",
    "árvore", "lua", "carro", "música", "câmera"
]

lista = random.sample(palavras, 25)
palavra = random.choice(lista)

print("Palavra:", palavra)

traducao = MyMemoryTranslator(
    source="pt-BR",
    target="en-US"
).translate(palavra)

print("Tradução correta:", traducao)

print("Fale agora...")
recording = sd.rec(
  int(duration * sample_rate), # o número de amostras a serem registradas
  samplerate=sample_rate,      # taxa de amostras
  channels=1,                  # 1 significa gravação mono
  dtype="int16")               # tipo de dados para as amostras registradas
sd.wait()  # aguardando o término da gravação

wav.write("output.wav", sample_rate, recording)
print("Gravação concluída, estou reconhecendo...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="en-US")
    print("Você disse:", text)

    print("")

    if text.lower().strip() == traducao.lower().strip():
        print("ACERTOU! 😁👍")
    else:
        print("ERROU... 😒")
        print("Resposta correta:", traducao)

except sr.UnknownValueError:
    print("A fala não pôde ser reconhecida.")

except sr.RequestError as e:
    print(f"Service error: {e}")
print('FIM! Obrigado por jogar!')
