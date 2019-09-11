#Complete as funcoes a seguir

def soma(a, b):
	#Insira o codigo aqui
    print(num1, "+", num2,"Resultado =", a+b)

def subtrai(a, b):
	#Insira o codigo aqui
    print(num1, "-", num2, "Resultado =", a-b)

def multiplica(a, b):
	#Insira o codigo aqui
    print(num1, "*", num2,"Resultado =", a*b)

def divide(a, b):
	#Insira o codigo aqui
    if (b == 0):
        print("Não se pode dividir por 0")
    else:
        print(num1, "/", num2,"Resultado =", a/b)

#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)


