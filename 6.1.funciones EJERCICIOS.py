# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:04:27 2024

@author: Usuario
"""

# %% 1 Ejercicio: Crear función resta 2 nros y devuelve resultado


def resta2(a, b):
    return a-b


print('1 Ejercicio = ', resta2(3, 2))

# %% 2 Ejercicio: crear función lambda que convierte string a minusculas


to_lowercase = lambda in_string: in_string.lower()


print('2 Ejercicio = ', to_lowercase('HOLA MUNDO'))

# %%
"""
3 Ejercicio:
crear función que acepta 3 argumentos 2 números y 1 string
suma = devuelve el resultado de los 2 numeros
resta = devuelve el resultado de los 2 numeros
"""


def suma_y_resta(a, b, action):
    if (action == 'suma'):
        res = a + b
    elif (action == 'resta'):
        res = a - b
    return res


print('3) Ejercicio = ', suma_y_resta(10, 5, 'suma'))

# %%
"""
4 Ejercicio:
crear función que pregunte al usuario una frase
devuelve la frase con palabras en orden inverso
Ejp:
    input: la lluvia en Chile
    output: Chile en lluvia la
"""


def question_to_user():
    print('\n== 4) Ejercicio ==\n')
    msg = 'Ingresa una frase por favor: \n>> '

    input_string = input(msg)
    input_string_clean = input_string.strip(' ')
    input_list = []

    while (len(input_string_clean) == 0):
        input_string = input(msg)
        input_string_clean = input_string.split(' ')

    if len(input_string_clean) > 0:
        input_list = input_string_clean.split(' ')
        input_list_inv = input_list[::-1]
        string_inv = " ".join(input_list_inv)
        print('string_inv = ', string_inv)


question_to_user()

# %% 5. Ejercicio: crear una función que detecte si una palabra o frase es palindromo


def string_palindromo():
    print('\n\n== 5) Ejercicio ==\n')
    msg = 'Ingrese una palabra o frase palindromo: \n>> '
    in_user = ''
    in_clean = ''
    largo = 0
    in_lista = []

    while largo < 3:
        in_user = input(msg)
        in_clean = in_user.strip(' ')
        largo = len(in_clean)

    if largo >= 3:
        for caracter in in_clean:
            in_lista.append(caracter)

        lista_inversa = in_lista[::-1]

        if in_lista == lista_inversa:
            print('✔️ Es palindromo')
        else:
            print('✖ No es palindromo')


string_palindromo()

# %% 6. Ejercicio:
# crear una función que reciba una lista de listas
# debe retornar una lista unica


def lista_simplificada(lista_de_listas):
    print('\n\n== 6) Ejercicio ==\n')

    try:
        cadena = []
        print('lista_de_listas = ', lista_de_listas)
        nro_listas = len(lista_de_listas)
        print('\nnro_listas = ', nro_listas)
        
        for elemento in lista_de_listas:
            for indice, valor in enumerate(elemento):
                cadena.append(valor)

        print('\ncadena = ', cadena)

    except Exception as e:
        print('> Error: ', e)

lista_de_listas = [
    ['blanco', 'negro', 'verde', 'azul'],
    ['dulce', 'salado', 'acido', 'amargo'],
]


lista_simplificada(lista_de_listas)
