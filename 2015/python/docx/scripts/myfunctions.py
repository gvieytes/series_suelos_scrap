# -*- coding: utf-8 -*-
#!/home/gvieytes/Desktop/Trabajos/html-scrap/python/venv2.7/bin/python


#### Calcula la cantidad de campos entre "nº de registro" y "horizonte" ####

def contarCampos(fileName):
    with open(fileName, 'r') as f:
        while True:
            line = f.readline()

            # Salteo las lineas hasta "Horizonte" y cuento hasta "Profundidad"
            if line.strip().startswith("Horizonte"):
                i = 0
                while not f.readline().strip().startswith("Profundidad (cm"):
                    i = i + 1
                return i 

## Para probar el cantLineas
#import sys
## Capturo el nombre del archivo pasado por parametro 
#fileName = sys.argv[1]
#print "Filename", fileName
#print "cantidad", contarCampos(fileName)

################################################################



#### Para obtener la version correcta de los titulos ####

def getTitulo(tit):
    titulo = tit.lower()
    if " de registro" in titulo:
        return "NRO DE REGISTRO.."
    if "horizonte" in titulo:
        return "NOMBRE(S)........"
    if "profundidad (cm" in titulo:
        return "PROFUNDIDADES(CM)"
    if "mat.organica (%)" in titulo:
        return "MATERIA ORGÁN.(%)"
    if "c (%)" in titulo:
        return "CARBONO ORGÁN.(%)"
    if "n (%)" in titulo:
        return "NITRÓGENO TOT.(%)"
    if "c/n" in titulo:
        return "RELACIÓN C/N....."
    if ("<2" in titulo) or ("< 2"  in titulo):
        return "ARCILLA 2 (%)...."
    if "2-20" in titulo:
        return "LIMO 2-20 (%)...."
    if "2-50" in titulo:
        return "LIMO 2-50 (%)...."
    if "20-50" in titulo:
        return "LIMO 20-50 (%)..."
    if "50-74" in titulo:
        return "AMF 50-74 (%)...."
    if "50-100" in titulo:
        return "AMF 50-100 (%)..."
    if "50-500" in titulo:
        return "AM 50-500 (%)...."
    if "74-100" in titulo:
        return "AMF 74-100 (%)..."
    if "100-250" in titulo:
        return "AF 100-250 (%)..."
    if "100-500" in titulo:
        return "AM 100-500 (%)..."
    if "250-500" in titulo:
        return "AM 250-500 (%)..."
    if "500-1000" in titulo:
        return "AG 500-1000 (%).."
    if "500-2000" in titulo:
        return "AMG 500-2000 (%)."
    if "1000-2000" in titulo:
        return "AMG 1-2 mm (%)..."
    if "co3ca (%)" in titulo:
        return "CALCAREO CaCO3(%)"
    if "resistencia de la pasta" in titulo:
        return "RESIST. PASTA...."
    if "ph en pasta" in titulo:
        return "PH PASTA........."
    if "ph h2o" in titulo:
        return "PH H2O 1:2,5....."
    if "ph clk" in titulo:
        return "PH 1N ClK 1:2,5.."
    if "mmhos/cm" in titulo:
        return "CONDUCT mmhos/cm."
    if "valor t" in titulo:
        return "VT CIC ME/100G..."
    if "ca++" in titulo:
        return "CI ME/100G-Ca ++."
    if "mg++" in titulo:
        return "CI ME/100G-Mg ++."
    if "k+" in titulo:
        return "CI ME/100G-K +..."
    if "na+" in titulo:
        return "CI ME/100G-Na +.."
    if "h+" in titulo:
        return "CI ME/100G-H +..."
    if "% na/t" in titulo:
        return "Na+ % DEL VALOR T"
    if "humedad (%)" in titulo:
        return "EQUIV. HUMEDAD(%)"
    if "factor de humedad" in titulo:
        return "FACTOR DE HUMEDAD"
    if "ppm" in titulo:
        return "FÓSFORO ASIM(PPM)"
    if "valor s" in titulo:
        return "VALOR S (ME/100G)"
    if "ca disponible (mg/kg)" in titulo:
        return "Ca DISPON(mg/kg)."
    if "k disponible (mg/kg)" in titulo:
        return "K DISPON(mg/kg).."
    if "mg disponible (mg/kg)" in titulo:
        return "Mg DISPON(mg/kg)."
    if "h de cambio" in titulo:
        return "CI ME/100G-H +..."
    if "cic (meq/100 g)" in titulo:
        return "CIC ME/100G(T)..."
    if "% saturación de agua" in titulo:
        return "% SAT. DE AGUA..."
    if "so4ca" in titulo:
        return "SO4Ca (g/%)......"
    if "s/t" in titulo:
        return "SAT.B % (S/T)...."
    if "suma de bases" in titulo:
        return "SUM.B. ME/100G(S)"
    if "gravas" in titulo:
        return "GRAVAS..........."
    if "gravilla (> 2" in titulo:
        return "GRAVILL >2 T.Ca %"
    if "gravilla (> 7" in titulo:
        return "GRAVILL >7 T.Ca %"
    if "% de saturación de s + h" in titulo:
        return "% SAT. S + H....."
    if "% de saturación de t" in titulo:
        return "% SAT. T........."
    if "sales solubles grs (%)" in titulo:
        return "SALES SOL GRS. %."

