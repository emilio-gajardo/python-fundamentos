# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 12:55:38 2024

@author: Usuario
"""

# EJERCICIOS N° 1:
# Crear  un diccionario cuyas claves sean los tres primeros días de la semana
# y los valores sean la posición en la semana de dicho día
# Ejercicio 2: convertir todas las claves del diccionario anterior a mayúsculas

dias_semana = {
    'lunes': 1,
    'martes': 2,
    'miercoles': 3
}
print('1) dias_semana = ', dias_semana)

dic_new = {}

for (clave, valor) in dias_semana.items():
    key_new= clave.upper()
    dic_new[key_new] = valor

dias_semana = dic_new

print('2) dias_semana = ', dias_semana)
