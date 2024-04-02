import os
import cmath
import matplotlib.pyplot as plt


def cleanConsole():
    return os.system("cls" if os.name == "nt" else "clear")


def funciones():
    cleanConsole()
    nombre_usuario = input("Ingrese su Nombre: ").title()
    cleanConsole()
    print(f"Bienvenido {nombre_usuario} al mejor tabulador de funciones.")
    funcion = int(
        input(
            f"\n¿Qué tipo de función tienes?\n\n1. Función Constante\n2. Función Lineal\n3. Función Cuadratica\n4. Función Exponencial\n5. Función Valor Absoluto\n6. Función Radical\n7. Función Logaritmica\n\n==> "
        )
    )
    cleanConsole()

    if funcion == 1:
        return funcionConstante()
    elif funcion == 2:
        return funcionLineal()
    elif funcion == 3:
        return funcionCuadratica()
    elif funcion == 4:
        return funcionExponencial()
    elif funcion == 5:
        return funcionValorAbsoluto()
    elif funcion == 6:
        return funcionRadical()
    elif funcion == 7:
        return funcionLogaritmica()
    else:
        return print("\nFunción no válida")


def tablaDeValores():
    minimo_tabla_valores = int(
        input("Ingrese el valor mínimo de la Tabla de Valores: ")
    )
    maximo_tabla_valores = int(
        input("\nIngrese el valor máximo de la Tabla de Valores: ")
    )
    cleanConsole()
    return minimo_tabla_valores, maximo_tabla_valores


def graficarFunciones(tipo_funcion, valor_x, valor_y):
    # Tabular valores de la función
    print("\nValores tabulados de la función:")
    for x, y in zip(valor_x, valor_y):
        print(f"\nf({x}) = {y}")

    # Graficar función
    plt.plot(valor_x, valor_y)

    # Agregar etiquetas y título
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title(f"Grafica de la Función {tipo_funcion}")


    # Trazar líneas verticales y horizontales para dividir el gráfico en 4 cuadrantes
    plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y=0
    plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x=0
    plt.grid(True)  # Mostrar cuadrícula

    plt.xticks(valor_x) # Especificar las ubicaciones de los marcadores en el eje x
    plt.yticks(valor_y) # Especificar las ubicaciones de los marcadores en el eje y
    # Mostrar el gráfico
    plt.show()


def funcionConstante():
    print(
        "\nLa fórmula general de las funciones constantes es:\n\nf(x) = c\n\nDonde C es una constante."
    )
    input("\nEnter para continuar... ")
    CONSTANTE_C = int(input("\nIngresa la Constante C: "))
    minimo, maximo = tablaDeValores()
    valor_x = list(range(minimo, maximo + 1))
    funcion_constante = [CONSTANTE_C] * len(valor_x)
    print(f"La función constante es: f(x) = {CONSTANTE_C}")
    graficarFunciones("Constante", valor_x, funcion_constante)


def funcionLineal():
    print(
        "La formula general de las funciones lineales es: \n\nf(x) = mx+b\n\nDonde M es la pendiente de la recta y B es la ordenada al origen."
    )
    pendiente = int(input("\nIngresa la pendiente de la función: "))
    if pendiente == 0:
        cleanConsole()
        print(
            "Tu función es una función constante, tiene pendiente 0... Te redireccionaré a el modulo correcto."
        )
        input("Enter para continuar... ")
        return funcionConstante()
    else:
        ordenada = int(input("\nIngresa la ordenada al Origen: "))
        cleanConsole()
        minimo, maximo = tablaDeValores()
        valor_x = list(range(minimo, maximo + 1))
        funcion_lineal = [(pendiente * x) + ordenada for x in valor_x]
        print(f"La función lineal es: f(x) = {pendiente}x + {ordenada}")
        graficarFunciones("Lineal", valor_x, funcion_lineal)


