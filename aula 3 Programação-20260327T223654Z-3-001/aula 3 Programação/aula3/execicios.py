# 1- Faça um programa em Python que calcule e mostre o valor do volume do tronco de
# uma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura do
# tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e
# calcular a seguinte expressão:
# volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print("=======================VOLUME DO TRONCO DE PIRAMIDE=================================")
altura = float(input("Digite a altura do tronco da pirâmide:"))
Bmenor = float(input("Digite a Base menor do triângulo:"))
Bmaior = float(input("Digite a Base maior do triângulo:"))

volume =altura/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print(f"O volume do tronco da piramide é: {volume:0f}")


# 2- Crie um programa em Python que solicite o valor em horas para o usuário, calcule e
# mostre o valor em minutos, sabendo que 1 hora tem 60 minutos.

print("=======================VALOR EM MINUTOS==========================")
valor = int(input("Digite um valor em horas:"))
min = valor*60

print(f"O valor digitado {valor} tem {min} minutos")


# 3- Crie um programa em Python que solicite ao usuário a sua idade expressa em anos,
# meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas em dias.
# Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.

print("=======================IDADE============================")
idade = int(input("Digite a sua idade em anos,meses e dias:"))
ano = idade*365
mes = idade*30

print(f"A idade {idade} expressa em dias {}")




# 4- Escreva um programa em Python para calcular o valor de uma prestação em atraso
# (prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de
# multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o
# valor da prestação atualizado, sabendo que:
# prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)
# 5- Faça uma programa em Python que peça do usuário um valor em graus para um
# ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o seno,
# cosseno e tangente deste ângulo.

