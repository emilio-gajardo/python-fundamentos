# Created on Fri May  3 12:08:54 2024
# @author: Usuario

# 1) Ejercicio: convertir la lista en una lista de diccionarios

from collections import Counter
print('\n== Ejercicio 1 ==')

lista_de_listas = [
    ['frontend', 'html'],
    ['frontend', 'css'],
    ['frontend', 'javascript'],
    ['backend', 'php'],
    ['backend', 'dart'],
    ['backend', 'java'],
    ['movil', 'dart']
]

claves = ['area', 'lenguaje']

lista_de_diccionarios = []

for sublista in lista_de_listas:
    diccionario = {}
    for i in range(0, len(claves)):
        diccionario[claves[i]] = sublista[i]
    lista_de_diccionarios.append(diccionario)


print(lista_de_diccionarios)

# %%

# 2) Ejercicio:
# Hacer una función que toma una frase y devuelve las  5 letras mas comunes
print('\n== 2) Ejercicio ==')


def letras_comunes(str_frase):
    print('str_frase = ', str_frase)
    ls_letras = []
    for letra in str_frase:
        if letra not in " ,.\n":
            ls_letras.append(letra)

    counter_letras = Counter(ls_letras)
    dict_counter = dict(counter_letras.most_common(5))
    print(dict_counter)


letras_comunes('Hola mundo desde python')

# %%

# 3) Ejercicio:
# Crear una función que dados 2 listas de elementos, retorne el coeficiente de jaccard.
# jaccard: calcula la similitud entre 2 grupos
# 1 = iguales
# 0 = totalemente distintos
# se calcula así:
# jaccard (el tamaño de la intersección ) ➗ (el tamaño de la unión de los conjuntos)
# intersacción = repeticiones
# union = todos los elementos

print('\n== 3) Ejercicio ==')


def coef_jaccard(ls1, ls2):

    set1 = set(ls1)
    set2 = set(ls2)

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    print('intersection = ', intersection)
    print('union = ', union)

    jaccart = len(intersection) / len(union)
    print('jaccart_coefficient = ', jaccart)


ls1 = [1, 2, 3, 4, 5, 6]
ls2 = [4, 5, 6]
coef_jaccard(ls1, ls2)
