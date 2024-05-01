import os


def limpiar_consola():
    os.system("cls")


limpiar_consola()


class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")


nombre_estudiante = input("Ingresa el nombre del estudiante: ").capitalize()
edad_estudiante = int(input("Ingresa la edad del estudiante: "))
grado_estudiante = input("Ingresa el grado del estudiante: ")

estudiante = Estudiante(nombre_estudiante, edad_estudiante, grado_estudiante)

limpiar_consola()

while True:
    accion_estudiante = input("¿Estudiando?: ").lower()

    limpiar_consola()

    if accion_estudiante == "estudiando":
        estudiante.estudiar()
        break
    else:
        input("Presiona una tecla para continuar... ")
        limpiar_consola()
