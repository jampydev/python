



# Pedir al usuario que ingrese una frase
frase_original = input("Por favor, ingresa una frase: ")




# Convertir la frase a minúsculas
frase_minusculas = frase_original.lower()




# Reemplazar todas las vocales por asteriscos (*)
frase_modificada = frase_minusculas.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')



# Calcular la longitud de la frase original y de la frase modificada
longitud_original = len(frase_original)
longitud_modificada = len(frase_modificada)



# Imprimir ambas frases y sus respectivas longitudes
print("Frase original:", frase_original)
print("Longitud de la frase original:", longitud_original)
print("Frase modificada:", frase_modificada)
print("Longitud de la frase modificada:", longitud_modificada)
