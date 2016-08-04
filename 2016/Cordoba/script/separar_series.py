#####
## 
## Este script tiene como objetivo separar las series en archivos distintos
## Requisitos: Necesita un archivo de texto donde cada serie empiece con un 
##             renglon que diga "Serie NOMBRE-DE-SERIE"
## Uso: Por ahora el PATH de entrada y salida y el nombre de salida estan
##      hardcodeados en este mismo script. Falta que los reciba por parametro 
#####




def genNombreArchivo(linea):
    ## Armo el nombre del archivo de salida
    # Saco la palabra "Serie" y el espacio del principio
    nombreArchivo = linea[6:]
    # Saco los parentesis, reemplazo fin de linea con ".txt" y espacios por guion bajo
    nombreArchivo = nombreArchivo.replace('\n', '.txt').replace('(', '').replace(')', '').replace(' ', '_')
    # Convierto todo a minusculas
    nombreArchivo = nombreArchivo.lower()
    
    return(nombreArchivo)



pathEntrada = '../txt/'
nombreEntrada = 'series_de_suelos_normalizado.txt'
corte = 'Serie'
pathSalida = '../series/'

# Abro el archivo
with open(pathEntrada + nombreEntrada,'r') as archivoEntrada:
    # Recorro todo el archivo
    while True:
        linea = archivoEntrada.readline()
        if linea == '':
            break

        # Si encuentro el comienzo de una serie, abro un archivo con el nombre de esa serie para poner la salida
        if linea.startswith(corte):
            # Obtengo el nombre del archivo de salida
            nombreSalida = genNombreArchivo(linea)
            # Creo un archivo nuevo donde poner el recorte de la serie
            with open (pathSalida + nombreSalida, 'w') as archivoSalida:
                # Copio todas las lineas de una serie en su archivo correspondiente 
                while True:
                    linea = archivoEntrada.readline()
                    if linea.startswith(corte) or linea == '':
                        break
                    archivoSalida.write(linea)
