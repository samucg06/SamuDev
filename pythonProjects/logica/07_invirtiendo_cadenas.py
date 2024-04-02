import os


def limpiar_consola():
    os.system("cls")


def string_usuario():
    cadena_texto = input("Ingrese una cadena de texto: ")
    return cadena_texto


def invertir_cadenas():
    limpiar_consola()
    cadena_texto = string_usuario()
    cadena_original = cadena_texto
    limpiar_consola()
    cadena_invertida = str()

    for _ in cadena_texto:
        ultimo_caracter = cadena_texto[-1]
        cadena_invertida += ultimo_caracter
        cadena_texto = cadena_texto[:-1]

    print(f"Cadena original: {cadena_original}")
    print(f"Cadena invertida: {cadena_invertida}")


if __name__ == "__main__":
    invertir_cadenas()
