#OPERADORES
print('OPERADORES\n')

#Aritméticos - operadores matemáticos básicos
print('Aritméticos - operadores matemáticos básicos\n')

print('"+" - Soma')
print('"-" - Subtração')
print('"*" - Multiplicação')
print('"/" - Divisão')
print('"//" - Divisão inteira (parte decimal é truncada/ignorada)')
print('"%" - Módulo ou resto da divisão')
print('"**" - Potênciação\n')

print('Exemplos:')
a = 3
b = 7
print('a =',a)
print('b =',b)

soma = a+b
print('Soma entre',a,' e ',b,'é',soma)
subtracao = a-b
print('Subtração entre',a,' e ',b,'é',subtracao)
multiplicacao = a*b
print('Multiplicação entre',a,' e ',b,'é',multiplicacao)
divisao = a/b
print('Divisão entre',a,' e ',b,'é',divisao)
divInt = a//b
print('Divisão inteira entre',a,' e ',b,'é',divInt)
modulo = a%b
print('Modulo entre',a,' e ',b,'é',modulo)
potencia = a**b
print('Potenciação entre',a,' e ',b,'é',potencia,'\n')

#De comparação - compara valores e retorna True ou False (Verdadeiro ou Falso)
print('De comparação - compara valores e retorna True ou False (Verdadeiro ou Falso)\n')
print('"==" - True para valores iguais')
print('"!=" - True para valores diferentes')
print('">" - True para o primeiro valor maior que o segundo')
print('"<" - True para o segundo valor maior que o primeiro')
print('">=" - True para o primeiro valor maior ou igual ao segundo')
print('"<=" - True para o segundo valor maior ou igual ao primeiro\n')

print('Exemplos:')
x = 2
y = 9
print('x =',x)
print('y =',y)

igual = x==y
print('x == y:',igual)
diferente = x!=y
print('x != y:',diferente)
maior_que = x > y
print('x > y:',maior_que)
menor_que = x < y
print('x < y:',menor_que)
maior_igual = x >= y
print('x >= y:',maior_igual)
menor_igual = x <= y
print('x <= y:',menor_igual,'\n')

#Lógicos - expressões condicionais e avaliar multiplas condições
print('Lógicos - expressões condicionais e avaliar multiplas condições\n')

print ('"and" - retorna True se ambas as condições são verdadeiras')
print ('"or" - retorna True se ao menos uma das condições é verdadeira')
print ('"not" - retorna True para condição falsa e False para condição verdadeira')

print('Exemplos:')
n1 = 7
n2 = 5
print('n1 =',n1)
print('n2 =',n2)

log_and = (n1 > 5) and (n2 < 5)
print('(n1 > 5) and (n2 < 5) =',log_and)
log_or = (n1 > 5) or (n2 < 5)
print('(n1 > 5) or (n2 < 5) =',log_or)
log_not = not((n1 > 5) or (n2 < 5))
print('not((n1 > 5) or (n2 < 5)) =',log_not)