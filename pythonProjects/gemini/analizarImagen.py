import os
import PIL.Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyCgAs97GTGiqS9wqlbSE7aQaxbtKQuFCmk")
model = genai.GenerativeModel("gemini-pro-vision")

ensaladaFrutas = PIL.Image.open("c://logs//texto.jpg")
os.system("cls")

response = model.generate_content(
    [
        "Si hay una persona en la imagen sin casco, responde solo la palabara NOTIENECASCO",
        ensaladaFrutas,
    ],
    stream=True,
)
response.resolve()
print(response.text)
