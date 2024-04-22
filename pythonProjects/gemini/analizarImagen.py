import os
import PIL.Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyCgAs97GTGiqS9wqlbSE7aQaxbtKQuFCmk")
model = genai.GenerativeModel("gemini-pro-vision")

imagenes = PIL.Image.open("d://varios//gatos.jpg")
os.system("cls")

response = model.generate_content(
    [
        "Transcribe lo que dice la infografia",
        imagenes,
    ],
    stream=True,
)
response.resolve()
print(response.text)
