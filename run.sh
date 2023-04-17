#!/bin/bash
#Ejecuta el proyecto

#Inicia GNU radio 
exec python3 GNU\ radio\ files/top_block.py &

#Ejecuta servidor web
(cd webServer && exec pipenv run python __main__.py)
