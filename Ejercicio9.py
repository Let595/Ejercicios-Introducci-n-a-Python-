def convertir_dolares_a_euros(dolares,tipo_cambio):
    euros = dolares * tipo_cambio
    return euros

tipo_cambio = 0.85
# 1 dolar = 0.85 euros

dolares = float(input("Ingrese la cantidad de dolares a convertir a euros: "))
euros =convertir_dolares_a_euros(dolares,tipo_cambio)

print(f"{dolares} dolares son {euros:.2f} euros.")