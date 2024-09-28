# Manipulação de strings
    # O Python permite formar strings com um par de aspas simples ou duplas.

# Índice
    # As strings são sequências de caracteres, de forma que podemos acessar um caractere em uma dada posição utilizando um índice. No exemplo a seguir, caso se queira obter o caractere na primeira posição da string nome, basta acessar o índice 0 da variável.

    # nome = 'Daniel'
    # print(nome[0])

    # Caso tente acessar um índice inexistente, o seguinte erro será exibido: IndexError: string index out of range. Isso acontece porque o índice que se tentou acessar está fora do range da cadeia de caracteres da variável. No exemplo dado, a string "Daniel" só nos permitiria acessar até o índice 5. Se tentarmos acessar nome[6], esse erro seria gerado.

    # Há também a possibilidade de "fatiar" uma variável do tipo String, retornando um "pedaço" dela. No Código 3 podemos ver essa característica na manipulação de Strings.

    # nome = "Daniel"
    # print(nome[0:3]) # Dan

    # Também podemos usar índices negativos para as posições dos caracteres nas strings. Nesse caso, a ordem será inversa, começando do último até o primeiro:

    # nome = "Daniel"
    # print(nome[-2]) # e

    # Uma string no Python é uma sequência de caracteres imutável.

# Concatenação de Strings
    # nome = 'Daniel'
    # sobrenome = 'Silva'

    # nome_completo = nome + ' ' + sobrenome

    # print(nome_completo) # Daniel Silva

# Comparação de Strings
    # No Python podemos comparar strings de duas formas distintas: com o operador == ou is.
    # Com o operador == verificamos se o conteúdo de duas strings é igual.
    # Já com o operador is, o que será comparado é a referência do endereço na memória.

# Principais métodos de Strings
    # No Python existem métodos que podem ser usados para fazer operações com strings.
    # Os métodos de string retornam novos valores, mas não alteram a string original.

# Método find()
    # Com o método find() podemos procurar uma substring dentro de uma string e retornar a posição onde ela foi encontrada:

    # mensagem = 'string no Python'
    # print(mensagem.find('Python')) # 10

    # No caso de a ocorrência não ser encontrada, o resultado será -1

# Método replace()
    # O método replace() é utilizado para substituir ocorrências de substrings dentro de uma string.

    # mensagem = 'Quero aprender Java! Na DevMedia tem salas de Java para aprender essa linguagem'
    # nova_mensagem = mensagem.replace('Java', 'Python')
    # print(nova_mensagem) # Quero aprender Python! Na DevMedia tem salas de Python para aprender essa linguagem

# Método split()
    # Com o método split() desmembramos uma string em múltiplas strings através de um separador passado no parâmetro:

    # ensagem = 'Estou aprendendo Python na DevMedia'
    # nova_mensagem = mensagem.split(' ')
    # print(type(nova_mensagem)) # type 'list'
    # print(nova_mensagem) # ['Estou', 'aprendendo', 'Python', 'na', 'DevMedia']

    # É obrigatório o uso de um separador na função split() quando usada com aspas, pois caso contrário, um erro será gerado com a mensagem ValueError: empty separator. Se as aspas não forem usadas com split(), a função considerará o espaço em branco como separador.

# Método upper()
    # Com o método upper() retornamos uma cópia da string com todas as letras minúsculas convertidas em maiúsculas.

    # mensagem = 'eu gosto de Python'
    # nova_mensagem = mensagem.upper()

    # print(nova_mensagem) # EU GOSTO DE PYTHON

# Método lower()
    # om o método lower(), retornamos uma cópia da string com todas as letras maiúsculas convertidas em minúsculas.

    # mensagem = 'eu gosto de Python'
    # nova_mensagem = mensagem.lower()

    # print(nova_mensagem) # eu gosto de python

# Acentuação no Python

    # Para podermos usar acentuação no Python, devemos definir a codificação utf-8

    # nome = 'João da Silva'
    # print(nome)

    # O código acima irá gerar o seguinte erro: SyntaxError: Non-ASCII character '\xc3' que é gerado devido ao caractere acentuado que usamos na variável nome.

    # Para resolver esse problema, podemos usar #coding: utf-8 no início do código, de acordo com que é instruído na documentação.

    # # coding: utf-8
    # nome = 'João da Silva'
    # print(nome)

    # Na versão 3 do Python, isso não é necessário.