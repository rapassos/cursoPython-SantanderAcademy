#ESTRUTURA DE DADOS
print('ESTRUTURA DE DADOS\n')

#Listas - são estruturas de dados organizadas, mutáveis e que permitem armazenar uma coleção de elementos
print('Listas - são estruturas de dados organizadas, mutáveis e que permitem armazenar uma coleção de elementos\n')

#Criação e acesso
print('Criação e acesso')

frutas = ["maçã", "banana", "laranja","abacate"]
print('frutas = ["maçã", "banana", "laranja","abacate"]\n')

print('Permite acessar utilizando o indice do elemento entre [], iniciando em 0')
print('print(frutas[0]) =',frutas[0])
print('print(frutas[1]) =',frutas[1])

print('É possível acessar em ordem reversa, utilizando indices negativos, -1 representa o último item, -2 o penúltimo, etc')
print('print(frutas[-1]) =',frutas[-1])
print('print(frutas[-3]) =',frutas[-3],'\n')

#Métodos de listas
print('Métodos de listas')
print('A linguagem python tem métodos incorporados as listas, os mais comuns são:')

frutas = ["maçã", "banana", "laranja","abacate"]
print('frutas = ["maçã", "banana", "laranja","abacate"]\n')

print('- .append(elemento) - Adiciona um elemento ao final da lista')
frutas.append("pera")
print('\tfrutas.append("pera") resulta em =',frutas)


print('- .insert(indice,elemento) - insere um elemento em uma posição específica da lista')
frutas.insert(1,"uva")
print('\tfrutas.insert(1,"uva") resulta em =',frutas)

print('- .remove(elemento) - remove um alemento da lista')
frutas.remove("banana")
print('\tfrutas.remove("banana") resulta em =',frutas)

print('- .pop(indice) - retorna um elemento especifico da lista e remove este elemento')
print('\tfrutas.pop(2) retorna =',frutas.pop(2),'e resulta em =',frutas)

print('- .sort() - ordena os elemento da lista em ordem ascendente')
frutas.sort()
print('\tfrutas.sort() resulta em =',frutas)

print('- .reverse() - ordena os elemento da lista em ordem inversa')
frutas.reverse()
print('\tfrutas.reverse() resulta em =',frutas)

#Listas de compreenssão - É uma forma consisa de criar novas listas baseadas em listas existentes, permitindo filtrar e trasnformar os elementos em uma única linha
print('Listas de compreenssão - É uma forma consisa de criar novas listas baseadas em listas existentes, permitindo filtrar e trasnformar os elementos em uma única linha\n')

print('nova_lista = [<<expressão>> for <<elemento>> in <<sequência>> if <<condição>>]')
print('Exemplo:\n')
numeros = [1, 2, 3, 4, 5]
print('numeros = [1, 2, 3, 4, 5]')
quadrado_pares = [x ** 2 for x in numeros if x % 2 == 0]
print('quadrado_pares = [x ** 2 for x in numeros if x % 2 == 0] resulta em =',quadrado_pares)
print('Neste exemplo foi criada a lista quadrado_pares contendo o quadrado dos numeros pares existentes na lista numeros')