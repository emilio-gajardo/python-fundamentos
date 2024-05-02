# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:31:43 2024

@author: Usuario
"""
#%%

# if elif: estructura de control

temp_actual = 10
msg = ''
print(f'Hay {temp_actual} °C')

if temp_actual <= 17:
    msg = 'Hace frío'
elif temp_actual > 16 and temp_actual < 20:
    msg = 'Esta templado'
elif temp_actual > 20:
    msg = 'Hace calor'
else:
    msg = 'Validar temperatura'
print(msg)

#%%

# if anidados
msg = ''
temp = 25
lluvia = True
if 20 < temp < 30:
    if lluvia:
        print('Esta lluviendo')

#%%

# bucle for

numeros = [1, 99, 12, 333, 5, 9, 15, 222, 777]
print(numeros)
numeros.sort()
print(numeros)

for elemento in numeros:
    if elemento <= 100:
        print(f'Válido = {elemento}')
    elif elemento == 222:
        pass # no hace nada
    elif elemento == 777:
        continue # salta a la siguiente iteración
    else:
        print(f'Inválido = {elemento}')
        break
#%%

# for simplificado para listas
[elemento for elemento in numeros if elemento < 10]


#%%
inventario = {'melones': 3, 'frutillas': 1, 'manzanas': 4}

# Iterar las claves de un diccionario con un for
for key in inventario.keys():
    print('key = ', key)

#%%

# Iterar keys y values de un diccionario

for fruta, cantidad in inventario.items():
    print(f'{fruta} = {cantidad} kg')
#%%

# Iterar string

pais = 'Chile'

for letra in pais:
    print(f'Letra = {letra}')
#%%

# try except = manejador de excepciones

numero_str = '10.5'

try:
    numero_int = int(numero_str)
    print(type(numero_int))
except ValueError as ve:
    print(f'ValueError: {ve}')
except Exception as e:
    print(f'Error: {e} \ntype: {type(e)}')

#%%

# Bucle = while

nro_elefantes = 1

while nro_elefantes <= 5:
    print(f'{nro_elefantes} elefante se balanceaba ...')
    nro_elefantes += 1
#%%

# bucle infinito

contador = 0
while 1 > 0:
    contador += 1
    print('Bucle infinito = ', contador)

#%%
# while
#input(), ingresar datos por la terminal

while 1:
    input_user = input('Ingrese un número del 1 al 10. Escrive [x] para salir: \n')
    
    try:
        if input_user == 'x':
            print('Bye')
            break
        elif int(input_user) <= 10:
            print(f'Has ingresado el número = {input_user}')
        else:
            print(f'Valor inválido {input_user}')
    except Exception as e:
        print(f'Error: {e}')