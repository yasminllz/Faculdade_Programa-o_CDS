# 1- Escreva um algoritmo que solicite um número ao usuário. Caso seja digitado um valor
# entre 0 e 9, mostre: “valor correto”, caso contrário mostre: “valor incorreto”.
print("=====================EXERCÍCIO 1 ======================")
variavel = int(input("Digite um número:"))

if variavel >=0 and variavel <=9:
    print("Parabens!😊 Valor Correto")
else:
    print("Valor Incorreto!")


# 2- Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de
# horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a
# seguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize um
# caractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário é R$
# 37,50

# print("========================EXERCÍCIO 2 =============================")
# turno = int(input("Digite o seu Turno de Trabalho:"))
# quan_horas = int(input("Digite a sua quantidade de horas trabalhadas:"))
if(turno == "N"):
    valorHora = 45
else:
    valorHora = 37,50


# 3- Faça um programa em Python que obtenha o valor de uma compra, calcular e mostrar
# o valor da compra considerando o desconto, conforme descrito abaixo:
# para compras acima de R$ 200 a loja dá um desconto de 20%
# para as abaixo disso não tem desconto, mostre o valor da compra.

print("=========================EXERCÍCIO 3===============================")
compra = int(input("Digite o valor da sua compra:r$"))
desconto = compra*20/100
if compra>= 200:
    print(f"Parabens você teve obteve um desconto de 20% = {desconto} na sua compra de R${compra} ")
else:
    print(f"O valor da sua compra deu R${compra}")

# 4- Escreva um programa em Python que solicite ao usuário os valores de três contas de
# consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário é
# suficiente para pagar as três contas, caso não seja apresente a mensagem “Salário
# insuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas.
print("========================EXERCICIO 4 =============================")
agua = int(input("Digite o valor da conta de agua:"))
luz = int(input("Digite o valor da conta de agua:"))
internet = int(input("Digite o valor da conta de agua:"))
