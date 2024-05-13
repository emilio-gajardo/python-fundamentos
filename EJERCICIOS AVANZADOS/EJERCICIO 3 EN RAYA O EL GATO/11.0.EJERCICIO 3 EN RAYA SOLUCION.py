# -*- coding: utf-8 -*-
"""Created on Wed May  8 13:13:19 2024
# @author: Usuario"""

import sys


class Tablero:

    def __init__(self, f1c1="", f1c2="", f1c3="", f2c1="", f2c2="", f2c3="", f3c1="", f3c2="", f3c3="", turno=1):
        self.f1c1 = f1c1
        self.f1c2 = f1c2
        self.f1c3 = f1c3
        self.f2c1 = f2c1
        self.f2c2 = f2c2
        self.f2c3 = f2c3
        self.f3c1 = f3c1
        self.f3c2 = f3c2
        self.f3c3 = f3c3
        self.turno = turno

    def to_string(self):
        msg = ""
        msg += "\n"
        msg += f"[f1c1: {self.f1c1}]  [f1c2: {self.f1c2}]  [f1c3: {self.f1c3}]\n"
        msg += f"[f2c1: {self.f2c1}]  [f2c2: {self.f2c2}]  [f2c3: {self.f2c3}]\n"
        msg += f"[f3c1: {self.f3c1}]  [f3c2: {self.f3c2}]  [f3c3: {self.f3c3}]\n"
        print (msg)

    def mostrar_titulo_instrucciones(self):
        msg = "\n== EJERCICIO AVANZADO - JUEGO DEL GATO (#) 😸 ==\n"
        msg += "\nInstrucciones:\n"
        msg += "\n1) Participan 2 jugadores"
        msg += "\n2) El jugador 1 marca con una [X]"
        msg += "\n3) El jugador 2 marca con una [0]"
        msg += "\n4) El Ganador tiene 3 marcas consecutivas en línea recta\n"
        print(msg)

    def mostrarTablero(self):
        tablero = "────────────────────────────────────────"
        tablero += "\nVista del tablero:\n"
        tablero += "             ┌────────┬────────┬────────┐\n"
        tablero += "             │ Col 1  │  Col 2 │  Col 3 │\n"
        tablero += "             ├────────┼────────┼────────┤\n"
        tablero += f"Fila 1            {self.f1c1}        {self.f1c2}       {self.f1c3} \n"
        tablero += "             ├────────┼────────┼────────┤\n"
        tablero += f"Fila 2            {self.f2c1}        {self.f2c2}       {self.f2c3} \n"
        tablero += "             ├────────┼────────┼────────┤\n"
        tablero += f"Fila 3            {self.f3c1}        {self.f3c2}       {self.f3c3} \n"
        tablero += "             └────────┴────────┴────────┘\n"
        # tablero += f"Turno: {self.turno}"
        tablero += "\n────────────────────────────────────────\n"
        print(tablero)
        #self.to_string()

    def inicar_o_salir(self):
        validador = False

        while validador == False:
            msg = "\nOpciones del juego:"
            msg += "\nPara salir   = 0"
            msg += "\nPara iniciar = 1"
            msg += "\n🔎 Ingrese opción = "
            input_str = input(msg)
            input_str = input_str.strip(" ")

            if self.validar_opcion_inicio(input_str):
                validador = True
                input_int = int(input_str)
            else:
                validador = False
                self.print_invalido("Ha ingresado un valor no permitido")

        if validador:
            if input_int == 0:
                self.salir_del_juego()

            if input_int == 1:
                print("\n⏳ Iniciando partida...")
                self.solicitar_ingresar_movimiento()

    def solicitar_ingresar_movimiento(self):
        print("\nIngrese un movimiento = fila, columna. Ejemplo: 1,1")
        print(f"🎯 Su turno actual es el = {self.turno}")
        validador = False

        while validador == False:
            entrada = input("🔎 Ingrese movimiento = ")
            if self.validar_entrada(entrada):
                validador = True
                print("\n")
            else:
                validador = False
                self.print_invalido("Ha ingresado un valor no válido")

    def validar_entrada(self, entrada):
        validador = False

        if not self.validar_input_vacio(entrada):
            validador = False

        if self.validar_input_vacio(entrada):

            if "," not in entrada:
                validador = False

            if "," in entrada:
                valores = entrada.strip().split(",")

                if len(valores) != 2:
                    validador = False

                if len(valores) == 2:
                    try:
                        fila = int(valores[0])
                        columna = int(valores[1])
                    except ValueError:
                        validador = False

                    if fila not in [1, 2, 3] or columna not in [1, 2, 3]:
                        validador = False
                    else:
                        validador = True
                        #self.print_valido()
                        self.validar_movimiento(fila, columna)

        return validador

    def validar_movimiento(self, fila, columna):
        valido = False
        jugador_x = Jugador(marcador="X")
        jugador_o = Jugador(marcador="O")
        marcador = ""

        marcadores = {
            1: jugador_x.marcador, 3: jugador_x.marcador, 5: jugador_x.marcador, 7: jugador_x.marcador, 9: jugador_x.marcador,
            2: jugador_o.marcador, 4: jugador_o.marcador, 6: jugador_o.marcador, 8: jugador_o.marcador
        }

        while (not valido or self.turno < 10):

            marcador = marcadores[self.turno]
            print(f">> self.turno = {self.turno}")
            print(f">> marcador = {marcador}")

            # Fila 1
            if fila == 1 and columna == 1 and self.f1c1 == "":
                self.f1c1 = marcador
                self.turno += 1
                valido = True
                self.validar_movimientos_ganadores()

            elif fila == 1 and columna == 2 and self.f1c2 == "":
                self.f1c2 = marcador
                self.turno += 1
                valido = True
                self.validar_movimientos_ganadores()

            elif fila == 1 and columna == 3 and self.f1c3 == "":
                print(f">> f1c3 = {self.f1c3}")
                self.f1c3 = marcador
                print(f">> f1c3 = {self.f1c3}")
                self.turno += 1
                valido = True
                self.validar_movimientos_ganadores()

            # Fila 2
            elif fila == 2 and columna == 1 and self.f2c1 == "":
                self.f2c1 = marcador
                self.turno += 1
                valido = True
                self.validar_movimientos_ganadores()

            elif fila == 2 and columna == 2 and self.f2c2 == "":
                self.f2c2 = marcador
                self.turno += 1
                valido = True
                self.validar_movimientos_ganadores()

            elif fila == 2 and columna == 3 and self.f2c3 == "":
                self.f2c3 = marcador
                self.turno += 1
                valido = True
                self.validar_movimientos_ganadores()

            # Fila 3
            elif fila == 3 and columna == 1 and self.f3c1 == "":
                self.f3c1 = marcador
                self.turno += 1
                valido = True
                self.validar_movimientos_ganadores()

            elif fila == 3 and columna == 2 and self.f3c2 == "":
                self.f3c2 = marcador
                self.turno += 1
                valido = True

                self.validar_movimientos_ganadores()

            elif fila == 3 and columna == 3 and self.f3c3 == "":
                self.f3c3 = marcador
                self.turno += 1
                valido = True
                self.validar_movimientos_ganadores()

            if valido == False:
                self.print_invalido("Movimiento ingresado no permitido")
                print("\nRevise tablero actual")
                self.mostrarTablero()
                self.solicitar_ingresar_movimiento()

            elif valido == True and self.turno <= 10:
                self.mostrarTablero()
                self.solicitar_ingresar_movimiento()


    def print_valido(self, msg=""):
        print(f"✅ Válidado \n{msg}")

    def print_invalido(self, msg):
        print(f"❌ Opción inválida. {msg}")

    def validar_movimientos_ganadores(self):
        self.to_string()
        posiciones = [
            [self.f1c1, self.f1c2, self.f1c3],  # Fila 1
            [self.f2c1, self.f2c2, self.f2c3],  # Fila 2
            [self.f3c1, self.f3c2, self.f3c3],  # Fila 3
            [self.f1c1, self.f2c1, self.f3c1],  # Columna 1
            [self.f1c2, self.f2c2, self.f3c2],  # Columna 2
            [self.f1c3, self.f2c3, self.f3c3],  # Columna 3
            [self.f1c1, self.f2c2, self.f3c3],  # Diagonal 1
            [self.f3c1, self.f3c2, self.f3c3],  # Diagonal 2
        ]

        ganador_encontrado = False

        for combinacion in posiciones:
            if all(p == "X" for p in combinacion):
                ganador = "X"
                print(">> Ganador = X")
                ganador_encontrado = True
                self.mostrar_ganador(ganador)
                break
            elif all(p == "O" for p in combinacion):
                ganador = "O"
                print(">> Ganador = O")
                ganador_encontrado = True
                self.mostrar_ganador(ganador)
                break

        if not ganador_encontrado:
            print(">> No hay Ganador")

        return ganador_encontrado

    def validar_input_vacio(self, cadena):
        cadena = cadena.strip(" ")
        if len(cadena) > 0:
            return True
        else:
            return False

    def validar_entero(self, input_str):
        try:
            int(input_str)
            return True
        except ValueError:
            return False

    def validar_opcion_inicio(self, input_str):

        # 1) Validar largo de caracteres
        if len(input_str) == 0:
            validador = False

        # 2) Validar si es entero
        if self.validar_entero(input_str):

            # 3) Validar si es 1 o 0
            input_int = int(input_str)
            if input_int == 0 or input_int == 1:
                validador = True
            else:
                validador = False
        else:
            validador = False

        return validador

    def mostrar_ganador(self, marca_ganador):
        msg = ""
        msg += "\n💎💎💎💎💎💎💎💎💎💎💎💎💎\n"
        msg += "\n🏆 ¡Felicidades! 🏆"
        msg += f"\nEl ganador es el jugador [ {marca_ganador} ] \n"
        msg += "\n💎💎💎💎💎💎💎💎💎💎💎💎💎"
        print(msg)
        self.salir_del_juego()

    def salir_del_juego(self):
        print("\n👋 Adios...")
        sys.exit()


class Jugador:
    def __init__(self, marcador):
        self.marcador = marcador


def iniciarJuego():
    print("⏳ Iniciando juego...")
    tablero1 = Tablero()

    tablero1.mostrar_titulo_instrucciones()
    tablero1.mostrarTablero()
    tablero1.inicar_o_salir()

iniciarJuego()