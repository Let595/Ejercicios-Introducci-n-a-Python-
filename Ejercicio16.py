n = 1
par = impar = 0
while n != 0:
    n = int(input("Ingresa un número: "))
    if n > 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("El total de números pares es: ",par)
print("El total de números impares es: ",impar)