## Para probar el getTitulo
#print getTitulos("Horizonte")
#print getTitulos(" de registo")

################################################################




#### Función para obtener LAT y LONG ####

import urllib
import simplejson

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

def get_coordinates(query, from_sensor=False):
    query = query.encode('utf-8')
    params = {
        'address': query,
        'sensor': "true" if from_sensor else "false"
    }
    url = googleGeocodeUrl + urllib.urlencode(params)
    json_response = urllib.urlopen(url)
    response = simplejson.loads(json_response.read())
    if response['results']:
        location = response['results'][0]['geometry']['location']
        latitude, longitude = location['lat'], location['lng']
        print query, latitude, longitude
    else:
        latitude, longitude = None, None
        print query, "<no results>"
    return latitude, longitude

## Para probar la funcion de coordenadas
#print "TEST1"
#print get_coordinates("Campo El Reposo, Dto Cuchilla Redonda, Dpto Gualeguaychu, Entre Rios", False)
#
#print "TEST2"
#print get_coordinates("Campo El Reposo, departamento Cuchilla Redonda, departamento Gualeguaychu, Entre Rios", False)

################################################################





#### Para armar el archivo principal de la serie ####

def armarSerie(fileName, titulos, idNro):
    ## Calculo la cantidad de campos a leer por fila
    cant_lineas = contarCampos(fileName)
    
    ## Leo las lineas que me sirven después de cada título ###
    archivo = open(fileName)
    
    ## Pongo un default a los parametros generales
    clasificacion = "FALTA!"
    serie = "FALTA!"
    ubicacion = "FALTA!"
    drenaje = "FALTA!"
    tipoSuelo = "FALTA!"
    
    start_read = False
    ## Recorro el archivo linea por linea mientras que tenga algo
    while True:
        line = archivo.readline()
    
        ## Si no hay mas lineas, salgo del loop
        if not line:
            break
    
        ## Levanto los datos generales del perfil
        if (line.strip().startswith("Pertenece a la familia")) and not start_read:
            lineFlia = line.strip("\"").split("\"")
            clasificacion = lineFlia[2].strip().decode('utf-8').upper().encode('utf-8').replace("DE LOS ","").strip("\.")
            tipoSuelo = lineFlia[1].decode('utf-8').upper().encode('utf-8')
    
        if (line.strip().startswith("SERIE")) and not start_read:
            lineSerie = line.strip().split("Símbolo: ")
            serie = ' '.join(((lineSerie[0].decode('utf-8').upper().encode('utf-8'))+"("+(lineSerie[1].decode('utf-8').upper().encode('utf-8'))+")").split())
    
        if (line.strip().startswith("Ubicación:")) and not start_read:
            lineUbicacion = line.strip().split("Ubicación: ")
            ubicacion = lineUbicacion[1]
    
        if (line.strip().startswith("Drenaje")) and not start_read:
            lineDrenaje = archivo.readline().strip()
            lineDrenaje = archivo.readline().strip()
            drenaje = lineDrenaje
    
        ## Salteo las lineas hasta el primer titulo
        if ((line.strip().startswith("Horizonte")) or (" de registro" in line.strip().lower())) and not start_read:
            start_read = True
            print "-----------------------------------------------------------------------------------------------------------------------------------------------------------"
            print "%s ->> ID..........................: %03d" % (fileName, idNro)
            print "%s ->> CLASIFICACION...............: %s" % (fileName, clasificacion)
            print "%s ->> SERIE.......................: %s" % (fileName, serie)
            print "%s ->> UBICACION...................: %s" % (fileName, ubicacion)
            print "%s ->> PROVINCIA...................: ENTRE RIOS" % fileName
            print "%s ->> LATITUD.....................: FALTA!" % fileName
            print "%s ->> LONGITUD....................: FALTA!" % fileName
            print "%s ->> ALTITUD.....................: FALTA!" % fileName
            print "%s ->> PENDIENTE...................: FALTA!" % fileName
            print "%s ->> DRENAJE.....................: %s" % (fileName, drenaje)
            print "%s ->> ESCURRIMIENTO...............: FALTA!" % fileName
            print "%s ->> PERMEABILIDAD...............: FALTA!" % fileName
            print "%s ->> TIPO DE SUELO...............: %s" % (fileName, tipoSuelo)
            print "%s ->> COLOR ......................: FALTA!" % fileName
    
        ## Si la linea es un titulo, guardo las siguientes N lineas
        if any(texto in line.strip().lower() for texto in titulos) and start_read:
            valores = []
    
            i = 0
            for i in range(cant_lineas):
                dato = archivo.readline().strip().replace(" ", "").replace("N.D.", "").replace("ND", "").replace("N.D", "").replace("N/D", "").replace("N,D,", "").replace("*", "").replace("Vest.", "").replace("vest(n)", "").replace("vest.", "").ljust(8)
                valores.append(dato)
    
            x = valores
            s = (" | ".join(['%s']*len(x))) % tuple(x)
            print "%s ->> HORIZONTE->%s: %s" % (fileName, getTitulo(line.strip()), s)
    
    archivo.close()


################################################################

