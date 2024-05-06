# Created on Thu May  2 18:20:10 2024
# @author: Usuario

# Sets: similar a una lista, pero con elementos no repetidos

from collections import defaultdict
from collections import Counter

print('\n== Crear set: Forma 1 ==')
amigos1 = set(['Emilio', 'Guillermo', 'Ignacio'])
print('type(amigos1) = ', type(amigos1))

print('\n== Crear set: Forma 2 ==')
colores1 = {'blanco', 'rojo', 'verde', 'azul'}
print('type(colores1) = ', type(colores1))

print('\n== Buscar elemento dentro de un set ==')
print("'blanco' in colores1 = ", 'blanco' in colores1)


print('\n== union() unir set sin elementos duplicados ==')
colores2 = {'negro', 'cafe', 'morado'}
print('colores1.union(colores2) = ', colores1.union(colores2))

print('\n== intersection() buscar elementos repetidos en los set ==')
frutas1 = {'manzana', 'pera', 'platano'}
frutas2 = {'melon', 'sandia', 'platano'}
print('frutas1.intersection(frutas2) = ', frutas1.intersection(frutas2))

print('\n== filtrar grupo 1 y dejar solo elementos no duplicados entre 2 set ==')
print('frutas1 - frutas2 = ', frutas1 - frutas2)

print('\n== Agrear elemento a un set')
print('frutas1 = ', frutas1)
frutas1.add('feijoa')
print('frutas1 = ', frutas1)

print('\n== Remover elemento de un set')
print('frutas1 = ', frutas1)
frutas1.remove('pera')
print('frutas1 = ', frutas1)


print('\n== Remover elementos repetidos de una lista convirtiendola a un set')
paises1 = ['Chile', 'Argentina', 'Peru', 'Venezuela', 'Venezuela']
print('paises1 = ', paises1)
paises_unicos = list(set(paises1))
print('paises_unicos = ', paises_unicos)


# el orden de los elmentos no importa
print('\n== Comparar igualdad elemetos de set ==')
set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}
print('(set1 == set2) = ', set1 == set2)
print('(set1 > set2) = ', set1 > set2)


print('\n== Contador o Counter ==')
votos = ['2016', '2016', '2017', '2018', '2019', '2020', '2020']
votos_count = Counter(votos)
print('votos_count = ', votos_count)

print('\n== Buscar existencia de elemento en un set ==')
# 0 al no existir
# cantidad al si existir
print("votos_count['2020'] = ", votos_count['2029'])

print('\n== Añadir un elemento nuevo al Counter ==')
print("votos_count.update['999'] = ", votos_count.update(['999']))
print(votos_count)

print('\n== Añadir varios elementos nuevos al Counter ==')
votos_count.update({'11': 11, '22': 22})
print(votos_count)


print('\n== Actualizar cantidad de un elemento a un Counter ==')
votos_count['999'] = 999
print(votos_count)

# %%


# DefaultDict:

# - Crea diccionarios.
# - Permite devolver un valor por defecto si una clave no existe
# - Se inicia pasandole una función que indicará el valor a devolver en caso de no existir la clave especificada
# - No existe como primitiva de python
# - Debe importarse así: "from collections import defaultdict"


sabores = defaultdict('vainilla')  # da error, forma invalida

# %%
print('\n== Definición de valor por defecto de un diccionario ==')
sabores = defaultdict(lambda: 'vainilla')
print(sabores)

# %%
print('\n-- Buscar un value usando el key existente --')
sabores['emi'] = 'lucuma'
print(sabores['emi'])

# %%
print('\n-- Buscar un value usando el key NO existente --')
# aquí retorna el valor por defecto definido en el "defaultdict"
print(sabores['nn'])

# %%

print('\n== Definir defaultdict usando diccionario ya creado ==')
frutas_dic = {'manzanas': 1, 'feijoa': 2, 'ciruela': 3}
frutas_df = defaultdict(lambda: 'fruta-default', frutas_dic)
print(frutas_df)

# %%

# Aplicación:
# Se tiene: una lista de listas con muchas propiedades
# Se necesita: obtener una lista de características

tecno_ls = [
    ['backend', 'java'],
    ['backend', 'javascript'],
    ['backend', 'php'],
    ['backend', 'python'],
    ['frontend', 'javascript'],
    ['frontend', 'css'],
    ['frontend', 'html'],
    ['frontend', 'typescript'],
]

tecno_df = defaultdict(list)

for (especialidad, lenguaje) in tecno_ls:
    tecno_df[especialidad].append(lenguaje)

tecno_df
