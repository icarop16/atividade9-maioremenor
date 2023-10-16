#Faça um software que verifique entre 2 numeros qual o maior 
numero = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um número inteiro: "))
if numero > numero2:
    print(f"O número {numero} é maior que {numero}")
elif numero == numero2:
    print (f"O número informado é igual a {numero2}")
else:
    print(f"O número {numero} é menor que {numero2}")