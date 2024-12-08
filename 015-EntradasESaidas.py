#ENTRADAS E SAÍDAS
print('ENTRADAS E SAÍDAS\n')

print('Python nos permite manipular arquivos e interagir com o usuário, solicitando informações, exibir resultados na tela ou ler e escrever dados em arquivos externos\n')

print('Entrada de dados')
print('Para obter dados do usuário durante a execução do programa, podemos utilizar a função "input()". Esta função mostra uma mensagem na tela e espera que o usuário insira um valor.')
print('nome = input("Insira seu nome: ")\nidade = input("Insira sua idade: ")\n\nprint("Olá, " + nome + "!")\nprint("Você tem " + idade + " anos.")\neste código resulta em:')

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")
print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.\n")

print('Neste exemplo, são solicitados os nome e a idade do usuário utilizando a fuinção input(). Os valores são armazenados nas variáveis nome e idade, e postariormente impressos na tela utilizando a função print().\n')

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('A função input() sempre retorna uma cadeia de texto. Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, é necessário fazer a conversão explicitamente, utilizando funções como int() para inteiros ou float() para ponto flutuante.')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

print('idade = int(input("Insira sua idade: "))\n\nif idade >= 18:\n\tprint("Você é maior de idade.")\nelse:\n\tprint("Você é menor de idade.")\n Este código resulta em:')

idade = int(input("Insira sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

print('Neste exemplo, é solicitada a idade usuário que é convertida para número inteiro e armazenada na variável idade, e posteriormente verificada se é maior que 18 e exibe na tela a informação se é menor ou maior de idade.\n')

print('Saída de dados')
print('para imprimir informações na tela, usamos a função print(). Essa função recebe um ou mais argumentos e mostra no console. Pode se utilizar a f-string (formatação de cadeias) para inserir variáveis diretamente na cadeia de texto.')
print('nome = "Juan"\nidade = 25\n\nprint(f"Olá, meu nome é {nome} e tenho {idade} anos.")\n Este código resulta em:')
nome = "Juan"
idade = 25
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

print('Neste caso, as variáveis são inseridas dentro da cadeia utilizando chaves {} e a cadeia é precedida pela letra f para indicar que é uma f-string.')
