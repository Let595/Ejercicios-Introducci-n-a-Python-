texto = input("Ingresa una frase: ")

def numero_palabras(texto):
    texto_limpio = texto.replace(",","")
    palabras = texto_limpio.split()
    numero_palabras = len(palabras)
    return numero_palabras

resultado = numero_palabras(texto)
print(f"La cantidad de palabras de la frase es : {resultado}")