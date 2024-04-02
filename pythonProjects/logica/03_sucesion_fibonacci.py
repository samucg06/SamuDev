import os


def limpiar_consola():
    os.system("cls")


def fibonacci():
    limpiar_consola()
    numero_fibonacci = [0, 1]
    for i in range(2, 50 + 1):
        numero_fibonacci.append(numero_fibonacci[i - 1] + numero_fibonacci[i - 2])
    return print(numero_fibonacci)


if __name__ == "__main__":
    fibonacci()
