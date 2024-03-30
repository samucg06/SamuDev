import os


def clean_console():
    os.system("cls")


def fizz_buzz():
    clean_console()
    for numero in range(1, 100 + 1):
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)


if __name__ == "__main__":
    fizz_buzz()
