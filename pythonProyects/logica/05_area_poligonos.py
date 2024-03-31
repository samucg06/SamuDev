import os


def limpiar_consola():
    os.system("cls")
    return


def poligono_usuario():
    try:
        poligono = int(
            input(
                "¿A qué poligono le desea calcular el area?\n\n1. Cuadrado\n2. Rectángulo\n3. Triángulo\n\n==> "
            )
        )
        if poligono != 1 or poligono != 2 or poligono != 3:
            limpiar_consola()
            print("Poligono Invalido\n")
            input("Enter para continuar... ")
            area_poligono()
        else:
            return poligono
    except ValueError:
        limpiar_consola()
        print("Debe ingresar unicamente valores númericos\n")
        input("Enter para continuar... ")
        area_poligono()


def valores_poligono():
    unidad_longitud = input("Ingrese la unidad de medida: ").lower()
    base = float(input("Ingrese la medida de la base del poligono: "))
    altura = float(input("Ingrese la medida de la altura del poligono: "))

    return unidad_longitud, base, altura


def area_poligono():
    limpiar_consola()
    poligono = poligono_usuario()
    limpiar_consola()
    unidad_longitud, base, altura = valores_poligono()
    limpiar_consola()

    if poligono == 1:
        area_cuadrado = base * altura
        print(f"El area del Cuadrado es: {area_cuadrado} {unidad_longitud}^2")
        return
    elif poligono == 2:
        area_rectangulo = base * altura
        print(f"El area del Cuadrado es: {area_rectangulo} {unidad_longitud}^2")
        return
    elif poligono == 3:
        area_triangulo = (base * altura) / 2
        print(f"El area del Cuadrado es: {area_triangulo} {unidad_longitud}^2")
        return


if __name__ == "__main__":
    area_poligono()
