import os


def limpiar_consola():
    os.system("cls")


limpiar_consola()


class Transporte:
    def __init__(self, metodo_transporte=str, tipo_transporte=str):
        self.metodo_transporte = metodo_transporte
        self.tipo_transporte = tipo_transporte

    def movilizarse(self):
        print(
            f"El {self.metodo_transporte} es un tipo de transporte {self.tipo_transporte}"
        )


class Vehiculo(Transporte):
    def __init__(
        self,
        metodo_transporte=str,
        tipo_transporte=str,
        tipo_vehiculo=str,
        tipo_terreno=str,
    ):
        super().__init__(metodo_transporte, tipo_transporte)
        self.tipo_vehiculo = tipo_vehiculo
        self.tipo_terreno = tipo_terreno

    def desplazarse(self):
        print(
            f"El tipo de vehiculo {self.tipo_vehiculo} tiene una facilidad para desplazarse a traves de {self.tipo_terreno}"
        )


camaro = Vehiculo("auto", "terrestre", "deportivo", "asfalto")
camaro.movilizarse()
print()
camaro.desplazarse()
