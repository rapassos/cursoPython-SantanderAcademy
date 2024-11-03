#ESTRUTURA DE DADOS - DICIONÁRIOS
print('ESTRUTURA DE DADOS - DICIONÁRIOS\n')

#Dicionários - são estruturas de dados mutáveis, não ordenadas que armazenam dados em pares chave-valor
print('Dicionários - são estruturas de dados mutáveis, não ordenadas que armazenam dados em pares chave-valor\n')

#Criação e acesso
print('Criação e acesso')

pessoa = {"nome":"Rafael","idade":42,"cidade":"São Bernardo do Campo"}
print('pessoa = {"nome":"Rafael","idade":42,"cidade":"São Bernardo do Campo"}')

print('pessoa["nome"] =',pessoa["nome"])
print('pessoa["idade"] =',pessoa["idade"])
print('pessoa["cidade"] =',pessoa["cidade"])

print("\nPodemos utilizar o método .get(<<chave>>), que caso a chave não exista, retorna 'None' no lugar do valor")
print('pessoa.get("abc") =',pessoa.get("abc"))
print('pessoa.get("nome") =',pessoa.get("nome"),'\n')

#Métodos de dicionários
print('Métodos de dicionários')
print('A linguagem python tem métodos incorporados aos dicionários, seguem alguns exemplos')

print('.keys() - retorna todas as chaves de um dicionário')
print('pessoa.keys() =',pessoa.keys())

print('.values() - retorna todos os valores de um dicionário')
print('pessoa.values() =',pessoa.values())

print('.items() - retorna todos os pares de chave-valor de um dicionário')
print('pessoa.items() =',pessoa.items())

print('.update() - retorna todos os valores de um dicionário')
pessoa.update({"profissão":"Analista de TI"})
print('pessoa.update({"profissão":"Analista de TI"})',pessoa)
