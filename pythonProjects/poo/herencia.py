class Humano:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def comer(self):
        print(f"{self.nombre} esta comiendo")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo")


class Profesor(Humano):
    def __init__(self, nombre, edad, nacionalidad, materias, cargo):
        # Con la función super() llamamos al constructor de la clase padre
        super().__init__(nombre, edad, nacionalidad)
        self.materias = materias
        self.cargo = cargo


class Cientifico(Humano, Profesor):
    def __init__(self, nombre, edad, nacionalidad, materias, cargo, investigaciones):
        super().__init__(nombre, edad, nacionalidad, materias, cargo)
        self.investigaciones = investigaciones
