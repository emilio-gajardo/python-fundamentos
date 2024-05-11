# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:22:36 2024

@author: Usuario
"""

# %%
import os
my_path = "./data/ejercicios/"
os.makedirs(my_path, exist_ok=True)
# %%
""" EJERCICIO 1:
    Hacer una función que dado el nombre de un archivo,
    lo lea y devuelva la línea con la mayor longitud
"""
my_file_name = "frases motivacionales.txt"
my_path = "./data/ejercicios/"


def read_file_long_line(my_file_name=""):
    print("\n== EJERCICIO 1 ==")

    try:
        if len(my_file_name.strip()) == 0:
            print("> Nombre de archivo inválido")

        elif len(my_file_name.strip()) > 0:
            print("> Nombre archivo ok")
            ls_data_file = []
            my_archivo_csv = my_path + my_file_name
            print("> my_archivo_csv = ", my_archivo_csv)

            with open(my_archivo_csv, "r") as fname:
                lineas = fname.readlines()
                for linea in lineas:
                    ls_data_file.append(linea.strip("\n"))

            element_longer = max(ls_data_file, key=len)
            element_longer_index = ls_data_file.index(element_longer)
            element_longer_len = len(element_longer)

            print("> element_longer_index = ", element_longer_index)
            print("> element_longer_len =", element_longer_len)
            print('> element_longer = ', element_longer)

    except Exception as e:
        print(f'Exception: \n{e}')


read_file_long_line(my_file_name)

# %%
""" EJERCICIO 2
Hacer una función que tenga como argumento un nombre de un archivo y un número "N"
y devuelva las "N" últimas líneas del archivo
"""
# from pathlib import Path


def fn_read_file_n_lines(file_name, n_lineas):
    print("\n== Ejercicio 2 ==\n")

    try:
        path = "./data/ejercicios/"
        path_file = (path + file_name)
        ls_data_file = []

        with open(path_file, "r") as fname:
            lineas = fname.readlines()
            for linea in lineas:
                ls_data_file.append(linea.strip("\n"))

        last_elements = ls_data_file[-n_lineas:]

        contador = 1
        for elemento in last_elements:
            print("> [{} Línea] = {} ".format(contador, elemento))
            contador += 1

    except Exception as e:
        print(f"Exception: \n{e}")


file_name = "mensaje motivacional a programadores.txt"
fn_read_file_n_lines(file_name, 23)

# %%
""" EJERCICIO 3
1.- Hacer una función que dado un diccionario cree un archivo csv
2.- El nombre tiene que acabar en "csv" con los datos del mismo
3.- Los archivos csv [Comma-Separated-Values] son una forma de almacenar datos con cada columna separada por una coma
4.- Ejemplo:

    Diccionario:
    {
     nombre: ["nombre1", "nombre2"],
     edad: [1, 2],
     ciudad: ["ciudad1", "ciudad2"]
    }

    Formato csv:
    nombre, edad, ciudad
    nombre1, 1, ciudad1
    nombre2, 2, ciudad2
"""


def fn_convert_dic_to_csv(my_dictionary):
    print("\n== EJERCICIO 3 ==\n")

    try:
        path = "./data/ejercicios/"
        file_name = "dictionary to csv.csv"
        archivo_csv = f"{path}{file_name}"

        # capturar claves de diccionario
        columnas = list(my_dictionary.keys())

        # contar columnas del 1° lista
        longitud_datos = len(my_dictionary[columnas[0]])

        with open(archivo_csv, "w") as csvfile:

            # convertir lista a string con formato
            encabezado = ",".join(columnas)+"\n"

            # escribir encabezados
            csvfile.write(encabezado)

            for i in range(longitud_datos):
                fila = []
                for columna in columnas:
                    fila.append(str(my_dictionary[columna][i]))

                # convertir lista a string con formato
                fila_csv = ",".join(fila)+"\n"

                # escribir filas
                csvfile.write(fila_csv)

        with open(archivo_csv, "r") as fname:
            print("> Read file csv:\n")

            # leer e imprimir archivo
            file_read = fname.read()
            print(file_read)

    except Exception as e:
        print(f"Exception = {e}")


my_dictionary = {
    "nombre": ["nombre1", "nombre2"],
    "edad": [1, 2],
    "ciudad": ["ciudad1", "ciudad2"]
}

fn_convert_dic_to_csv(my_dictionary)
