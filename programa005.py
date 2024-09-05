
try:
    #pedir ao utilizador para inserir o primeiro número e gravar na variavel    
    primeiro_numero = float(input("Digite o primeiro número : "))
    #pedir ao utilizador para inserir o segundo número e gravar na variavel
    segundo_numero = float(input("Digite o segundo número: "))
except:
    print('Deve inserir um numero inteiro')
    exit()

#somar os dois numeros
soma = primeiro_numero + segundo_numero
#imprimir a soma dos dois numeros
print("Resultado: ",soma)












