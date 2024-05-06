# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:27:55 2024

@author: Usuario
"""

import argparse
from modulo_importable import saludar_modulo, felicitar_modulo

def parsear_argumentos_avanzado():

    parser = argparse.ArgumentParser(
        description="Descripción del script"
    )

    parser.add_argument(
        "metodo",
        help="""Indica el método que se quiere usar.
        Valores válidos son saludar, felicitar""",
        choices=["saludar", "felicitar"]
    )

    parser.add_argument(
        "usuario",
        help="""Indica el usuario con quien se quiere interactuar.""")

    parser.add_argument(
        "--capitalizar", # -- => indica que es argumento opcional
        help="Capitaliza el nombre del usuario",
        action="store_true")

    argumentos = parser.parse_args()
    return argumentos


def main(argumentos):
    nombre = argumentos.usuario

    if argumentos.capitalizar:
        nombre = nombre.capitalize()
        print(nombre)
    if argumentos.metodo == "saludar":
        saludar_modulo(nombre)
    elif argumentos.metodo == "felicitar":
        felicitar_modulo(nombre)


if __name__ == "__main__":
    argumentos = parsear_argumentos_avanzado()
    print("argumentos pasados al script: ", argumentos)
    main(argumentos)
