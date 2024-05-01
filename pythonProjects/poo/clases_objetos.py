import os


def cleanConsole():
    os.system("cls")


cleanConsole()

"""
class Portatiles():
    cpu = "Intel"
    gpu = "Nvidia"
    motherboard = "ASUS"


portatil_uno = Portatiles()
portatil_dos = Portatiles()
portatil_tres = Portatiles()

print("CPU: " + portatil_uno.cpu)
print("GPU: " + portatil_dos.gpu)
print("MOTHERBOARD: " + portatil_tres.motherboard)
"""


class Portatil:
    def __init__(self, cpu, gpu, motherboard):
        self.cpu = cpu
        self.gpu = gpu
        self.motherboard = motherboard

    def programar(self):
        print(f"Programando en {self.cpu}...")

    def compilar(self):
        print(f"Compilando en {self.gpu}...")


portatil_uno = Portatil("AMD", "Nvidia", "MSI")
portatil_dos = Portatil("Intel", "Nvidia", "ASUS")

portatil_uno.programar()
portatil_dos.compilar()
