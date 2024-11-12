peso=float(input("Ingrese su peso"))
estatura=float(input("Ingrese su estatura"))
imc=peso/estatura

if imc < 18.5:
    print("Su peso es bajo")
elif imc > 18.5 and imc < 25:
    print("Su peso es normal")
elif imc > 25 and imc < 30:
    print("Sobrepeso")
elif imc > 30:
    print("Obeso")

