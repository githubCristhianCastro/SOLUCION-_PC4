"""
Almacenar la informacion proveniente de mi API en una base datos. posterior a ello
leer los registros
"""

import requests 
import sqlite3
#import pprint

from pprint import pprint 

url_base= 'https://api.apis.net.pe/v1/tipo-cambio-sunat?month=1&year=2023'


def get_tipo_cambio_mes(anio:str, mes:str):
    respuesta = requests.get(url_base.format(anio=anio, mes=mes))
    data = respuesta.json()
    return data