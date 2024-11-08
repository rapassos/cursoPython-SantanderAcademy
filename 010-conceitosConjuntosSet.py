#ESTRUTURA DE DADOS - CONJUNTOS(SET)
print('ESTRUTURA DE DADOS - CONJUNTOS(SET)\n')

#Conjuntos(set) - Estrutura de dados mutável, não ordenada que permite armazenar uma coleção de de elementos únicos.
print('Conjuntos(set) - Estrutura de dados mutável, não ordenada que permite armazenar uma coleção de de elementos únicos.\n')

#Criação e operação básica
print('Criação e operação básica')

frutas = {"maçã", "banana", "laranja"}
print('frutas = {"maçã", "banana", "laranja"}')
numeros = set([1, 2, 3, 4, 5])
print('numeros = set([1, 2, 3, 4, 5])')

#Conjuntos suportam operações matemáticas de conjuntos
print('Conjuntos suportam operações matemáticas de conjuntos:\n')

conjunto1 = {1,2,3}
print('conjunto1 = {1,2,3}')
conjunto2 = {3,4,5}
print('conjunto2 = {3,4,5}\n')

uniao = conjunto1|conjunto2
print('uniao = conjunto1|conjunto2 resulta em uniao =',uniao,'\n')

intersecao = conjunto1&conjunto2
print('intersecao = conjunto1&conjunto2 resulta em intersecao =',intersecao,'\n')

diferenca = conjunto1-conjunto2
print('diferenca = conjunto1-conjunto2 resulta em diferenca =',diferenca,'\n')

diferenca_simetrica = conjunto1^conjunto2
print('diferenca_simetrica = conjunto1^conjunto2 resulta em diferenca_simetrica =',diferenca_simetrica,'\n')

#Métodos de conjuntos
print('Métodos de conjuntos')
print('A linguagem python tem métodos incorporados aos conjuntos, seguem alguns exemplos\n')

frutas = {"maçã","banana","laranja"}
print('frutas = {"maçã","banana","laranja"}\n')

print('.add(<<elemento>>) - adiciona um elemento ao conjunto')
frutas.add("pera")
print('frutas.add("pera") resulta em frutas =',frutas,'\n')

print('.remove(<<elemento>>) - remove um elemento do conjunto, caso não exista gera um erro')
frutas.remove("banana")
print('frutas.remove("banana") resulta em frutas =',frutas,'\n')

print('.discard(<<elemento>>) - remove um elemento do conjunto, caso não exista segue a execução')
frutas.discard("uva")
print('frutas.discard("uva") resulta em frutas =',frutas,'\n')

print('.clear() - remove todos os elementos do conjunto')
frutas.clear()
print('frutas.clear() resulta em frutas =',frutas,'\n')