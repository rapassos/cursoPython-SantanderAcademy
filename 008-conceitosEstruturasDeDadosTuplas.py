#ESTRUTURA DE DADOS - TUPLAS
print('ESTRUTURA DE DADOS - TUPLAS\n')

#Tuplas - são estruturas de dados imutáveis e que permitem armazenar uma coleção de elementos
print('Tuplas - são estruturas de dados imutáveis e que permitem armazenar uma coleção de elementos\n')

#Criação e acesso
print('Criação e acesso')

ponto = (3, 4)
print('ponto = (3, 4)')

print('Permite acessar utilizando o indice do elemento entre [], como feito nas listas')
print('ponto[0] =',ponto[0])
print('ponto[-1] =',ponto[-1],'\n')

#Métodos de tuplas
print('Métodos de tuplas')
print('A linguagem python tem métodos incorporados as tuplas')

minha_tupla = (1,2,3,2,4,2)
print('minha_tupla = (1,2,3,2,4,2)')

print('- .index(elemento[,start_index, end_index]) - devolve o indice da primeira aparição de um elemento na tupla, podendo, opicionalmente, indicar o início e fim da busca')
print('\tminha_tupla.index(2) retorna =',minha_tupla.index(2))
print('\tminha_tupla.index(2,2) retorna =',minha_tupla.index(2,2))
print('\tminha_tupla.index(2,2,5) retorna =',minha_tupla.index(2,2,5))

print('- .count(elemento) - devolve o número de vezes que o elemento aparece na tupla')
print('\tminha_tupla.count(2) retorna =',minha_tupla.count(2))

print('- len(tupla) - devolve o número de elementos da tupla')
print('\tlen(minha_tupla) retorna =',len(minha_tupla))
