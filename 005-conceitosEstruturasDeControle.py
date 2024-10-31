#ESTRUTURAS DE CONTROLE
print('ESTRUTURAS DE CONTROLE\n')

#Estruturas condicionais
print('Estruturas condicionais\n')

#IF
print('IF - Condicional SE, executa um bloco de código se a condição for verdadeira')
print('Exemplo:')
idade = 18
print('idade = ',idade)
print('if idade >= 18:\n    #Bloco de código a ser executado caso a condição seja verdadeira\n    print("Você é maior de idade.")')
print('Saída:')
if idade >= 18:
    #Bloco de código a ser executado caso a condição seja verdadeira
    print('Você é maior de idade.')
print('\n')

#IF-ELSE
print('IF-ELSE - Condicional SE-SENÃO, executa um bloco de código se a condição for verdadeira,\n caso contrário executa um outro bloco de código alternativo')
print('Exemplo:')
idade = 16
print('idade = ',idade)
print("if idade >= 18:\n    #Bloco de código a ser executado caso a condição seja verdadeira\n    print('Você é maior de idade.')")
print("else:\n    #Bloco de código a ser executado caso a condição não seja satisfeita\n    print('Você é menor de idade.')")
print('Saída:')
if idade >= 18:
    #Bloco de código a ser executado caso a condição seja verdadeira
    print('Você é maior de idade.')
else:
    #Bloco de código a ser executado caso a condição não seja satisfeita
    print('Você é menor de idade.')
print('\n')

#IF-ELIF-ELSE
print('IF-ELIF-ELSE - Condicional SE-SENÃOSE-SENÃO, permite especificar múltiplas condições e blocos de códigos alternativos')
print('Exemplo:')
nota = 75
print('nota = ',nota)
print('if nota >= 90:\n   print ("Excelente")\nelif nota >= 80:\n   print ("Muito bom")\nelif nota >= 70:\n   print ("Bom")\nelse:\n   print ("Precisa melhorar")')
print('Saída:')
if nota >= 90:
   print("Excelente")
elif nota >= 80:
   print("Muito bom")
elif nota >= 70:
   print("Bom")
else:
   print("Precisa melhorar")
print('\n')