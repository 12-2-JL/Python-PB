import re

try:
    with open("Texton.txt", "r") as file:
        text=file.read()

except FileNotFoundError:
    print("not a single observable file in sight")


def dox(patron):
    try:
      encuentros=re.findall(patron, text)
      return encuentros
    except:
        print("not a single functional code in sight")
   


Numeros=r"\d{2}\s\d{3}\s\d{3}\s\d{4}"
Tarjetas_de_credito=r"\d{4}\s\d{4}\s\d{4}\s\d{4}"
CURPs=r"\b[A-Z]{4}\d{6}[A-Z]{7}\d"
contraseñas=r"((*[a-z])(*[A-Z])(*[0-9])(*[!;#$%&'()*+,-./:;<=>?@^_{}~ ])){8}"
URLs=r"\bhttps://[^\s]+"

print("se encontraron los siguientes números:", dox(Numeros))
print("se encontraron las siguientes Tarjetas_de_credito:", dox(Tarjetas_de_credito))
print("se encontraron los siguientes CURPs:", dox(CURPs))
print("se encontraron las siguientes contraseñas:", dox(contraseñas))
print("se encontraron los siguientes URLs:", dox(URLs))
