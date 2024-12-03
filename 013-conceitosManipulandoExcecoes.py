#MANEJO DE EXCEÇÕES
print('MANEJO DE EXCEÇÕES\n')

print('O manejo de exceções, permite controlar o comportamento da aplicação em casos de erros especificados, utilizando as declarações "try", "except" e "finally" opcionalmente.\n')

print('Try')
print('O bloco try, compreende o trecho de código que pode gerar a exceção, e em caso de ocorrencia destinará o fluxo para o bloco except, exemplo:')
print('try:\n\t# Código que pode gerar uma exceção\n\tresultado = 10 / 0  # Divisão por zero\n\tprint(resultado)\nexcept ZeroDivisionError:\n\tprint("Erro: Divisão por zero")\n')

print('O resultado do código acima é:')
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")

print('\nExcept')
print('O bloco except, define como será tratada uma exceção, sendo possível definir diversas exceções a serem tratadas, exemplo:')
print('try:\n\t# Código que pode gerar uma exceção\n\tresultado = 10 / 0  # Divisão por zero\n\tprint(resultado)\nexcept ZeroDivisionError:\n\tprint("Erro: Divisão por zero")\nexcept ValueError:\n\tprint("Erro: Valor inválido")\n')
print('O resultado do código acima é:')
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")

print('\nFinally')
print('O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos, exemplo:')
print('try:\n\t# Código que pode gerar uma exceção\n\tarquivo = open("arquivo.txt", "r")\n\t# Realizar operações com o arquivo\nexcept FileNotFoundError:\n\tprint("Erro: Arquivo não encontrado")\nfinally:\n\tarquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção\n')
print('O resultado do código acima é:')
try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    print('')
    #arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção