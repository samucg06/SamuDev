from tkinter import filedialog
import docx
import os
import docx.document
import google.generativeai as genai
import pdfplumber


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


def generar_respuesta(pregunta, texto, model):
    try:
        response = model.generate_content(
            f"{pregunta}, responda en base al siguiente texto: {texto}"
        )
        return response.text
    except Exception as e:
        print(f"Error al generar la respuesta {e}")
        return "Error al generar la respuesta."


def extraer_texto_docx(archivo_docx):
    doc = docx.Document(archivo_docx)
    texto = ""
    for parrafo in doc.paragraphs:
        texto += parrafo.text
    return texto


def extraer_texto_txt(archivo_txt):
    texto = ""
    with open(archivo_txt, "r") as txt:
        for linea in txt:
            texto += linea
        return texto


def extraer_texto_pdf(archivo_pdf):
    texto = ""
    with pdfplumber.open(archivo_pdf) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text()
        return texto


def verificacion_extension_archivo(ruta_archivo):
    if ruta_archivo == "":
        print("Error")
        return False
    else:
        extension_pdf, extension_txt, extension_docx = ".pdf", ".txt", ".docx"

        ruta_archivo, extension_archivo = os.path.splitext(ruta_archivo)
        if extension_archivo == extension_pdf:
            texto = extraer_texto_pdf(ruta_archivo + extension_archivo)
            return True, texto
        elif extension_archivo == extension_txt:
            texto = extraer_texto_txt(ruta_archivo + extension_archivo)
            return True, texto
        elif extension_archivo == extension_docx:
            texto = extraer_texto_docx(ruta_archivo + extension_archivo)
            return True, texto
        else:
            print("No es un archivo PDF")
            return False, ""


def main():
    genai.configure(api_key="AIzaSyCgAs97GTGiqS9wqlbSE7aQaxbtKQuFCmk")
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    ruta_archivo = filedialog.askopenfilename()
    print(f"Archivo Seleccionado: {ruta_archivo}")
    verificacion, texto = verificacion_extension_archivo(ruta_archivo)

    if verificacion:
        while True:
            pregunta_usuario = input("Ingrese una pregunta: ")
            limpiar_consola()
            respuesta = generar_respuesta(pregunta_usuario, texto, model)
            print(respuesta, "\n")
            siguiente_pregunta = input(
                "¿Desea ingresar otra pregunta (si/no)?: "
            ).lower()

            if siguiente_pregunta == "si":
                continue
            elif siguiente_pregunta == "no":
                break
            else:
                print("Respuesta invalida.")
                input("Enter para continuar...")

        print("Hasta Luego")
        exit()
    else:
        exit()


if __name__ == "__main__":
    main()
