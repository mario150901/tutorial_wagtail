'''
crear eventos

ejecutar:

python manage.py shell < datos/crear_eventos.py
'''

from deportes.models import Deporte
import datetime as dt
import json
import os


# borrar eventos
for e in Deporte.objects.all():
    e.delete()

#lista de eventos del json
if os.path.exists("datos/federaciones-deportivas-aragonesas.json"):
    events = json.load(open("datos/federaciones-deportivas-aragonesas.json", encoding="utf-8"))
else:
    events = json.load(open("federaciones-deportivas-aragonesas.json", encoding="utf-8"))

events = events['docs']
for e1 in events:
    e = Deporte()
    e.nombre = e1["nombre"].replace('"', "")
    e.descripcion = e1["descripcion"]
    e.imagen = e1["imagen"]
    e.fecha_inicio = dt.datetime.strptime(str(e1["fecha_inicio"]), "%Y%m%d").date()
    e.categoria = e1["categoria"]
    e.autor = e1['autor']
    e.save()