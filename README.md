# Reconocimiento de voz automático con speech_recognition

Usar cualquier modelo de speech_recognition con micrófono.

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

* Inestabilidad de reconocimiento de voz debido a la calidad de la señal de audio. 

* Tiempo de reconocimiento de voz y conversión a texto. 


## Manejo

Se puede cambiar el idioma de reconocimiento de voz en el parámetro de Language

```
value = r.recognize_google(audio, language="es")
```
