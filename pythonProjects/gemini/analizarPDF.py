import os
import pdfplumber
import google.generativeai as genai
import time


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


def tiempo_compilacion():
    inicio = time.time()
    final = time.time()
    compilacion = final - inicio
    return compilacion


def extraer_texto_pdf(ruta_pdf):
    """
    Extrae el texto de un archivo PDF.

    Args:
        ruta_pdf (str): Ruta del archivo PDF.

    Returns:
        str: Texto extraído del PDF.
    """
    texto = ""
    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text()
    return texto


def verificar_existencia_archivo(ruta_archivo):
    """
    Verifica si un archivo existe.

    Args:
        ruta_archivo (str): Ruta del archivo.

    Returns:
        bool: True si el archivo existe, False en caso contrario.
    """
    return os.path.exists(ruta_archivo)


def validar_ruta_pdf(ruta_pdf):
    """
    Valida si la ruta proporcionada corresponde a un archivo PDF.

    Args:
        ruta_pdf (str): Ruta del archivo PDF.

    Returns:
        bool: True si la ruta es válida, False en caso contrario.
    """
    return ruta_pdf.lower().endswith(".pdf")


def validar_pregunta(pregunta):
    """
    Valida si la pregunta ingresada por el usuario no está vacía.

    Args:
        pregunta (str): Pregunta ingresada por el usuario.

    Returns:
        bool: True si la pregunta es válida, False en caso contrario.
    """
    return pregunta.strip() != ""


def generar_respuesta(pregunta, texto_pdf, model):
    """
    Genera una respuesta a una pregunta utilizando un modelo de lenguaje.

    Args:
        pregunta (str): Pregunta del usuario.
        texto_pdf (str): Texto extraído del PDF.
        model: Modelo de lenguaje.

    Returns:
        str: Respuesta generada por el modelo de lenguaje.
    """
    try:
        response = model.generate_content(
            f"De la siguiente pregunta {pregunta}, responda en base al siguiente texto: {texto_pdf}"
        )
        return response.text
    except Exception as e:
        print(f"Error al generar la respuesta: {e}")
        return "Error al generar la respuesta."


def mostrar_respuesta(respuesta):
    """
    Muestra la respuesta generada por el modelo de lenguaje al usuario.

    Args:
        respuesta (str): Respuesta generada por el modelo de lenguaje.
    """
    print(respuesta)
    print("-" * 80)


def main():
    compilacion = tiempo_compilacion()
    genai.configure(api_key="AIzaSyCgAs97GTGiqS9wqlbSE7aQaxbtKQuFCmk")
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    while True:
        limpiar_consola()
        print(compilacion, "\n")
        ruta_pdf = input("Ingrese la ruta del PDF que desea analizar: ").replace(
            "\\", "/"
        )

        if not validar_ruta_pdf(ruta_pdf):
            print("Error: La ruta no corresponde a un archivo PDF.")
            continue

        if not verificar_existencia_archivo(ruta_pdf):
            print("Error: El archivo PDF no existe.")
            continue

        texto_pdf = extraer_texto_pdf(ruta_pdf)

        while True:
            limpiar_consola()
            pregunta = input("Ingrese una pregunta: ")

            if not validar_pregunta(pregunta):
                print("Error: La pregunta no puede estar vacía.")
                continue

            respuesta = generar_respuesta(pregunta, texto_pdf, model)
            mostrar_respuesta(respuesta)

            pregunta_continuar = input("¿Desea ingresar otra pregunta? (si/no): ")
            if pregunta_continuar.lower() != "si":
                break

        pregunta_salir = input("¿Desea salir del programa? (si/no): ")
        if pregunta_salir.lower() == "si":
            break

    limpiar_consola()
    print("¡Hasta luego!")


if __name__ == "__main__":
    main()
