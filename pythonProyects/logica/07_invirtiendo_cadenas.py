import os


def limpiar_consola():
    os.system("cls")


def string_usuario():
    cadena_texto = input("Ingrese una cadena de texto: ")
    return cadena_texto


def invertir_cadenas():
    limpiar_consola()
    cadena_texto = string_usuario()
    limpiar_consola()
    palabra_invertida = ""

    for _ in cadena_texto:
        ultimo_caracter = cadena_texto[-1]
        palabra_invertida += ultimo_caracter
        cadena_texto = cadena_texto[:-1]

    print(f"La oración invertida es:\n\n{palabra_invertida}")


if __name__ == "__main__":
    invertir_cadenas()
