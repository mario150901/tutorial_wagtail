from deportes.models import Deporte
import json
import os


# borrar eventos
for d in Deporte.objects.all():
    d.delete()

#lista de eventos del json
if os.path.exists("datos/datos_equipos.json"):
    deportes = json.load(open("datos/datos_equipos.json", encoding="utf-8"))
else:
    deportes = json.load(open("datos_equipos.json", encoding="utf-8"))

#deportes = deportes[0]
'''
 {
    "Entidad": "AJEDREZ",
    "Domicilio": "Av.��Jos� Atar�s,101 semis�tano",
    "C.P": 50018.0,
    "Localidad": "ZARAGOZA",
    "Horario": "Lu y Mi de�18 a�20 h.",
    "Web": "http://ajedrezaragon.com",
    "Email": "fada@ajedrezaragon.com",
    "Tfno": "976 526213",
    "Fax": ""
  },

'''

for d1 in deportes:
    d = Deporte()
    d.entidad = d1["Entidad"]
    d.domicilio = d1["Domicilio"]
    d.c_p = d1["C.P"]
    d.localidad = d1["Localidad"]
    d.horario = d1["Horario"]
    d.web = d1['Web']
    d.email = d1['Email']
    d.telefono = d1['Tfno']
    d.fax = d1['Fax']
    d.save()