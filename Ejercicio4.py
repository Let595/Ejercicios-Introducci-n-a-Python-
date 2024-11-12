texto = input('Ingrese una palabra')
vocales = 'aeiou'
j = 0
for i in texto:
    if i in vocales:
        j = j + 1

print(f'La frase tiene {j} vocales')
