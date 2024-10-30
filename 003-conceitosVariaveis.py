#VARIÁVEIS

#Variáveis são espaços na memória onde podemos armazenar dados e informações durante o tempo de execução dos nossos programas

#Declaração e atribuição de variáveis
print('Exemplos de declaração de variáveis e atribuição de valores:')
nome = "Juan"
print('nome = "',nome,'"')
idade = 25
print('idade =',idade)
altura = 1.76
print('altura =',idade)
estudante = True
print('estudante =',estudante)

#Podemos copiar o valor de uma variável para outra, exemplo abaixo
print('Copiando valores entre variáveis')
a = b = c = 10
print('a = b = c =',a)
print('a =',a,'\nb =',b,'\nc =',c)

#Regras para nomear variáveis em python
print('\nRegras para nomear variáveis em python:')
print('- Os nomes das variáveis só podem conter letras (a-z, A-Z), números (0-9) e sublinhados (_).\nNão podem começar com um número')
print('- O Python diferencia maiúsculas de minúsculas, então nome e Nome são variáveis diferentes.')
print('- Não se pode usar palavras-chave reservadas do Python como nomes de variáveis\n(por exemplo, if, else, for, while, etc.).')
print('- Recomenda-se usar nomes descritivos para as variáveis, que indiquem claramente seu propósito:\nnome, idade, total_vendas, etc.\n')

print('Exemplos válidos:')
print('idade \nnome_completo \ntotal_vendas \n_contador\n')

print('Exemplos inválidos:')
print('1idade #Inicia com número')
print('nome-completo #Usa hífen em vez de sublinhado')
print('if #Palavra-chave reservada do python')