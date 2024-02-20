# Compreensão de listas
# Sintaxe: [expr for item in lista]
# Forma tradicional de iterar pela lista e realizar as operações sobre cada elemento: 
lista = [1, 2, 3, 4, 5]
lista_numeros_dobrados = []
for numero in lista:
    lista_numeros_dobrados.append(numero * 2)

# Utilizando list comprehension
lista_numeros_dobrados = [x * 2 for x in lista]
print(lista_numeros_dobrados)


    