def funcionCuadratica():
    print(
        "La formula general de las funciones cuadraticas es: \n\nf(x) = ax^2+bx+c\n\nDonde A, B y C son constantes y A != 0."
    )
    CONSTANTE_A = int(input("\nIngrese el valor de la constante a: "))
    if CONSTANTE_A == 0:
        cleanConsole()
        print(
            "Tu función es un función lineal, tiene constante a con valor 0... Te redireccionaré al modulo correcto."
        )
        input("Enter para continuar... ")
        return funcionLineal()
    else:
        CONSTANTE_B = int(input("\nIngrese el valor de la constante bn: "))
        CONSTANTE_C = int(input("\nIngrese el valor de la constante c: "))
        cleanConsole()
        minimo, maximo = tablaDeValores()
        valor_x = list(range(minimo, maximo + 1))
        funcion_cuadratica = [
            (CONSTANTE_A * (x) ** 2) + (CONSTANTE_B * x) + CONSTANTE_C for x in valor_x
        ]
        print(
            f"La función cuadrática es: f(x) = {
                CONSTANTE_A}x^2 + {CONSTANTE_B}x + {CONSTANTE_C}"
        )
        graficarFunciones("Cuadratica", valor_x, funcion_cuadratica)


def funcionExponencial():
    print(
        "La formula general de las funciones exponenciales es:\n\nf(x) = a * b^x\n\nDonde A y B son constantes y B es la base de la función."
    )
    CONSTANTE_A = int(input("\nIngrese el valor de la constante a: "))
    BASE_FUNCION = int(input("\nIngrese el valor de la base de la función: "))
    cleanConsole()
    minimo, maximo = tablaDeValores()
    valor_x = list(range(minimo, maximo + 1))
    funcion_exponencial = [CONSTANTE_A * (BASE_FUNCION) ** x for x in valor_x]
    print(f"La función exponencial es: f(x) = {CONSTANTE_A * BASE_FUNCION^valor_x}")
    graficarFunciones("Exponencial", valor_x, funcion_exponencial)


def funcionValorAbsoluto():
    print(
        "La formula general de las funciones con valor absoluto es:\n\nf(x) = |x|\n\nDonde la función devuelve el valor absoluto de X"
    )
    input("\nEnter para continuar... ")
    cleanConsole()
    minimo, maximo = tablaDeValores()
    valor_x = list(range(minimo, maximo + 1))
    funcion_valor_absoluto = [abs(x) for x in valor_x]
    print("La función valor absoluto es: f(x) = |x|")
    graficarFunciones("Valor Absoluto", valor_x, funcion_valor_absoluto)


def funcionRadical():
    print(
        "La formula general de las funciones radicales es:\n\nf(x) = \u221Aax+b+c\n\nDonde A, B y C son constantes reales, y X es la variable independiente."
    )
    CONSTANTE_A = int(input("\nIngrese el valor de la constante a: "))
    CONSTANTE_B = int(input("\nIngrese el valor de la constante b: "))
    CONSTANTE_C = int(input("\nIngrese el valor de la constante c: "))
    cleanConsole()
    minimo, maximo = tablaDeValores()
    valor_x = list(range(minimo, maximo + 1))
    funcion_radical = [
        cmath.sqrt(CONSTANTE_A * x + CONSTANTE_B) + CONSTANTE_C for x in valor_x
    ]
    print(
        f"La función radical es: f(x) = sqrt({
            CONSTANTE_A}x + {CONSTANTE_B}) + {CONSTANTE_C}")
    graficarFunciones("Radical", valor_x, funcion_radical)


def funcionLogaritmica():
    print(
        "La formula general de las funciones logaritmicas es:\n\nf(x) = log\u2098(x)\n\nDonde M es la base del algoritmo."
    )
    base_algoritmo = int(input("\nIngrese la base del Algoritmo: "))
    if base_algoritmo <= 1:
        cleanConsole()
        print("La base del algoritmo no puede tener valores menores o iguales a 1")
        print("\nTe aconsejo intentar con base logaritmo mayor a 1")
        input("\nEnter para continuar... ")
        funcionLogaritmica()
    else:
        cleanConsole()
        minimo, maximo = tablaDeValores()
        valor_x = list(range(minimo, maximo + 1))
        funcion_logaritmica = [cmath.log(x, base_algoritmo) for x in valor_x]
        print(f"La función logarítmica es: f(x) = log{base_algoritmo}(x)")
        graficarFunciones("Logaritmica", valor_x, funcion_logaritmica)


if __name__ == "__main__":
    funciones()
