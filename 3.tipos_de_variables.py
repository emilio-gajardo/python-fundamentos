"""
Created on Thu Apr 25 00:06:28 2024
@author: Usuario
Objetivo: Tipos de variables de python
Los tipos de variables en python se llaman class
tipo string = class str
"""

#%% STRING

#%% Variable primitiva: string

print('Hola mundo')

var_region = 'Valparaíso'
var_pais = 'Chile'

# Ver tipo de variable
print(type(var_region))

# Concatenar variables string
print('\n== Concatenación ==')
# Forma 1
print('Forma 1: usando "," = ', var_region, var_pais)

# Forma 2
print('Forma 2: usando "+"  = ' + var_region + var_pais)

# Forma 3: método format aplicado a concatenar string
print('Forma 3: usando método format()')
msg1 = '> Hola soy de {}, vivo en {}'
print(msg1.format(var_pais, var_region))


# Multiplicación de string
print('\n== Multiplicación de string ==')
var_mensaje = 'Bienvenido'
print(var_mensaje * 3)

#%%
"""
Método de interpolación de strings
format aplicado a decimales numéricos
"""

import math

nroPi = math.pi
pi_str = 'format(nroPi): {}'.format(nroPi)
print(pi_str)
print(math.pi)
print('N° Pi 2f = {:.2f}'.format(math.pi))

#%% Método de interpolación de strings
# Disponible >= python 3.6
# f string

robot = 'python'
saludo2 = f"Hola buenos días, desde {robot}"
print(saludo2)

#%% Método upper(), lower(), capitalize()

titulo = 'intro to PYTHON'

print(f'\n<< Titulo original = {titulo} >>')

print('\nupper() => Convertir en mayúscula')
print(titulo.upper())

print('\nlower() => Convertir en minúsculas')
print(titulo.lower())

print('\ncapitalize() => Convertir en capitalizar')
print(titulo.capitalize())

#%%
# strip() => Eliminar caracteres de un string
# solo elimina los caracteres que estan al inicio y al final de la palabra
print('\nstrip() => método para quitar comas de un string')
nombre_con_comas = ',joham,'
print(f'\nNombre con comas: {nombre_con_comas}')
print('Nombre sin comas: ', nombre_con_comas.strip(','))

#%% Método: replace()
print('\nreplace() => reemplaza string')

name_original = 'Rojelio'
print(f'name_original: {name_original}')

name_replaced = name_original.replace('elio', 'as')
print(f'name_prelaced: {name_replaced}')

#%%

print('\nsplit() => convertir string en array de string')
colores = 'blanco|negro|rojo|azul|verde|amarillo'
print(f'colores: {colores}')

colores_array = colores.split("|")
print(f'colores_array: {colores_array }')



#%% NÚMEROS
"""
Números primitivos:
    int = enteros
    float = decimales
"""

entero = 23
print(type(entero))

decimal = 65.5
print(type(decimal))


#%%

print('\nstr() => conversion de numero a string')

nroUnoInt = 1
nroUnoStr = str(nroUnoInt)

print('nroUnoInt: ', type(nroUnoInt))
print('nroUnoStr: ', type(nroUnoStr))

#%%

print('\nInterpolación de números dentro de string')

# Ejp 1
pais = 'Chile'
anio = 1810
print(f'El país de {pais} fue fundado el año {anio}')

# Ejp 2
temp_actual = 18.5
print(f'La temperatura actual es de {temp_actual} °C')


#%%

print('\nConvertir string a números')
nro_string = '100'

print(f'nro_string = {nro_string} | tipo = {type(nro_string)}')

nro_int = int(nro_string)
print(f'nro_int = {nro_int} | tipo = {type(nro_int)}')

nro_float = float(nro_string)
print(f'nro_float = {nro_float} | tipo =  {type(nro_float)}')


#%%

print('\n== Operaciones aritméticas ==')
a = 5
b = 2
print(f'SUMA: a+b = {a+b}')
print(f'RESTA: a-b = {a-b}')
print(f'MULTIPLICACION: a*b = {a*b}')
print(f'DIVISION: a/b = {a/b}')

#%%

print('\n== Operaciones matematica ==')
a = 7
b = 2
print(f'(a = {a}) y (b = {b})')

print('\nMultiplo, quedarse solo con la parte entera')
print(f'(a//b) = {a//b}')

print('\nModulo, quedarse solo con la parte decimal o el resto')
print(f'(a%b) = {a%b}')

print('\nNegación, cambiar el sentido de un valor')
print(f'(-a) = {-a}')

print('\nPorntecia, elevar un número')
print(f'(a**b) = {a**b}')


#%%

print('\n== Boolean ==')

verdadero = True
falso = False
nulo = None

print(f'True = type(verdadero) = {type(verdadero)}')
print(f'False = type(falso) = {type(falso)}')
print(f'None = type(nulo) = {type(nulo)}')

print('\nCualquier tipo de vairable se puede convertir en True')
print('bool(zanahoria) =', bool('zanahoria'))
print('bool(1) = ', bool(1))
print('bool(-1) = ', bool(-1))

print('\nSolo el (cero=0), se convierte en false')
print('bool(0)    = ', bool(0))
print('bool(None) = ', bool(None))
print('bool("")   = ', bool(""))
print('bool([])   = ', bool([]))
print('bool({})   = ', bool({}))


#%%

print('\n== COMPARACIONES LÓGICAS ==')
a = 7
b = 2

print(f'({a} > {b}) = {a > b}')
print(f'({a} < {b}) = {a < b}')
print(f'({a} == {b}) = {a == b}')
print(f'({a} != {b}) = {a != b}')


#%%

print('\n== MULTIPLES COMPARACIONES A LA VEZ ==')
print(f'(a = {a}) y (b = {b})')
print(f'(not {a} != 23) = ', not {a} != 23)
print(f'({a} != 23 and {a} > {b}) = ', a != 23 and b > a)
print(f'({a} != 23 or {b} < {a}) = ', a != 23 or b < a)

#%%

print('\n== COMPARAR SI ALGO ES BOOL ==')
print('(verdadero is True) = ', verdadero is True)

#%%
print('\nTipo de dato "range"')
print('type(range(10)) = ', type(range(10)))
var_range = list(range(10))
print('range = ', var_range)
var_range_10 = range(10)
print(var_range_10)