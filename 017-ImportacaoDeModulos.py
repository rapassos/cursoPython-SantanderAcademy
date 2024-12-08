#IMPORTAÇÃO E CRIAÇÃO DE MÓDULOS
print('IMPORTAÇÃO E CRIAÇÃO DE MÓDULOS')

print('Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas. A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente. Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.\n')

print('==============================')
print('Tenha em mente')
print('Python vem com uma ampla biblioteca padrão de módulos que fornecem funcionalidades adicionais. Esses módulos estão disponíveis sem a necessidade de instalá-los separadamente.')
print('==============================')

print('Importar módulos')
print('Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. Podemos importar um módulo completo ou funções específicas de um módulo.')
print('import math\n\nresultado = math.sqrt(25)\nprint(resultado)  # Imprime 5.0')
print('Este exemplo importa o módulo math, que contem recursos voltados para operações matemáticas e utilizamos a função sqrt() que calcula a raiz quadrada. O código acima resulta em:')
import math
resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0
print('\nTambém é possível importar funções específicas de um módulo, utilizando a sintax "from <módulo> import <função>".')
print('from math import sqrt\n\nresultado = sqrt(25)\nprint(resultado)  # Imprime 5.0')
print('Neste exemplo, foi importada apenas a função sqrt() do módulo math, podendo ser utilizada a seguir sem a necessidade de referenciar o módulo durante, porém com a mesma funcionalidade, o codigo acima resulta em:')
from math import sqrt
resultado = sqrt(25)
print(resultado)  # Imprime 5.0

print('\nFunções e classes de módulos padrão')
print('A biblioteca padrão de Python oferece uma ampla gama de módulos com funções e classes úteis. Seguem alguns exemplos comuns:')
print('\nMath:\n\t- sqrt() -> raiz quadrada\n\t- sin() -> seno\n\t- cos() -> cosseno, etc.')
print('\nRandom:\n\t- ramdom() -> número aleatório 0 ou 1\n\t- randint() -> número inteiro aleatório em um intervalo,etc.')
print('\nDatetime:\n\t- datetime.now() -> data e hora atual\n\t- datetime.date() -> data\n\t- datetime.time() -> hora, etc.')
print('Exemplos:')
print('import random\nimport datetime\n\nnumero_aleatorio = random.randint(1, 10)\nprint(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10\n\ndata_atual = datetime.datetime.now()\nprint(data_atual)  # Imprime a data e hora atual\nEste código resulta em:')
import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10

data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual

print('\nEstes são apenas alguns exemplos dos muitos módulos disponíveis em python. Consulte a docuentação oficial do Python, para mais informações sobre outros módulos e funções disponíveis')
