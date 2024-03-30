import subprocess  # La biblioteca (subprocess) en Python permite ejecutar comandos del sistema operativo y controlar procesos externos desde un programa Python.
import os


def limpiarConsola():
    os.system("cls")


t = 1
s = ""


def turnOff():
    t = float(input("En cuántos minutos desea que se apagué el computador?: ")) * 60
    if t >= 0:
        subprocess.call("shutdown -s -t %d" % t)
        s = input("Desea cancelar la operación?[S/n]: ").capitalize()
        if s == "S":
            subprocess.call("shutdown -a")
            return print("Cancelando operación de apagado")
        else:
            return print("Su computador esta en proceso de apagado")
    else:
        return exit()


if __name__ == "__main__":
    limpiarConsola()
    turnOff()
