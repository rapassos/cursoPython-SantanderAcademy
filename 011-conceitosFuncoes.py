#FUNÇÕES
print('FUNÇÕES\n')
print('Funções são blocos de código reutilizáveis que permitem encapsular tarefas e executar quando necessário, melhorando a organização e facilitando a manutenção do código\n')

#Definição e chamada de funções
print('Definição e chamada de funções')

print('Exemplo:')
def saudacao():
    print("Olá mundo")
print('def saudacao():\n\tprint("Olá mundo")\n')

print('Chamada:')
print('saudacao() resulta em:')
saudacao()

def saudacao(nome):
    print(f'Olá, {nome}!')
print('\ndef saudacao(nome):\n\tprint(f"Olá, {nome}!")\n')
print('saudacao("João") resulta em :')
saudacao("João")
print('saudacao("Maria") resulta em :')
saudacao("Maria")

print('\nValores de retorno')
print('A palavra chave return permite retornar valores na chamada da função')

def somar(a,b):
    return a+b
print('def somar(a,b):\n\treturn a+b')
soma = somar(3,7)
print('soma = somar(3,7) resulta em soma =',soma)

print('\nFunções anônimas (lambda)')
print('A palavra chave lambda permite criar funções anônimas, sem nome, definidas em uma linha. Normalmente para funções pequenas e concisas')
quadrado = lambda x: x**2
print('quadrado = lambda x: x**2')
print('quadrado(5) =',quadrado(5))

#Escopo - Variáveis global e local
print('\nEscopo - Variáveis global e local\n')
def funcao1():
    variavel_local = 10
    print(variavel_local)
print('def funcao1():\n\tvariavel_local = 10\n\tprint(variavel_local)\n')

variavel_global = 20
def funcao2():
    print(variavel_global)
print('variavel_global = 20\ndef funcao2():\n\tprint(variavel_global)\n')

print('funcao1() resulta em:')
funcao1()
print('funcao2() resulta em:')
funcao2()
print('print(variavel_global) =',variavel_global)
print('print(variavel_local) gera um erro, pois foi definida no escopo da função1\n')

#Documentando funções (docstrings)
print('Documentando funções (docstrings)\n')

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.

    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.

    Returns:
        float: A área do retângulo.
    """
    return base * altura

print('def area_retangulo(base, altura):\n\t"""\n\tCalcula a área de um retângulo.\n\n\tArgs:\n\t\tbase (float): A base do retângulo.\n\t\taltura (float): A altura do retângulo.\n\n\tReturns:\n\t\tfloat: A área do retângulo.\n\t"""\n\treturn base * altura\n')

print('area_retangulo(17,3) resulta em',area_retangulo(17,3))


#Funções com número variável de argumentos
print('Funções com número variável de argumentos\n')

def somador(*numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma
print('def somador(*numeros):\n\tsoma = 0\n\tfor num in numeros:\n\t\tsoma += num\n\treturn soma')
print('somador(1,2,3) resulta em',somador(1,2,3))
print('somador(4,5,6,7) resulta em',somador(4,5,6,7))

