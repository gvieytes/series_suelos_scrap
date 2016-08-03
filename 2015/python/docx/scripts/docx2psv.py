# -*- coding: utf-8 -*-
#!/home/gvieytes/Desktop/Trabajos/html-scrap/python/venv2.7/bin/python

## Imports
import sys
import argparse

## Importo funciones que yo cree
from myfunctions import *


## Lista de titulos
titulos = [" de registro", "horizonte", "profundidad (cm", "mat.organica (%)", \
          "c (%)", "n (%)", "c/n", "<2", "< 2", "2-20", "2-50", "20-50", \
          "50-74", "50-100", "50-500", "74-100", "100-250", "100-500", \
          "250-500", "500-1000", "500-2000", "1000-2000", "co3ca (%)", \
          "resistencia de la pasta", "ph en pasta", "ph h2o", "ph clk", \
          "mmhos/cm", "valor t", "ca++", "mg++", "k+", "na+", "h+", "% na/t", \
          "humedad (%)", "factor de humedad", "(ppm)", "valor s", \
          "ca disponible (mg/kg)", "k disponible (mg/kg)", "mg disponible (mg/kg)", \
          "h de cambio", "cic (meq/100 g)", "% saturación de agua", "so4ca", "s/t", \
          "suma de bases", "gravas", "gravilla (> 2", "gravilla (> 7", \
          "% de saturación de s + h", "% de saturación de t", "sales solubles grs (%)"]

## Capturo el nombre del archivo pasado por parametro 
#fileName = sys.argv[1]
i = 1
args = sys.argv[1:]
for f in args:
    armarSerie(f, titulos, i)
    i = i + 1

