# Exemplos de declaração de diferentes tipos de dados em Python

# Inteiros
idade = 30
print("Idade:", idade)

# Ponto flutuante
altura = 1.75
print("Altura:", altura)

# Caracteres (String)
nome = 'Alice'
print("Nome:", nome)

# Booleanos
esta_chovendo = True
print("Está chovendo:", esta_chovendo)

# Dados compostos: Lista
numeros = [1, 2, 3, 4]
print("Números:", numeros)

# Conversão de tipos
numero_str = str(10)  # Convertendo de inteiro para string
print("Número (string):", numero_str)

# Operações simples com variáveis
soma_idade = idade + 5
print("Idade em cinco anos:", soma_idade)

multiplicacao = numeros[2] * 10
print("Terceiro número multiplicado por 10:", multiplicacao)

# Convertendo float para int e vice-versa
altura_int = int(altura)
print("Altura convertida para inteiro:", altura_int)

idade_float = float(idade)
print("Idade convertida para float:", idade_float)

# Acessando elementos em uma string
primeira_letra = nome[0]
print("Primeira letra do nome:", primeira_letra)

# Atividades práticas propostas
# Peça ao usuário para entrar com um tipo de dado e realize uma operação
entrada_usuario = input("Digite um número inteiro: ")
numero_usuario = int(entrada_usuario)  # Conversão para int
dobro_numero = numero_usuario * 2
print("O dobro do número digitado é:", dobro_numero)
