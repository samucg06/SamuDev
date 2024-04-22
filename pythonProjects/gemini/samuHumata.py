import os
import google.generativeai as genai
from tkinter import filedialog
import tkinter as tk
import pdfplumber


def limpiar_consola():
    os.system("cls")


def extraer_texto_pdf(archivo_pdf):
    texto = ""
    with pdfplumber.open(archivo_pdf) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text()


def click_directorio(archivo_pdf_directorio):
    archivo_pdf_directorio = filedialog.askopenfilename()

    if archivo_pdf_directorio != "":
        print("Error")
    else:
        extraer_texto_pdf(archivo_pdf_directorio)


def interfaz_grafica():
    interfaz = tk.Tk()
    entrada = tk.StringVar(interfaz)

    # Dimensiones: Ancho x Alto
    interfaz.geometry(f"300x600")
    # Color del Fondo
    interfaz.configure(background="black")
    # Titulo de la Ventana de la Interfaz
    tk.Wm.wm_title(interfaz, "SamuHumata")

    label_directorio = ""

    # Botones
    boton_directorio = tk.Button(
        # Lugar en donde estara el Botón
        interfaz,
        # Contenido del Botón
        text="Click Me!",
        # Fuente y tamaño del contenido
        font=("Courier", 14),
        # Color del fondo del Botón
        bg="#A3FBC7",
        # Color de la fuente
        fg="black",
        # Función del Botón
        command=lambda: click_directorio(label_directorio),
        # Relieve del Butón
        relief="flat",
    )
    boton_directorio.pack(
        # Relleno del Botón a lo largo y ancho
        fill=tk.BOTH,
        # Expandir Botón
        expand=True,
    )

    # Etiquetas
    tk.Label(
        interfaz,
        # Contenido de la Etiqueta
        text="Welcome to SamuHumata!",
        font=("Courier", 14),
        bg="black",
        fg="white",
        # Centrar el contenido de la Etiqueta
        justify="center",
    ).pack(
        # Relleno del Botón a lo largo y ancho
        fill=tk.BOTH,
        # Expandir Botón
        expand=True,
    )

    # Entradas de Texto
    tk.Entry(
        font=("Courier", 14),
        bg="gray",
        fg="black",
        justify="center",
        textvariable=entrada,
    ).pack(
        fill=tk.BOTH,
        expand=True,
    )

    interfaz.mainloop()


def main():
    pass


if __name__ == "__main__":
    interfaz_grafica()
