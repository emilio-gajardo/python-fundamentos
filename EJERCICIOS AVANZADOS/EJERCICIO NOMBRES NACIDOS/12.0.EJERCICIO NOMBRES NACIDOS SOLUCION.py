# 11-05-2024
#@autor: EJGA

#import pandas as pd
import os
import sys

class BuscarNombre:

    def __init__(self, data_path="./data/"):
        self.data = []
        self.data_path = data_path
        self.file_name_backup = "data_backup.csv"
        self.load_data()


    def load_data(self):
        print("load_data()")

        files_names = [
            {'anio': 2002, 'nombre': 'nomnac02.csv'}, {'anio': 2003, 'nombre': 'nomnac03.csv'}, {'anio': 2004, 'nombre': 'nomnac04.csv'},
            {'anio': 2005, 'nombre': 'nomnac05.csv'}, {'anio': 2006, 'nombre': 'nomnac06.csv'}, {'anio': 2007, 'nombre': 'nomnac07.csv'},
            {'anio': 2008, 'nombre': 'nomnac08.csv'}, {'anio': 2009, 'nombre': 'nomnac09.csv'}, {'anio': 2010, 'nombre': 'nomnac10.csv'},
            {'anio': 2011, 'nombre': 'nomnac10.csv'}, {'anio': 2012, 'nombre': 'nomnac12.csv'}, {'anio': 2013, 'nombre': 'nomnac13.csv'},
            {'anio': 2014, 'nombre': 'nomnac14.csv'}, {'anio': 2015, 'nombre': 'nomnac15.csv'}, {'anio': 2016, 'nombre': 'nomnac16.csv'},
        ]

        try:
            print("⏳ Cargando datos...")

            for file_info in files_names:
                nombre = file_info["nombre"]
                file_path = f"{self.data_path}{nombre}"

                with open(file_path, "r") as file:

                    for line in file:
                        data_row = []
                        data_row = line.strip(" ").strip("\n").split(",")

                        self.data.append({
                            "anio": file_info["anio"],
                            "nombre_hombre": data_row[0].strip(),
                            "nombre_mujer": data_row[1].strip(),
                        })

            if len(self.data) == 0:
                print("> Error: datos no cargados")
                sys.exit()
            else:
                print("> Datos cargados ok...")
                self.create_backup()

        except Exception as e:
            print(f"> Error: al cargar datos \n{e}")
            sys.exit()

    def create_backup(self):
        print("create_backup()")
        path_full = self.data_path+self.file_name_backup

        try:
            os.makedirs(self.data_path, exist_ok = True)
            print("> Creando backup...")
            with open (path_full, "w") as fname:
                fname.write("ANIO, NOMBRE HOMBRE, NOMBRE MUJER\n")
                for item in self.data:
                    anio = item["anio"]
                    nombre_hombre = item["nombre_hombre"]
                    nombre_mujer = item["nombre_mujer"]
                    fname.write(f"{anio}, {nombre_hombre}, {nombre_mujer}\n")
            print("> Backup creado OK")

        except Exception as e:
            print(f"Error: al crear data backup \n{e}")
            sys.exit()

    def validator_load_data(self):
        print("> Validando datos...")

        if len(self.data) == 0:
            print("> Error: no hay datos cargados. Verifique la fuente de datos")
            sys.exit()
        else:
            print("> Validación de datos cargados: OK")
            print(f"> Datos encontrados = {len(self.data)}")
            self.mostrar_titulo()
            self.mostrar_instrucciones()

    def mostrar_titulo(self):
        msg = "\n⏳ Iniciando programa..."
        msg += "\n== EJERCICIO AVANZADO EN PYTHON =="
        msg += "\n== BUSCADOR DE NOMBRES POPULARES =="
        print(msg)


    def mostrar_instrucciones(self):
        msg = "\n> Busca el nombre de los recién nacidos mas populares"
        msg += "\n> Los datos incluidos son de 14 años, desde el 2002 hasta el 2016"
        msg += "\n> El nombre a ingresar no debe tener números, solo letras\n"
        print(msg)
        self.solicitar_input()

    def solicitar_input(self):
        print("> solicitar_input()")
        input_valido = False

        while input_valido == False:
            input_str = input("> Ingresa un nombre a buscar = ")
            if not self.validar_input(input_str):
                input_valido = False
            else:
                input_valido = True
                input_str = input_str.upper()
                self.buscar_nombre(input_str)


    def validar_input(self, input_str):
        print("validar_input()")
        valido = False
        try:
            input_str = input_str.strip(" ")
            if len(input_str) == 0:
                print("> Error: largo de string = 0")
                return False

            if len(input_str) > 0:
                if not input_str.isalpha():
                    print("> Error: el input contiene caracteres que no son letras")
                    return False
                else:
                    return True

        except ValueError as ve:
            print(f"> Error: ValueError: {ve}")
            return False
        except Exception as e:
            print(f"> Error: {e}")
            valido = False
        return valido


    def buscar_nombre(self, nombre):
        print(f"Nombre a buscar: {nombre}")
        print("> Buscando...")
        contador  = 0
        for elemento in self.data:
            for clave, valor in elemento.items():
                if valor == nombre:
                    contador += 1
        if contador == 0:
            print(f"> No se ha encontrado el nombre {nombre}")
        else:
            print(f"> Veces Encontrado = {contador}")


def iniciar_juego():
    buscar = BuscarNombre()
    buscar.validator_load_data()

iniciar_juego()