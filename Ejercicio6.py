def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[:: -1]

print(es_palindromo('Radar'))
print(es_palindromo('Gatos'))
