# -*- coding: utf-8 -*-
#!/home/gvieytes/Desktop/Trabajos/html-scrap/python/venv2.7/bin/python

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


### Ejecuto la funcion
import sys

fileName = sys.argv[1]

## Leo las lineas que me sirven después de cada título ###
archivo = open(fileName)

while True:
    line = archivo.readline()

    ## Si no hay mas lineas, salgo del loop
    if not line:
        break

    print get_coordinates(line, False)

