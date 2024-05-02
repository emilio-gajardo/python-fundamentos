# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:01:41 2024
@author: Usuario
"""


class AutoBasico:
    def girar_izq(self):
        print('girar a la izq')

    def girar_der(self):
        print('girar a la der')

    def acelerar(self):
        print('acelerar')

    def frenar(self):
        print('frenar')


print(AutoBasico())

# Instacia de una clase
auto1 = AutoBasico()
print(auto1)

# Comparar tipo de clase
print(type(auto1) == AutoBasico)

# Ejecutar métodos de clase
auto1.acelerar()
auto1.frenar()

# %%


class AutoConColor:
    def __init__(self, color):
        self.color = color  # atributo

    def describir(self):
        print('color = ', self.color)

    def izquierda(self):
        print('Izquierda')

    def derecha(self):
        print('Derecha')

    def acelerar(self):
        print('Acelerar')

    def frenar(self):
        print('Frenar')


# instanciación
auto_rojo = AutoConColor(color='rojo')

# llamada a método
auto_rojo.describir()

# llamada a propiedad
print('auto_rojo.color = ', auto_rojo.color)

# agregar propiedad a objeto
auto_rojo.matricula = '777-7'
print('auto_rojo.matricula = ', auto_rojo.matricula)

# %%


class Auto:

    # constructor
    def __init__(self, modelo, velocidad_max, color='negro'):
        self.color = color
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.velocidad_actual = 0

    def describir(self):
        print('color: {}, modelo: {}, velocidad_max: {}'
              .format(self.color, self.modelo, self.velocidad_max)
              )

    def estado(self):
        if self.velocidad_actual == 0:
            print('Detenido')
        else:
            print('Andando a: {} km/h'.format(self.velocidad_actual))

    def izquierda(self):
        print('Izquierda')

    def derecha(self):
        print('derecha')

    def acelerar(self, acelerar):
        self.velocidad_actual = self.velocidad + self.acelerar
        print('self.velocidad_actual: ', self.velocidad_actual)


auto1 = Auto(modelo='Corsa', velocidad_max=120, color='blanco')
auto1.describir()
auto1.velocidad_actual = 100
auto1.estado()

# %%

class Vehiculo:

    # constructor
    def __init__(self, modelo, velocidad_max, color='negro'):
        self.color = color
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.velocidad_actual = 0

    # método que representa algo en modo print()
    def __repr__(self):
        return self.describir()

    def describir(self):
        obj = {
            'color': self.color,
            'modelo': self.modelo,
            'velocidad_max': self.velocidad_max
        }
        return obj

    def estado(self):
        if self.velocidad_actual == 0:
            print('Detenido')
        elif self.velocidad_actual > 0:
            print('Andando a: {} km/h'.format(self.velocidad_actual))
        else:
            print('Marcha atras')

    def izquierda(self):
        print('Izquierda')

    def derecha(self):
        print('derecha')

    def acelerar(self, velocidad):
        self.velocidad_actual += velocidad
    
    def frenar(self, velocidad):
        self.velocidad_actual -= velocidad


vehiculo1 = Vehiculo(modelo='Corsa', velocidad_max=120, color='blanco')
vehiculo1.describir()
vehiculo1.__repr__()

vehiculo1.acelerar(velocidad=100)
vehiculo1.estado()

vehiculo1.frenar(velocidad=90)
vehiculo1.estado()

#%% Herencia de clases

class Autobus(Vehiculo):
    def acelerar(self, velocidad):
        print('Autobus acelerando')

        if velocidad <= self.velocidad_max:
            self.velocidad_actual += velocidad
        else:
            print('Error: Velocidad maxima superada')
    
    def frenar(self, velocidad):
        print('Autobus frenando')
        if velocidad <= self.velocidad_actual:
            self.velocidad_actual -= velocidad
        elif velocidad > self.velocidad_actual:
            print(f'Error: no es posible frenar. Velocidad actual : {self.velocidad_actual} km/h')


autobus1 = Autobus(modelo='AB-1', velocidad_max=100)
autobus1.acelerar(90)
autobus1.describir()
autobus1.frenar(89)
autobus1.describir()
autobus1.estado()