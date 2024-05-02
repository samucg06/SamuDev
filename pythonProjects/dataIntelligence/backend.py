from tkinter import filedialog
import google.generativeai as genai
import pdfplumber
import docx
import os


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


def generar_respuesta(pregunta, texto, model):
    try:
        response = model.generate_content(
            f"{pregunta}, responda en base al siguiente texto: {texto}"
        )
        return response.text
    except Exception as e:
        return print(f"Error al generar la respuesta {e}")


def extraer_texto_docx(archivo_docx):
    try:
        doc = docx.Document(archivo_docx)
        texto = ""
        for parrafo in doc.paragraphs:
            texto += parrafo.text
        if texto == "":
            limpiar_consola()
            return print("El archivo .docx no tiene contenido"), exit()
        else:
            return texto
    except Exception as e:
        limpiar_consola()
        return print(f"Estas seguro que es un archivo .docx?\n\nError: {e}"), exit()


def extraer_texto_txt(archivo_txt):
    texto = ""
    with open(archivo_txt, "r") as txt:
        try:
            for linea in txt:
                texto += linea
            if texto == "":
                limpiar_consola()
                return print("El archivo .txt no tiene contenido"), exit()
            else:
                return texto
        except Exception as e:
            limpiar_consola()
            return print(f"Estas seguro que es un archivo .txt?\n\nError: {e}"), exit()


def extraer_texto_pdf(archivo_pdf):
    texto = ""
    try:
        with pdfplumber.open(archivo_pdf) as pdf:
            for pagina in pdf.pages:
                texto += pagina.extract_text()
            if texto == "":
                limpiar_consola()
                return print("El archivo .pdf no tiene contenido"), exit()
            else:
                return texto
    except Exception as e:
        limpiar_consola()
        return print(f"Estas seguro que es un archivo .pdf?\n\nError: {e}"), exit()


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
            return False, ""


def main():
    genai.configure(api_key="AIzaSyCgAs97GTGiqS9wqlbSE7aQaxbtKQuFCmk")
    model = genai.GenerativeModel("gemini-pro")
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        defaultextension=".docx",
        filetypes=[
            ("Todos los archivos", "*.*"),
        ],
    )
    verificacion, texto = verificacion_extension_archivo(ruta_archivo)

    if verificacion:
        while True:
            limpiar_consola()
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
        limpiar_consola()
        print("Hasta Luego")
        exit()
    else:
        limpiar_consola()
        print("Ha ocurrido un error")
        exit()


if __name__ == "__main__":
    main()
