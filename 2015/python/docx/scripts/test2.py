# -*- coding: utf-8 -*-
#!/home/gvieytes/Desktop/Trabajos/html-scrap/python/venv2.7/bin/python

## Imports
import sys
import re

## Capturo el nombre del archivo pasado por parametro 
fileName = sys.argv[1]
## Capturo el nombre del archivo pasado por parametro 
archivo = open(fileName)

start_read = False

while True:
    line = archivo.readline()

    ## Si no hay mas lineas, salgo del loop
    if not line:
        break

    ## Levanto los datos generales del perfil
    if (line.strip().startswith("Pertenece a la familia")) and not start_read:
        tipoSuelo = str(line.strip("\"")).split("\"")
 
print tipoSuelo[1]
