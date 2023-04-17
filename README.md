# Reconocimiento de voz automático con speech_recognition

Este proyecto se desarrollo usando Python 3.8, se recomeinda usar cualquier modelo de speech_recognition con micrófono.

## Configuración

Se recomienda instalar este proyecto en un ambiente virtual.

```
pipenv shell
pip install -r requirements.txt
```

Finalmente se puede probar el reconocimiento de voz:

```
python __main__.py
```

### Posibles problemas:

* Sensibilidad a la dicción del hablante y a la legibilidad del audio. 

* Al utilizar el micrófono se requiere de un ambiente tranquilo para evitar interferencias de audio. 

* Demora en el tiempo de reconocimiento de voz y conversión a texto. 


## Manejo

Se puede cambiar el idioma de reconocimiento de voz en el parámetro de Language

```
value = r.recognize_google(audio, language="es")
```
