# -*- coding: utf-8 -*-
#!/home/gvieytes/Desktop/Trabajos/html-scrap/python/venv2.7/bin/python

import sys
import argparse

fileName = sys.argv[1]

def decdeg2dms(dd):
  mnt,sec = divmod(dd*3600,60)
  deg,mnt = divmod(mnt,60)
  return abs(deg),abs(mnt),abs(sec)

archivo = open(fileName)

while True:
  line = archivo.readline()

  ## Si no hay mas lineas, salgo del loop
  if not line:
    break

  if (line.strip().startswith("LAT")):
    dd = float(line.strip().lstrip("LAT: "))
    decdeg2dms(dd)
    print "S%02d%02d%02d" % decdeg2dms(dd)
  elif (line.strip().startswith("LON")):
    dd = float(line.strip().lstrip("LON: "))
    decdeg2dms(dd)
    print "O%02d%02d%02d" % decdeg2dms(dd)
  else:
    print line.strip()
