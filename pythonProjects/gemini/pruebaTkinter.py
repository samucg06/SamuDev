import tkinter as tk


# Función para manejar el clic del botón
def hacer_clic():
    print("¡Has hecho clic en el botón!")


# Crear una instancia de la ventana principal
root = tk.Tk()

# Configurar el tamaño de la ventana
root.geometry("300x200")

# Configurar el título de la ventana
root.title("Ejemplo de Tkinter")

# Crear un botón en la ventana
button = tk.Button(root, text="Haz clic aquí", command=hacer_clic)

# Colocar el botón en la ventana
button.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
