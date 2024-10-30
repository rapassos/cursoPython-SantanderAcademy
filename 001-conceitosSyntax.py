#Em python a indentação do código (inclusão de espaços ou tabulações no inicio da linha), delimitam
#blocos de código

#Para testar cada bloco de execução, remova o caractere '#' no inicio da linha que deseja testar,
#mantendo a outra com o caractere "#"

#x = True #Executar o bloco verdadeiro
x = False #Executar o bloco Falso

if x:
    #Bloco indentado executado se x verdadeiro
    print('x = Verdadeiro!')
else:
    #Bloco indentado executado se x falso
    print('x = Falso!')


#A linguagem python diferencia caracteres maiúsculos de minúsculos, conforme o exemplo abaixo, a 
#variável 'X' é diferente da variável 'x' utilizada acima

X = not(x) #A função not(x) inverte o valor atribuído a variável 'x' e atribui o na variável 'X'

if X:
    #Bloco indentado executado se X verdadeiro
    print('X = Verdadeiro!')
else:
    #Bloco indentado executado se X falso
    print('X = Falso!')

#A linguagem python permite o aninhamento de instruções em linha única, porém somente é necessário
#neste caso

print('\nAqui ');print('está ');print('um exemplo ');print('de comandos ');print('aninhados em uma linha \n\n')

if (True):
    print('Aqui ')
    print('está ')
    print('um exemplo ')
    print('de comandos ')
    print('aninhados em um bloco indentado')

#A linguagem python utiliza '()' parenteses para a priorização de expressões matemáticas, definir e
#chamar funções para execução, como a função not() utilizada anteriormente
a = 2
b = 7
c = 5

print('\nConsiderando:\na = ',a,'\nb = ',b,'\nc = ',c)
resultado = (a + b) * c
print('O resultado de (a + b) * c é: ',resultado)
