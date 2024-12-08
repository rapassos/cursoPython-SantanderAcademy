#LEITURA E ESCRITA DE ARQUIVOS
print('LEITURA E ESCRITA DE ARQUIVOS\n')

print('Python permite ler e escrever em arquivos externos, os arquivos podem ser acessados de diferentes formas, seguem alguns exemplos:\n"r" -> Leitura\n"w" -> Escrita\n"a" -> Anexar, para adicionar informações ao final do arquivo\n')

print('Leitura de arquivos')
print('Para ler o conteúdo do arquivo, precisamos abri-lo com a função open(), em modo leitura ("r"). Depois utilizamos os métodos read() ou readlines() para ler o conteúdo do arquivo.')
print('arquivo = open("dados.txt", "r")\nconteudo = arquivo.read()\nprint(conteudo)\narquivo.close().\nEste código resulta em:')
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
print('Neste exemplo, o arquivo "dados.txt" é aberto em modo leitura, e seu conteúdo é armazenado na variável "conteúdo" através do metodo read(). O conteúdo é exivido na tela e fechado pelo método close().\n')

print('Escrita de arquivos')
print('Para abrir o arquivo em modo escrita usamos a função open() com a opção ("w"). Se o arquivo não existir, ele será criado automaticamente. Caso exista, o seu conteúdo será sobrescrito.')
print('arquivo = open("dados.txt", "w")\narquivo.write("Olá, mundo!")\narquivo.close()')
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()
print('Nese exemplo, o arquivo "dados.txt" é aberto em modo de escrita, depois é escrito a string "Olá, mundo!" é escrita no arquivo com o método write(), e finalmente o arquivo é fechado com o método close().\n')

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('É importante fechar sempre os arquivos depois de utilizá-los para liberar os recursos do sistema.')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

print('Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.')
print('with open("dados.txt", "r") as arquivo:\n\tconteudo = arquivo.read()\n\tprint(conteudo)')
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
print('Neste caso, o arquivo é aberto utilizando a declaração with e é fechado automaticamente uma vez que se sai do bloco with, mesmo se ocorrer uma exceção.\n')

print('A entrada e saída de dados em Python nos oferece uma grande flexibilidade para interagir com o usuário e manipular arquivos externos. Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos de texto. Lembre-se sempre de manejar adequadamente a abertura e fechamento de arquivos, e considerar as possíveis exceções que podem ocorrer durante as operações de entrada/saída.')
