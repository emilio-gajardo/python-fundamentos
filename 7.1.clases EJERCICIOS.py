# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:55:09 2024

@author: Usuario
"""

# %%
""" 1) Ejercicio:
Crear clase taxi que herede de vehículo y que pueda cobrar el trayecto
Debe tener atributo = distancia_recorrida
Debe tener metodo:
    "cobrar": imprime la cantidad a cobrar "3 euros x km"
    "añadir_distancia": se suma a la disntacia recorrida numero en km
    "añadir_tiempo": dado un tiempo en horas se añade distancia en función de la velocidad
"""


class Vehiculo:
    def __init__(self, distancia_recorrida=0):
        self.distancia_recorrida = distancia_recorrida


class Taxi(Vehiculo):

    def cobrar(self):
        tarifa = 3
        monto = self.distancia_recorrida * tarifa
        print('Taxi.cobrar() = {} $'.format(monto))

    def añadir_distancia(self, distancia):
        self.distancia_recorrida += distancia

    def añadir_tiempo(self, tiempo, velocidad):
        distancia = velocidad * tiempo
        self.distancia_recorrida += distancia


taxi1 = Taxi(100)
print('taxi1.distancia_recorrida = {} km'.format(taxi1.distancia_recorrida))
taxi1.cobrar()

taxi1.añadir_distancia(10)
taxi1.añadir_tiempo(1, 60)
print('taxi1.distancia_recorrida = {} km'.format(taxi1.distancia_recorrida))
taxi1.cobrar()

# %%
""" 2) Ejercicio:
Crear una clase Parking, donde puedan aparcar un limite determinado de vehiculos
(solo vehiculos)
y donde se puede validar si un vehiculo esta aparcado o no
    """


class Vehiculo:
    def __init__(self, patente):
        self.patente = patente


class Parking:

    def __init__(self, espacios_totales, lista_patentes=[]):
        self.espacios_totales = espacios_totales
        self.lista_patentes = lista_patentes
    
    def mostrar_ocupacion(self):
        ocupacion = (len(self.lista_patentes) * 100) / self.espacios_totales
        print(f'ocupación = {ocupacion} %')

    def validar_vehiculo(self, vehiculo):

        patente = vehiculo.patente
        print('patente = ', patente)

        if self.espacios_totales > len(self.lista_patentes):
            print('Si cumple: hay cupos libres')

            if patente not in self.lista_patentes:
                print('Si cumple: patente no registrada')
                self.lista_patentes.append(patente)

                if type(vehiculo) == Vehiculo:
                    print('Si cumple, es de tipo vehiculo')
                elif type(vehiculo) != Vehiculo:
                    print('No cumple: no es de tipo vehiculo')

            elif patente in self.lista_patentes:
                print('No cumple: ya esta estacionado')

        elif self.espacios_totales == len(self.lista_patentes):
            print('No cumple: sin cupos libres')


lista_patentes = ['123-1']
vehiculo1 = Vehiculo(patente='123-1')
parking1 = Parking(100, lista_patentes)
parking1.mostrar_ocupacion()
parking1.validar_vehiculo(vehiculo1)
parking1.mostrar_ocupacion()