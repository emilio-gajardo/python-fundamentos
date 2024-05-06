# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:59:22 2024

@author: Usuario
"""


def saludar_modulo(nombre):
    print("Hola {}, esta función se ha importado del módulo {}, {}"
          .format(nombre, __file__, __name__))


def felicitar_modulo(nombre):
    print("Felicitaciones {}".format(nombre))


def main():
    saludar_modulo("Tú")


if __name__ == "__main__":
    main()
