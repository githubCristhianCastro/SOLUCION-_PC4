import requests 
import sqlite3
#import pprint

from pprint import pprint 

url_base= 'https://api.coindesk.com/v1/bpi/currentprice.json'

respuesta = requests.get(url_base)
data_api =respuesta

def main():
    conexion = sqlite3.connect('cryptos.db')

    cursor= conexion.cursor()

    sentencia_create_table = open('creacion_tabla.sql').read()
    cursor.execute(sentencia_create_table)
    conexion.commit()

    datos_bitcoin=[]
    cursor.executemany("INSERT INTO bitcoin VALUES (?,?)",datos_bitcoin)
    conexion.commit()

    pass


nuevo_listado = []




pprint(data_api)

