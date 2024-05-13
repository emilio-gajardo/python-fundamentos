# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:52:02 2024
@author: Usuario
"""

import os

# crear carpeta
os.makedirs("./data/nombres/", exist_ok=True)

# %%

# listar archivos
archivos_carpeta_actual = os.listdir(".")
print(archivos_carpeta_actual)

# %%

# abrir archivo. r=read
archivo_inexistente = open("./data/nombres/usuarios.txt", "r")

# %%

# escribir archivo w=write
archivo_para_escribir = open("./data/nombres/usuarios.txt", "w")
archivo_para_escribir.write("Hola ")
archivo_para_escribir.write("Mundo")

# solo se escribe si el archivo esta cerrado
archivo_para_escribir.close()

# %%

# agregar contenido al archivo. a=add
archivo_para_escribir = open("./data/nombres/usuarios.txt", "a")
archivo_para_escribir.close()
archivo_para_escribir.write("\nHola mundo desde python")
archivo_para_escribir.close()

#%%

# Forma segura de leer y escribir archivos
# Usando GESTOR DE CONTEXTO
# Aquí no es necesario usar ".close()"

usuarios = ["user1", "user2", "user3", "user4"]
with open("./data/nombres/usuarios.txt", "a") as fname:
    fname.write("\n\n== Usuarios ==")
    for usuario in usuarios:
        fname.write(f"\n{usuario}")

#%%

# lectura archivo completo
with open("./data/nombres/usuarios.txt", "r") as fname:
    print("\n> Read file use read()")
    file_datos = fname.read()

print(file_datos)
type(file_datos)


#%%

# Leer cada linea del archivo por separado.
# Forma mas eficiente

ls_data_file = []
with open("./data/nombres/usuarios.txt", "r") as fname:
    print("\n> Read data use = readlines()")
    lineas = fname.readlines()
    for linea in lineas:
        ls_data_file.append(linea.strip("\n"))

print(ls_data_file)

#%%

# Usando libreria PATHLIB para leer archivos
# Los saltos de línea se representan en:
# Windows: \
# Linux: /

from pathlib import Path

ruta = Path("./data/nombres/")
archivo= ruta/ "usuarios.txt"
print(type(archivo))
archivo.read_text()

#%%

# Escribir archivo con Pathlib
ruta = Path("./data/nombres/")
archivo = ruta / "usuarios_2.txt"
msg = "Hola, usando Pathlib > write_text() para crear archivo"
archivo.write_text(msg)


#%%
print(archivo.read_text())
#%%

# Agregando texto a un archivo

usuarios = ["joham", "elisa", "ruth"]
ruta = Path("./data/nombres/")
archivo = ruta / "usuarios_2.txt"

with open(archivo, "a") as fname:
    fname.write("\nUsuarios:")
    for usuario in usuarios:
        fname.write(f"\n{usuario}")

print("\n> Leyendo archivo:")
archivo.read_text()
