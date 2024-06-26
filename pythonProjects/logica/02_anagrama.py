import os


def limpiar_consola():
    os.system("cls")


def ingresar_palabras():
    palabra_uno = input("Ingresa un Palabra: ").lower()
    palabra_dos = input("Ingresa otra palabra: ").lower()
    return palabra_uno, palabra_dos


def anagrama():
    limpiar_consola()
    palabra_uno, palabra_dos = ingresar_palabras()

    if palabra_uno == palabra_dos:
        return print("No es un anagrama")
    # La función set() en Python se utiliza para crear un conjunto, que es una colección desordenada de elementos únicos.
    if set(palabra_uno) == set(palabra_dos):
        return print("Es un anagrama")
    else:
        return print("No es un anagrama")


if __name__ == "__main__":
    anagrama()
