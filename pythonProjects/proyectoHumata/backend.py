from tkinter import filedialog
import docx
import os
import google.generativeai as genai
import pdfplumber


def generar_respuesta(pregunta, texto_pdf, model):
    try:
        response = model.generate_content(
            f"De la siguiente pregunta {pregunta}, responda en base al siguiente texto: {texto_pdf}"
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


def click_directorio(ruta_archivo):
    ruta_archivo = filedialog.askopenfilename()
    print(f"Archivo Seleccionado: {ruta_archivo}")

    if ruta_archivo == "":
        print("Error")
    else:
        extension_pdf, extension_txt, extension_docx = ".pdf", ".txt", ".docx"

        ruta_archivo, extension_archivo = os.path.splitext(ruta_archivo)
        if extension_archivo == extension_pdf:
            extraer_texto_pdf(ruta_archivo + extension_archivo)
        elif extension_archivo == extension_txt:
            extraer_texto_txt(ruta_archivo + extension_archivo)
        elif extension_archivo == extension_docx:
            extraer_texto_docx(ruta_archivo + extension_archivo)
        else:
            print("No es un archivo PDF")


def main():
    genai.configure(api_key="AIzaSyCgAs97GTGiqS9wqlbSE7aQaxbtKQuFCmk")
    model = genai.GenerativeModel("gemini-1.5-pro-latest")


if __name__ == "__main__":
    main()
