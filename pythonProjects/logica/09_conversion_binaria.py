import os


# Definición de una función para limpiar la consola
def limpiarConsola():
    os.system("cls")


# Definición de una función para convertir un número decimal a binario
def conversionBinaria(n):
    residuos = []  # Lista para almacenar los residuos de la división
    cadena_binario = []  # Lista para almacenar los dígitos binarios

    # Bucle para calcular los residuos de la división
    while n != 0:
        residuo = n % 2  # Obtener el residuo de la división por 2
        residuos.append(residuo)  # Agregar el residuo a la lista
        n = n // 2  # Actualizar el número dividiéndolo entre 2 (división entera)

    # Bucle para invertir la lista de residuos y convertirla en una lista de dígitos binarios
    for n in reversed(residuos):
        cadena_binario.append(n)

    # Convertir la lista de dígitos binarios en una cadena
    numero_binario = "".join(map(str, cadena_binario))
    # La función map(str, cadena_binario) convierte cada dígito en una cadena de caracteres
    # La función join() concatena todas estas cadenas en una sola cadena

    return numero_binario


# Función principal que maneja la entrada del usuario y llama a las funciones de conversión
def main():
    limpiarConsola()  # Limpiar la consola
    try:
        numero_usuario = int(
            input("Ingresa un número entero: ")
        )  # Solicitar al usuario que ingrese un número entero
        limpiarConsola()  # Limpiar la consola
        if numero_usuario < 0:
            raise ValueError(
                "Ingrese un número entero positivo"
            )  # Lanzar una excepción si el número es negativo
        numero_binario = conversionBinaria(
            numero_usuario
        )  # Convertir el número entero a binario
        print(
            f"El número {numero_usuario} en binario es: {numero_binario}"
        )  # Imprimir el resultado
    except ValueError as e:
        print(str(e))  # Capturar y manejar excepciones de valor incorrecto


# Comprobar si este script es el script principal que se está ejecutando
if __name__ == "__main__":
    main()  # Llamar a la función principal
