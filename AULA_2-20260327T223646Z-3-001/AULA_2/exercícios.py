#1 - desenvolva um programa  em python que solicite  os valores dos lados de um retangulo e calcule e mostre seu perimetro  e sua area 

lado_1 = int(input("Digite um lado da medida do Retangulo:"))
lado_2 = int(input("Digite um lado da medida do Retangulo:"))

perimetro = (lado_1*2) +(lado_2*2)
area = lado_1*lado_2

print("----------------------RESULTADO---------------------")
print("O Perimetro é:", perimetro)
print("A Area é:", area)

#2 - escreva um programa em python que solicite ao usuario o salario atual e mostre o salario acrescido de 5% de comissao
print("------------------SALARIO+COMISSAO-------------------")
salario = float(input("Digite o seu salario:"))
acrescimo = salario * 0.05
salario_acrescimo = salario+acrescimo

print(f"seu salario com acrescimo de 5% de comissão é: {salario_acrescimo}")


#3 - escreva um programa  que peca ao usuario a distancia entre duas cidades e o tempo de viagem. o programa devera calcular e exibir  a velocidade 
# media de um carro que vai de uma cidade para outra utilize  a formula          vm =  distancia  / tempo

print("-----------------------VELOCIDADE MEDIA------------------")
distancia = int(input("Digite uma distancia de duas cidades em km:"))
tempo = int(input("digite o tempo de viagem dessas duas cidades em minutos:"))
tempo_hr = tempo/60
velo_media = distancia/tempo_hr

print(f"A velocidade media é: {velo_media} km")

# 4 -😊 escreva um program em python que calcule as duas raizes de uma equacao de 2 grau ax+bx+c, conhecendo os valores dos coeficientes da mesma (a,b,c). Suponha que as raizessão reais. lembre-se que para calcular as duas raizes:

import math
a = int(input("digite o valor de A:"))
b = int(input("digite o valor de B:"))
c = int(input("digite o valor de C:"))

quadrado = b**b
delta = quadrado-4*a*c
raiz_delta = math.sqrt(delta)

x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print(f'''-----------RESULTADO------------
    quadrado{quadrado}  
    delta{delta}
    raiz de delta{raiz_delta}
    x1 {x1}
    x2 {x2}''')


#5  - escreva um programa em python que leia a cotação do dolar (taxa de conversão), leia um valor em dolares e converta e mostre o valor equivalente em reais:
print(-----------------TAXA DE COVERSÃO------------------)
valor =float(input("Digite o valor que deseja converter em real:"))
real = valor * 5.33
print(f"o valor em real é: {real} ")


# 6- Escreva um programa em Python que leia um valor representando o gasto realizado por um cliente do restaurante ComaBem e visualize o valor total a ser pago, considerando
# os 10% do garçom.

print("==============  RESTAURANTE COMABEM  ================")
valor = float(input("digite o quanto foi gasto:  "))
acrecimo =  valor * 0.10
total = valor+acrecimo

print(f" o total gasto foi {valor} mais com a taxa do garçom o total e : {total}")

# 7- Escreva um programa em Python que obtenha uma temperatura em graus Celsius, calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin. Utilize as
# fórmulas abaixo:

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Temperatura em Fahrenheit: {fahrenheit}")
print(f"Temperatura em Kelvin: {kelvin}")
