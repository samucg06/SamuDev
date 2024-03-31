import os


# Función para limpiar la consola (depende del sistema operativo)
def limpiar_consola():
    os.system("cls")  # En Windows, usa "cls" para limpiar la consola


# Función para obtener una cadena de texto ingresada por el usuario
def cadena_texto_usuario():
    cadena = input("Ingrese una cadena de texto: ")
    return cadena


# Función principal para contar las palabras en la cadena
def contar_palabras():
    limpiar_consola()
    cadena = cadena_texto_usuario()

    # Convertir la cadena a minúsculas y dividirla en palabras
    palabras = cadena.lower().split()

    # Crear un diccionario para contar las ocurrencias de cada palabra
    contador = {}
    for palabra in palabras:
        # Eliminar signos de puntuación alrededor de la palabra
        palabra = palabra.strip(".,!?")
        contador[palabra] = contador.get(palabra, 0) + 1

    # Imprimir el recuento final de todas las palabras
    for palabra, frecuencia in contador.items():
        print(f"'{palabra}': {frecuencia} veces")


# Ejecutar la función principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    contar_palabras()
