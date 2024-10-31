#LOOPS
print('LOOPS\n')

#For - itera sobre uma sequência (como uma lista, uma tupla ou string) ou qualquer objeto iterável
print('For - itera sobre uma sequência (como uma lista, uma tupla ou string) ou qualquer objeto iterável')
print('Exemplo:')
frutas = ["maçã", "banana", "laranja"]
print('frutas = ["maçã", "banana", "laranja"]')
print('for fruta in frutas:\n    print(fruta)')
print('Saída:')
for fruta in frutas:
    print(fruta)
print('\n')

#While
print('While - é utilizado para repetir um bloco de código enquanto uma condição for verdadeira')
print('Exemplo:')
contador = 0
print('contador =', contador)
print('while contador < 5:\n    print(contador)\n    contador += 1')
print('Saída:')
while contador < 5:
    print(contador+1)
    contador += 1
print('\n')

#Controle de Loops
print('Controle de Loops\n')

#Break
print('Break - é utilizado para sair prematuramente de um loop, independentemente da condição.')
print('Exemplo:')
contador = 0
print('contador =', contador)
print('while True:\n    print(contador+1)\n    contador += 1\n\n    if contador == 5:\n        break')
print('Saída:')
while True:
    print(contador+1)
    contador += 1

    if contador == 5:
        break
print('\n')

#Continue
print('Continue - é utilizado para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração')
print('Exemplo:')
print('for i in range(10):\n    if i % 2 == 0:\n        continue\n\n    print(i)')
print('Saída:')
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
print('\n')

#Pass
print('Pass - é uma operação nula que não faz nada. normalmente utilizada ')
print('Exemplo:')
print('for i in range(5):\n    pass')
print('Saída')
for i in range(5):
    pass
print('Neste exemplo, não são geradas saídas, apesar de iterar entre os números 0 à 4')