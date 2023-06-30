#PROBLEMA 1

import requests

try:
    n=int(input('Ingrese la cantidad de bitcoins que posee: '))
    if n<0:
        raise ValueError
except ValueError:
    print('Error: Ingrese un número positivo.')


try:
    respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    respuesta.raise_for_status()
    data = respuesta.json()
    precio_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))
except (requests.RequestException, KeyError):
    print('Error al obtener el precio de Bitcoin desde la API.')
    exit()

total_usd = n*precio_usd
print(f'El costo actual de {n:,} Bitcoins es ${total_usd:,.4f} USD.')

#PROBLEMA 2


from pyfiglet import Figlet
import random

figlet = Figlet()

fuente = figlet.getFonts()

fuente_elegida = input("Ingrese el nombre de la fuente a utilizar (dejar en blanco para seleccionar aleatoriamente): ")

if not fuente_elegida:
    fuente_elegida = random.choice(fuente)
    print(f"Se ha seleccionado aleatoriamente la fuente '{fuente_elegida}'.")
else:

    if fuente_elegida not in fuente:
        print("La fuente ingresada no está disponible.")
        exit()

texto_imprimir = input("Ingrese el texto a imprimir: ")

figlet.setFont(font=fuente_elegida)

print(figlet.renderText(texto_imprimir))

#PROBLEMA 3

import requests

url = "https://images.unsplash.com/photo-1601979031925-424e53b6caaa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGVycml0b3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60"

respuesta = requests.get(url)

with open('cachorro.jpg','wb') as f:
    f.write(respuesta.content)
    pass



#PROBLEMA 4

def guardar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "w") as archivo:
            for i in range(1, 11):
                resultado = numero * i
                linea = f"{numero} x {i} = {resultado}\n"
                archivo.write(linea)
        
        print(f"Se ha guardado la tabla de multiplicar del número {numero} en el archivo tabla-{numero}.txt.")
    except IOError:
        print("Error al guardar la tabla de multiplicar.")

def mostrar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            contenido = archivo.read()
            print(f"Tabla de multiplicar del número {numero}:\n")
            print(contenido)
    except FileNotFoundError:
        print("El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla(numero, linea):
    if numero < 1 or numero > 10 or linea < 1 or linea > 10:
        print("Los números deben estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if linea <= len(lineas):
                linea_deseada = lineas[linea - 1]
                print(f"Línea {linea} de la tabla de multiplicar del número {numero}:")
                print(linea_deseada)
            else:
                print(f"La línea {linea} no existe en el archivo tabla-{numero}.txt.")
    except FileNotFoundError:
        print("El archivo tabla-{numero}.txt no existe.")

def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar completa")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese un número de línea entre 1 y 10: "))
            mostrar_linea_tabla(numero, linea)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")



mostrar_menu()


#PROBLEMA 5

import requests
import json
import csv

try:
    n = int(input("Ingrese la cantidad de bitcoins que posee: "))
    if n < 0:
        raise ValueError("El número de bitcoins no puede ser negativo.")
except ValueError:
    print("Error: Ingrese un número válido de bitcoins.")
    exit()

try:
    respuesta = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    respuesta.raise_for_status()
    data = respuesta.json()
    price_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))
except (requests.RequestException, KeyError):
    print("Error al obtener el precio de Bitcoin desde la API.")
    exit()

total_usd = n * price_usd
print(f"El costo actual de {n:,} Bitcoins es ${total_usd:,.4f} USD.")

with open("bitcoin_prices.txt", "w") as file:
    file.write(json.dumps(data))

fields = ["Fecha", "Precio USD"]
values = [data["time"]["updated"], price_usd]

with open("bitcoin_prices.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerow(values)

print("Datos guardados en los archivos bitcoin_prices.txt y bitcoin_prices.csv.")

