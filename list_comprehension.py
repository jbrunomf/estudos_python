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


# Também podemos utilizar funções:
def dobrar(numero):
    return numero * 2

print('Utilizando funcão Dobrar: ', [dobrar(x) for x in lista])
    

lista_nomes = ['Carlos', 'Rafaela', 'Joaquina', 'Maria']
lista_nomes_maiusculos = [nome.upper() for nome in lista_nomes]
print(lista_nomes_maiusculos)