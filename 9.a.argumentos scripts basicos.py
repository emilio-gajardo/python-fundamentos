# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:48:08 2024

@author: Usuario
"""

import sys
from modulo_importable import saludar_modulo


def parsear_argumentos_basico():
    argumentos = sys.argv[1:]
    return argumentos


def main(argumentos):
    if argumentos[0] == "saludar":
        nombre = argumentos[1]
        saludar_modulo(nombre)


if __name__ == "__main__":
    # este código solo se ejecutaraá si se ejecuta este script directamente
    argumentos = parsear_argumentos_basico()
    print("argumentos pasados al script: ", argumentos)
    main(argumentos)
