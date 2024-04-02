import os
import math


def limpiar_consola():
    os.system("cls")


def numero_primo(numero):
    limpiar_consola()
    if numero < 1:
        print(f"{numero} no es un número primo")
    else:
        for i in range(
            2, int(math.sqrt(numero)) + 1
        ):  # Convertir math.sqrt(n) a entero
            if numero % i == 0:
                print(f"{numero} no es un número primo")
                return  # Salir de la función si encontramos un divisor
        print(f"{numero} es un número primo")


if __name__ == "__main__":
    verificar_numero = int(input("Ingrese un valor: "))
    numero_primo(verificar_numero)
