'''
crear eventos

ejecutar:

python manage.py shell < datos/crear_eventos.py
'''

import datetime as dt
import json
import os
import csv

datos = json.load(open("federaciones-deportivas-aragonesas.json",  encoding="utf-8"))
# print(datos)
#limpieza
datos = datos[0]
datos = datos["rows"]
datos = [d["values"] for d in datos]
claves = datos[0]

#crear csv
f = open("equipos.csv", "w")
fw = csv.writer(f)
fw.writerows(datos)
f.close()

# De csv a json
from csv import DictReader
dr = DictReader(open("equipos.csv"))
datosj = [x for x in dr]

# Convertir listas a json
datosj = [dict(zip(claves, d)) for d in datos[1:]]
print(datosj)
json.dump(datosj, open("datos_equipos.json", "w", encoding='utf-8'), ensure_ascii=False)
