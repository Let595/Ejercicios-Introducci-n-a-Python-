def sumar_lista(lista):
    suma = 0

    for numero in lista:
        suma += numero
    return suma

numeros = [1,3,5,7,9,11,13,15]

print(sumar_lista(numeros))
