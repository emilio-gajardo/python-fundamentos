# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 22:39:30 2024

@author: Usuario
"""

print('== Funcion tradicional ==')
def saludar():
    print('Hola mundo')

saludar()
print(type(saludar))
# salida = <class 'function'>


print('\n== Funcion con argumentos ==')
def saludar_persona(nombre):
    msg = f'Hola {nombre} buen día'
    print(msg)

saludar_persona('Emi')


print('\n== Funcion con argumentos y valor por defecto ==')
def despedir_persona(nombre = 'usuario'):
    msg = f'Adios {nombre} mucho exito'
    print(msg)

despedir_persona()

print('\n== Funcion con argumento y retorno ==')
def suma(a, b):
    return a+b

print('suma = ', suma(1, 2))

print('\n== Funcion con return multiple ==')
def suma_y_resta(a,b):
    suma = a+b
    resta = a-b
    return suma, resta # retirna una tupla = (suma, resta)

print(suma_y_resta(2, 4))


print('\n== Desestructuración de argumentos de funcion ==')
suma, resta = suma_y_resta(5, 2)
print('suma: ', suma)
print('resta = ', resta)


print('\n== Funcion lambda o anonima ==')
suma_lambda = lambda a, b: a + b
resultado_suma = suma_lambda(3, 5)
print('resultado_suma = ', resultado_suma)