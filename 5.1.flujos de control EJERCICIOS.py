# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:50:08 2024

@author: Usuario
"""

dias_semana = {
    'lunes': 1,
    'martes': 2,
    'miercoles': 3,
    'jueves': 4,
    'viernes': 5,
    'sabado': 6,
    'domingo': 7,
}

# Ejercicio 1: convertir todas las claves a mayúsculas usando bucle


semana_mayusculas = {}

for (clave, valor) in dias_semana.items():
    clave_mayusculas = clave.upper()
    semana_mayusculas[clave_mayusculas] = valor

dias_semana = semana_mayusculas
print('\ndias_semana = ', dias_semana)

ls_semana = list(dias_semana)
print('\nls_semana = ', ls_semana)

# Ejercicio 2: solo dias con "o"

dias_con_o = []

for dia in ls_semana:
    if 'O' in dia.upper():
        dias_con_o.append(dia)

print('\ndias_con_o = ', dias_con_o)