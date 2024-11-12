S = 'suma'
R = 'resta'
M = 'multiplicacion'
D = 'division'

num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero "))

operador = input("Introduce la operacion a realizar (suma,resta,multiplicacion,division): ")

resultado = 0

if operador == 'suma':
    resultado = num1 + num2
elif operador == 'resta':
    resultado = num1 - num2
elif operador == 'multiplicacion':
   resultado = num1 * num2
elif operador == 'division':
   resultado = num1 / num2

print("El resultado es",resultado )