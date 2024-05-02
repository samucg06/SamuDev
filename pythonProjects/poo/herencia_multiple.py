class Persona:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")


class Artista:
    def __init__(self, habilidad: str):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")


class EmpleadoArtista(Persona, Artista):
    def __init__(
        self, nombre: str, edad: int, nacionalidad: str, habilidad: str, cargo: str
    ):
        super().__init__(nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.cargo = cargo

    def presentarse(self):
        # return f"{self.mostrar_habilidad()}"
        return f"{super().mostrar_habilidad()}"


samuel = EmpleadoArtista("Samuel", 17, "colombiano", "Programar", "estudiante")
samuel.presentarse()
