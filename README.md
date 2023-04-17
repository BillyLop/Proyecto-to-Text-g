# Reconocimiento de voz automático con speech_recognition

Este proyecto se desarrollo usando Python 3.8, se recomienda usar cualquier modelo de speech_recognition con micrófono.

![demo video](./docs/FM2Text.mp4)

## Configuración

Se recomienda instalar este proyecto en un ambiente virtual.

```
pipenv shell
pip install -r requirements.txt
```
Para ejecutar GNU radio y levantar el servidor web puede utilizar el comando:

```
./run.sh
```
Debe ejecutarse desde el directorio raíz del proyecto.

Alternativamente se puede correr por separado y de forma manual.
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
