import os
import subprocess


def cleanConsole():
    return os.system("cls")


def rebootSystem():
    return subprocess.call("shutdown -r")


if __name__ == "__main__":
    cleanConsole()
    rebootSystem()
