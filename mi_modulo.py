def saludar(nombre):
    print(f"Hola, {nombre}")

def contar_letras(texto):
    texto_limpio = texto.strip()
    num_letras = len(texto_limpio)
    return num_letras

def contar_nombres(texto):
    palabras = texto.split()
    return len(palabras)


def contar_consonantes(texto):
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    texto_minusc = texto.lower()
    contador = 0
    for caracter in texto_minusc:
        if caracter in consonantes:
            contador += 1
            
    return contador 
#con len se evita el for y con strip 


