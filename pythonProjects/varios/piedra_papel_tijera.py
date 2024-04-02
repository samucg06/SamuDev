import random
import getpass

while True:
    password = getpass.getpass("Ingresa la contraseña: ")
    password_int = int(password)
    if password_int == 1:
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")

nombre_maquina = "Binario"
opciones_juego = ("Piedra", "Papel", "Tijeras")
puntajeUser = 0
puntajeMaquina = 0

contador = 0
rounds = 5

while contador < rounds:
    print("*" * 10)
    print(f"Round #{contador + 1}")
    print("*" * 10)

    username_option = input(
        "Ingresa tu nombre y tu elección. Por ejemplo: Samuel, Tijeras ==> "
    )
    nombre_usuario, user_option = username_option.split()
    user_option = user_option.capitalize()

    computer_option = random.choice(opciones_juego)

    print(f"La opción de {nombre_maquina} fue ==> {computer_option}")
    print(f"La opción de {nombre_usuario} fue ==> {user_option}")

    if user_option == computer_option:
        print("¡Es un empate!")
    elif (
        (user_option == "Piedra" and computer_option == "Tijeras")
        or (user_option == "Papel" and computer_option == "Piedra")
        or (user_option == "Tijeras" and computer_option == "Papel")
    ):
        print(f"{user_option} gana a {computer_option}.\n{nombre_usuario} ¡Gana!")
        puntajeUser += 1
    elif (
        (user_option == "Tijeras" and computer_option == "Piedra")
        or (user_option == "Piedra" and computer_option == "Papel")
        or (user_option == "Papel" and computer_option == "Tijeras")
    ):
        print(f"{computer_option} gana a {user_option}.\n{nombre_maquina} ¡Gana!")
        puntajeMaquina += 1
    else:
        print("Opción no válida")

    contador += 1

if puntajeUser > puntajeMaquina:
    print(
        f"¡{nombre_usuario} gana la partida con {puntajeUser} puntos VS {puntajeMaquina} puntos de {nombre_maquina}!"
    )
elif puntajeUser < puntajeMaquina:
    print(
        f"¡{nombre_maquina} gana la partida con {puntajeMaquina} puntos VS {puntajeUser} puntos de {nombre_usuario}!"
    )
else:
    print("¡Esto es un empate!")
