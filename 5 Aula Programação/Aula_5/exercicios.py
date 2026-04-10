# Exercícios
# 1- Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:
# • não-eleitor (abaixo de 16 anos)
# • eleitor obrigatório (entre 18 e 65 anos)
# • eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)
print("------------------CLASSE ELEITORAL----------------------")
idade = int(input("Digite a sua idade:"))
if idade >=16  and idade <18 or idade > 65:
    print("Voto facultativo!")
elif idade >= 18 and idade <= 65:
    print("Voto Obrigatório!")
else:
    print("Não eleitor!")


# 2- Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo
# grau, apresentando: as duas raízes, quando for possível efetuar o cálculo (delta positivo ou
# zero); a mensagem "Não há raízes reais", se não for possível fazer o cálculo (delta
# negativo); e a mensagem "Não é equação do segundo grau", se o valor de a for igual a
# zero.
import math
print("-------------------EQUAÇÃO DE 2* GRAU----------------------")
a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))

delta = b**2 - 4*a*c
if delta > 0:
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)
    print(f''' 
x1 = {x1}
x2 = {x2}
delta = {delta}
raiz de delta = {raiz_delta}''')
    
elif delta == 0:
    print("Não é equação de segundo grau")
else:
    print("Não há raízes reais")

# Exercícios
# 3- Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
# Crie uma programa que permita digitar o nome do produto e valor da compra, e
# imprimindo o nome do produto e o valor da venda.
# Valor de compra Valor de venda
# valor < R$10,00 lucro de 70%
# R$ 10,00 <= valor < R$ 30,00 lucro de 50%
# R$ 30,00 <= valor < R$ 50,00 lucro de 40%
# valor >= R$50,00 lucro de 30%
print("----------------------VENDA-----------------------------")
print('''
lata de refrigerante = R$ 4
biscoito             = R$ 3
chocolate            = R$ 7
yogurte              = R$ 2
salgadinho           = R$ 5
bolo no pote         = R$ 12
''')
produtos = {
    "lata de refrigerante" : 4,
    "biscoito"             : 3,
    "chocolate"            : 7,
    "yogurte"              : 2,
    "salgadinho"           : 5,
    "bolo no pote"         : 12
    
}

produto = input("Digite o nome do produto:")
if produto in produtos:
    valor = produtos[produto]
    print(f"PRODUTO = {produto}, VALOR = {valor}")
else:
    print("Produto invalido!")

#calculo da vends
if valor < 10:
    venda = valor* 1.70
elif valor < 30:
    venda = valor* 1.50
elif valor < 50:
    venda = valor* 1.40
else:
    venda = valor*1.30
    
print(f'''
produto = {produto}
valor = {valor}
venda = {venda}
''')

# Exercícios
# 4- Elabore um programa em Python que implemente uma calculadora com as funções de
# somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois
# valores, e perguntar qual a operação pretendida ('+', '-' , '*' ou '/' ) e a seguir calcular e
# mostrar o resultado.
print("----------------------- CALCULADORA ----------------------")

num1 = float(input("digite o valor 1: "))
num2 = float(input("digite o valor 2 : "))
print("digite a formula que voce deseja calcular(+)(-)(*)(/): ")
formula = input("digite a formula: ")

if formula == '+':
    calculo = num1+num2
elif formula == '-':
    calculo = num1-num2
elif formula == '*':
    calculo = num1*num2
elif formula == '/':
    calculo = num1/num2
else:
    print("erro digite alguma opção")

print(f"o resultado de {num1} {formula} {num2} = {calculo}")


# 5- Ler 4 números inteiros, exibir o maior e o menor deles.
# Exercício 5
nu1 = int(input("Digite o 1° número: "))
nu2 = int(input("Digite o 2° número: "))
nu3 = int(input("Digite o 3° número: "))
nu4 = int(input("Digite o 4° número: "))

maior = nu1
menor = nu1

if nu2 > maior:
    maior = nu2
if nu3 > maior:
    maior = nu3
if nu4 > maior:
    maior = nu4

if nu2 < menor:
    menor = nu2
if nu3 < menor:
    menor = nu3
if nu4 < menor:
    menor = nu4

print(f"Maior: {maior}")
print(f"Menor: {menor}")



# 6 – ler 5 números inteiros e exibir o maior deles
# Exercício 6
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 3° número: "))
n4 = int(input("Digite o 4° número: "))
n5 = int(input("Digite o 5° número: "))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
if n5 > maior:
    maior = n5

print(f"Maior: {maior}")





#exercicio
# 5- ler os valor e dizer qual é o maior 
#n1 = int(input("Digite um número:"))
#n2 = int(input("Digite um número:"))
#n3 = int(input("Digite um número:"))
#n4 = int(input("Digite um número:"))
#n5 = int(input("Digite um número:"))

