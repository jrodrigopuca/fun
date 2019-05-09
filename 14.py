# Documentación: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup

archivo = open("test.html")
sopa= BeautifulSoup(archivo, "html.parser")

# traer datos
# print(sopa.prettify())    # devuelve todo el html
# print(sopa.get_text())    # devuelve solo el texto

# traer un elemento por su tag:
# print(sopa.title)         # <title>Document</title>
# print(sopa.h1)            # <h1>Hola</h1>

# traer más de un elemento
# print(sopa.find_all('p'))   # [<p> Parrafo 1</p>, <p> Parrafo 2</p>]

