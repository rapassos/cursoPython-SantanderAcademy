#TRATAMENTO DE ERROS E EXCEÇÕES
print('TRATAMENTO DE ERROS E EXCEÇÕES\n')
print('Ao desenvolver códigos de programação podem ocorrer falhas e erros durante a execução, a linguagem Python permite lidar com estes casos usando o tratamento de exceções, permitindo controlar e definir o que deve ser feito em casos específicos.\n')

#Erros comuns em Python
print('Erros comuns em Python')

print('\nErro de sintaxe (SyntaxError)\n')
print('Ocorre quando as regras de sintax da linguagem não são seguidas, exemplo:')
print('def minha_funcao() # Faltam os dois pontos\n\tprint("Olá")')

print('\nErro de nome (NameError)')
print('Ocorre quando nos referimos à uma função ou variável não definida, exemplo:')
print('print(variavel_nao_definida)')

print('\nErro de tipo (TypeError)')
print('Ocorre quando utilizamos tipos de dados incompatíveis, exemplo:')
print('resultado = 5 + "10"')

print('\nErro de índice (IndexError)')
print('Ocorre quando tentamos acessar um indice fora do intervalo de uma lista ou sequência, exemplo:')
print('lista = [1, 2, 3]\nprint(lista[3])  # O índice 3 está fora do intervalo')

print('\nEstes são alguns exemplos. Quando um erro ocorre, o Python "dispara" uma exceção e exibe uma mensagem de erro com a descrição do problema.\n')