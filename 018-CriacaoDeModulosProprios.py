#CRIAÇÃO DE MÓDULOS PRÓPRIOS
print('CRIAÇÃO DE MÓDULOS PRÓPRIOS\n')
print('Além de utilizar os módulos padrão do Python, também podemos criar nossos próprios módulos para organizar e reutilizar nosso código.\n')

print('Criar e utilizar módulos personalizados\n')
print('Para criar um módulo personalizado, simplesmente criamos um novo arquivo Python com o nome desejado e definimos as funções, classes e variáveis que queremos incluir no módulo. Por exemplo, criamos um arquivo (no mesmo diretório onde estamos executando Python) chamado meu_modulo.py com o seguinte conteúdo:')
print('#meu_modulo.py\ndef saudar(nome):\n\tprint(f"Olá, {nome}!")\n\ndef calcular_soma(a, b):\n\treturn a + b\n')
print('Depois podemos importar e utilizar as funções definidas, como no exemplo abaixo:\n')
print('import meu_modulo\n\nmeu_modulo.saudar("João")  # Imprime "Olá, João!"\nresultado = meu_modulo.calcular_soma(5, 3)\nprint(resultado)  # Imprime 8\n')
print('Neste exemplo, importa-se o módulo meu_modulo e utilizam-se as funções saudar() e calcular_soma() definidas nele. O código acima resulta em:')
import meu_modulo
meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # Imprime 8

print('\nOrganização do código em módulos')
print('À medida que nossos programas crescem em tamanho e complexidade, é uma boa prática organizar nosso código em módulos separados segundo sua funcionalidade. Isso nos permite manter um código mais legível, agrupado em módulos e fácil de manter.\nPor exemplo, podemos ter um módulo operacoes.py que contenha funções relacionadas com operações matemáticas, e outro módulo utilidades.py que contenha funções de uso geral.')
print('# operacoes.py\ndef somar(a, b):\n\treturn a + b\n\ndef subtrair(a, b):\n\treturn a - b\n\n# utilidades.py\ndef imprimir_mensagem(mensagem):\n\tprint(mensagem)\n\ndef obter_nome_usuario():\n\treturn input("Digite seu nome: ")')
print('Depois, podemos importar e utilizar essas funções em nosso programa principal. Como no exemplo abaixo:')
print('import operacoes\nimport utilidades\n\nresultado = operacoes.somar(5, 3)\nutilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")\n\nnome = utilidades.obter_nome_usuario()\nutilidades.imprimir_mensagem(f"Olá, {nome}!")\n')
print('Ao organizar nosso código em módulos, podemos reutilizar funções e manter um código mais estruturado e agrupado em módulos. O código acima resulta em:')
import operacoes
import utilidades
resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")
nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")
