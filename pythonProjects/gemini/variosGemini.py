import os
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


os.system("cls")

genai.configure(api_key="AIzaSyCgAs97GTGiqS9wqlbSE7aQaxbtKQuFCmk")
model = genai.GenerativeModel("gemini-1.5-pro-latest")

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)
        pass

response = model.generate_content("Diferencias entre un pato y una gallina")
respuesta = to_markdown(response.text)
print(respuesta.data)
