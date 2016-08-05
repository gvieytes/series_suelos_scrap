#####
## 
## Este script tiene como objetivo separar las series en archivos distintos
## Requisitos: Necesita un archivo de texto donde cada serie empiece con un 
##             renglon que diga "Serie NOMBRE-DE-SERIE"
## Uso: Por ahora el PATH de entrada y salida y el nombre de salida estan
##      hardcodeados en este mismo script. Falta que los reciba por parametro 
#####

import os


# Arma el nombre del archivo de salida.
# Recibe numero de orden y renglon que diga "Serie NOMBRE-DE-SERIE"
def genNombreArchivo(numero,linea):
    # Saco la palabra "Serie" y el espacio del principio
    nombreArchivo = linea[6:]
    # Saco los parentesis, reemplazo fin de linea con ".txt" y espacios por guion bajo
    nombreArchivo = nombreArchivo.replace('\n', '.txt').replace('(', '').replace(')', '').replace(' ', '_')
    # Convierto todo a minusculas
    nombreArchivo = nombreArchivo.lower()
    
    return(str(numeroSerie).zfill(3) + '-' + nombreArchivo)


## VARIABLES
# Variables de ubicacion de archivos de entrada y salida
pathEntrada = '../txt/'
nombreEntrada = 'series_de_suelos_normalizado.txt'
pathSalida = '../series/'

# String de division de series (corte entre series)
corte = 'Serie'

# Inicializacion de variables
numeroSerie = 0
nombreSalida = ''
lineas = []

# Abro el archivo
with open(pathEntrada + nombreEntrada,'r') as archivoEntrada:
    # Recorro todo el archivo
    for linea in archivoEntrada:
        # Verifico si empieza una nueva serie
        if linea.startswith(corte):
            # Guardo en un archivo si no es la primera vez que aparece el punto de corte "Serie"
            if numeroSerie > 0:
                with open(nombreSalida, 'wt') as archivoSalida:
                    archivoSalida.write('\n'.join(lineas))
            lineas = []
            numeroSerie += 1
            nombreSalida = os.path.join(pathSalida + genNombreArchivo(numeroSerie,linea))
        lineas.append(linea.rstrip('\n'))

    with open(nombreSalida, 'wt') as archivoSalida:
                archivoSalida.write('\n'.join(lineas))
        

