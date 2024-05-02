"""
Created on Mon Apr 29 19:33:24 2024
@author: Usuario
"""
#%%

print('\n== LISTAS ==')

frutas = ['feijoa', 'manzana', 'naranja', 'piña', 99]
print('frutas = ', frutas)
print('type(frutas) = ', type(frutas))

print('\nAcceder a un elemento de con el indice')
print('frutas[0] = ', frutas[0])

print('\nAcceder a un rango de elementos segun indice [inicio:fin]')
print('frutas[0:2] = ', frutas[0:2])
print('frutas[3:] = ', frutas[3:])

print('\nImprimir de la lista solo las posiciones de 2 en 2')
print('frutas[::2] = ', frutas[::2])

print('\nImprimir la lista en orden inverso')
print('frutas[::-1]', frutas[::-1])

print('\nImprimir largo de la lista')
print('len(frutas) = ', len(frutas))

print('\nAgregar elemento a una lista al final')
print('frutas.append("mango") = ', frutas.append('mango'))
print('frutas = ', frutas)

print('\nRepetir una lista')
print('(frutas * 2) = ', frutas * 2)

print('\nUnir 2 listas')
verduras = ['cebolla', 'ajo']
print('(frutas + verduras) = ', frutas + verduras)

print('\nModificar elementos de una lista, segun indice')
frutas[0] = 'FRUTILLA'
print('frutas[0] = "FRUTILLA"')
print('frutas = ', frutas)

print('\nModificar elementos de una lista, segun rango de indices')
frutas[2:] = [ 'UVA', 'UVA', 'UVA']
print("frutas[2:] = [ 'UVA', 'UVA', 'UVA']")
print('frutas = ', frutas)

print('\nBuscar elemento de una lista segun valor')
print('frutas = ', frutas)
print("('UVA' in frutas)= ", 'UVA' in frutas)

print('\nBuscar la primera posición de un elemento en la lista')
print(f'frutas = {frutas}')
fruta_buscada = 'UVA'
print('frutas.index("manzana") = ', frutas.index(fruta_buscada))


print('\nEliminar elemento de una lista, "segun la posicion" y retorna el elemento eliminado')
print(f'frutas = {frutas}')
print('frutas.pop(1) = ', frutas.pop(1))
print(f'frutas = {frutas}')


print('\nEliminar elemento de una lista, "segun el valor"')
print(f'frutas = {frutas}')
frutas.pop(frutas.index('FRUTILLA'))
print(f'frutas = {frutas}')


print('\nOrdenar elementos de una lista, "de menos a mayor"')
edades = [18, 65, 12, 5, 40, 20]
print('edades = ', edades)
print('edades.sort() = ', edades.sort())
print('edades =', edades)


print('\nGenerar lista de números')
print('list(range(10)) = ', list(range(10)))


print('\nCapturar el valor de una posición de un string')
nombre = 'Chile'
print('nombre = ', nombre)
print('nombre[0] = ', nombre[0])
print('nombre[2:] = ', nombre[2:])

print('\n==================================================================\n')

print('\n== TUPLAS ==')
print('Son versiones de listas inmutables')

mosqueteros = ('Athos', 'Porthos', 'Amaris')
print('type = ', type(mosqueteros))
print('mosqueteros = ', mosqueteros)


print('\nCapturar el valor de un elemento de una Tupla')
print('mosqueteros[2:] = ', mosqueteros[2:])


print('\n==================================================================\n')


print('\n== DICCIONARIOS ==')

inventario = {
    'melones': 3,
    'frutillas': 1,
    'manzanas': 4
    }
print('type(inventario) = ', type(inventario))
print('inventario = ', inventario)


print('\nVer las claves de un diccionario')
inventario_keys = inventario.keys()
print('inventario.keys() = ', inventario_keys)
ls_inventario_keys = list(inventario_keys)
print('claves de inventario en formato lista = ', ls_inventario_keys)


print('\nCapturar el valor segun el indice')
print('ls_inventario_keys[0] = ', ls_inventario_keys[0])


print('\nCapturar valores de un diccionario')
inventario_values = inventario.values()
ls_inventario_values = list(inventario_values)
print('valores de inventorio = ', ls_inventario_values)


print('\nCapturar el valor segun key')
print('inventario["manzanas"] = ', inventario['manzanas'])

#%%
print('\n== Validar si existe un key dentro de un diccionario ==')
inventario = {'melones': 3,'frutillas': 1,'manzanas': 4}
print('Diccionario => inventario = ', inventario)
print("('manzanas' in inventario) = ", 'manzanas' in inventario)

#%%
print('\nEliminar una key de un diccionario')
print('inventario = ', inventario)
print("inventario.pop('frutillas') = ", inventario.pop('frutillas'))
print('inventario = ', inventario)


print('\n==================================================================\n')


print('\n== LISTA DE LISTAS ==')

lista_trayectos = [
    ['Valparaiso', 'Viña del Mar'],
    ['Viña del Mar', 'Quilpué'],
    ['Quilpué', 'Belloto'],
    ['Belloto', 'Villa Alemana']
    ]
print('lista_trayectos = ', lista_trayectos)

print('\nVer un elemento segun el indice')
print('lista_trayectos[1] = ', lista_trayectos[1])
print('lista_trayectos[1][1] = ', lista_trayectos[1][1])

print('\n==================================================================\n')

print('\n== DICCIONARIO DE TUPLAS ==')

diccionario_trayectos = {
    'Valparaíso': ('Valparaíso', 'Viña del Mar', 'Quilpué'),
    'Santiago': ('Estación pajaritos', 'Estación central')
    }
print("diccionario_trayectos = ", diccionario_trayectos)

print('\nVer una tupla del diccionario')
print("diccionario_trayectos['Valparaíso'] = ", diccionario_trayectos['Valparaíso'])

print('\n==================================================================\n')

print('\n== LISTA DE DICCIONARIOS ==')
lista_diccionarios = [
    {'origen': 'Valparaíso', 'destino': 'Quilpué'},
    {'origen': 'Viña del Mar', 'destino': 'Limache'}
    ]

print('lista_diccionarios = ', lista_diccionarios)