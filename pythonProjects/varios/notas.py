import os


def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")


def calcularNotaFinal(cantidad_notas):
    nota_acumulativa = 0
    for n in range(int(cantidad_notas)):
        nota = float(input(f"Ingrese la nota {n+1}: "))
        limpiarConsola()
        porcentaje_nota = float(input(f"Ingrese el porcentaje de la nota {n+1}: "))
        porcentaje_nota = porcentaje_nota / 100
        limpiarConsola()
        nota_acumulativa += nota * porcentaje_nota
    return round(nota_acumulativa, 3)


def calcularNotaFaltante(cantidad_notas, nota_deseada, nota_para_pasar):
    nota_acumulada = 0
    for n in range(cantidad_notas - 1):
        nota = float(input(f"Ingrese la nota {n + 1}: "))
        limpiarConsola()
        porcentaje_nota = float(input(f"Ingrese el porcentaje de la nota {n + 1}: "))
        porcentaje_nota = porcentaje_nota / 100
        limpiarConsola()
        nota_acumulada += nota * porcentaje_nota

    if nota_acumulada >= nota_para_pasar:
        print("¡Felicidades ya pasaste la materia!")
        if nota_acumulada >= nota_deseada:
            print("¡Tu meta se ha cumplido!")
    else:
        nota_para_pasar = nota_para_pasar - nota_acumulada
        nota_deseada = nota_deseada - nota_acumulada
        print(f"Necesitas {nota_para_pasar} en la siguiente nota para pasar la materia")
        print(f"Necesitas {nota_deseada} para llegar a tu meta")


def notas():
    limpiarConsola()
    try:
        eleccion_programa = int(
            input(
                "Qué desea hacer?\n\n1. Calcular Nota Final\n2. Calcular Nota Faltante\n\n==> "
            )
        )
        if eleccion_programa == 1:
            limpiarConsola()
            cantidad_notas = int(input("Ingrese la cantidad de Notas: "))
            limpiarConsola()
            nota_final = calcularNotaFinal(cantidad_notas)
            print(f"La nota final es: {nota_final}")
        elif eleccion_programa == 2:
            cantidad_notas = int(input("Ingrese la cantidad de notas: "))
            nota_deseada = float(input("Ingrese la nota deseada: "))
            nota_para_pasar = float(input("Ingrese la nota para pasar la materia: "))
            calcularNotaFaltante(cantidad_notas, nota_deseada, nota_para_pasar)
    except ValueError:
        print("Por favor, ingrese un número válido.")


if __name__ == "__main__":
    notas()
