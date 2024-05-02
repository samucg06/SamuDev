import os


def limpiar_consola():
    os.system("cls")


class Persona:
    def __init__(self, nombre=str, edad=int):
        self.nombre = nombre
        self.edad = edad

    def imprimir_nombre_persona(self):
        print(f"El nombre de la persona es {self.nombre}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, semestre=str):
        super().__init__(nombre, edad)
        self.semestre = semestre

    def imprimir_semestre_estudiante(self):
        print(f"El estudiante esta cursando {self.semestre}")


limpiar_consola()
samuel = Estudiante("Samuel", 17, "1er Semestre")
print(f"Nombre: {samuel.nombre}\nEdad: {samuel.edad}\nSemestre: {samuel.semestre}")
samuel.imprimir_nombre_persona()
samuel.imprimir_semestre_estudiante()
