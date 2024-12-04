#EXCEÇÕES PERSONALIZADAS
print('EXCEÇÕES PERSONALIZADAS\n')

print('Além das exceções disponibilizadas pelo Python, você pode criar suas próprias exceções para controlar situações específicas do seu programa.\n')

print('Para criar uma exceção personalizada, é necessário criar uma classe herdada da classe base Exception ou de uma de suas subclasses, exemplo:')
print('def funcao():\n\t# Código que pode gerar uma exceção personalizada\n\tif condicao:\n\t\traise Exception("Descrição do erro")\ntry:\n\tfuncao()\nexcept Exception as e:\n\tprint(f"Erro: {str(e)}")\n')
print('No exemplo, foi difinida a função funcao(), que dentro dela verifica se a "condicao" é verdadeira e gera uma exceção através da declaração raise. Em vez de criar uma classe personalizada, foi utilizada diretamente a classe base Exception para gerar a exceção.\n')
print('*************************')
print('Depois, utiliza-se um bloco try-except para capturar e lidar com a exceção. A variável e é utilizada para acessar a descrição do erro fornecida ao gerar a exceção.')
print('O tratamento de erros e exceções é uma parte fundamental da programação em Python. Permite lidar com situações inesperadas de maneira controlada e evitar que seu programa trave ou pare abruptamente.')
print('Quando ocorre um erro no seu código, o Python gera uma exceção. Ao utilizar blocos try-except, você pode capturar e lidar com essas exceções de maneira adequada. Pode especificar diferentes blocos except para lidar com diferentes tipos de exceções e realizar ações específicas em cada caso.')
print('*************************\n')
print('Além disso, o bloco finally permite executar código de limpeza ou liberação de recursos, independentemente de ter ocorrido uma exceção ou não. Isso é útil para garantir que certas ações sejam sempre realizadas, como fechar arquivos ou conexões de banco de dados.\n')
print('!!!!!!!!!!!!!!!!!!!!!!!!!')
print('Considere os possíveis erros que podem ocorrer no seu código e utilize o tratamento de exceções adequado para lidar com eles de maneira apropriada. Isso tornará seus programas mais robustos e confiáveis.')
print('!!!!!!!!!!!!!!!!!!!!!!!!!')