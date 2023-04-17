import speech_recognition as sr
import asyncio

async def microphone_convertion (self):
  r = sr.Recognizer()
  m = sr.Microphone()

  try:
      with m as source: r.adjust_for_ambient_noise(source, duration=0.01)
      while True:
          print("Say something!")
          with m as source: audio = r.listen(source)
          print("Got it! Now to recognize it...")
          try:
              # recognize speech using Google Speech Recognition
              value = r.recognize_google(audio, language="es")

              # we need some special handling here to correctly print unicode characters to standard output
              if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                  print(u"{}".format(value).encode("utf-8"))
                  yield u"{}".format(value).encode("utf-8")
              else:  # this version of Python uses unicode for strings (Python 3+)
                  print("{}".format(value))
                  yield "{}".format(value)
          except sr.UnknownValueError:
              print("Oops! No entendí eso")
              yield "Oops! No entendí eso"
          except sr.RequestError as e:
              print("Uh oh! No se pudieron solicitar los resultados del servicio de reconocimiento de voz de Google; {0}".format(e))
              yield "Uh oh! No se pudieron solicitar los resultados del servicio de reconocimiento de voz de Google; {0}".format(e)
  except KeyboardInterrupt:
      pass
