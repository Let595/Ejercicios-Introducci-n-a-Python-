n =int(input("Ingrese un número: "))
x= 1
c = 0
while x <= n:
    if n % x == 0:
        c = c + 1
    x = x + 1
if c == 2:
    print("El número ",n," es primo")
else:
    print("El número ",n," no es primo")
    