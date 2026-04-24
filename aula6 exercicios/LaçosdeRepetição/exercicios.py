# 4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são positivos e quantos são negativos. Determine, também, qual é o menor desses valores. Utilize o comando de repetição que desejar.
positivos = 0
negativos = 0
menor = None

while True:
    valor = float(input("Digite um valor (ou 0 para parar): "))
    
    if valor == 0:
        break
    
    if valor > 0:
        positivos += 1
    else:
        negativos += 1
    
    if menor is None or valor < menor:
        menor = valor

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Menor valor:", menor)


#  5- Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a altura de cada pessoa, calcule e mostre a altura média das mulheres e dos homens separadamente. Utilize o comando de repetição que desejar

soma_h = soma_m = 0
cont_h = cont_m = 0

while True:
    sexo = input("Sexo (M/F ou S para sair): ").upper()
    
    if sexo == "S":
        break
    
    altura = float(input("Altura: "))
    
    if sexo == "M":
        soma_h += altura
        cont_h += 1
    elif sexo == "F":
        soma_m += altura
        cont_m += 1

if cont_h > 0:
    print("Média homens:", soma_h / cont_h)
if cont_m > 0:
    print("Média mulheres:", soma_m / cont_m)

# 6 - Ler uma quantidade indeterminada de alunos com as seguintes informações RGM, NOME, Sexo e Media.
# Calcular a media da sala, exibir a media da sala, maior nota, menor nota e a media por sexo.

total = 0
soma = 0
maior = -999
menor = 999

soma_m = soma_f = 0
cont_m = cont_f = 0

while True:
    rgm = input("RGM (ou 'fim' para sair): ")
    if rgm == "fim":
        break
    
    nome = input("Nome: ")
    sexo = input("Sexo (M/F): ").upper()
    media = float(input("Média: "))
    
    soma += media
    total += 1
    
    if media > maior:
        maior = media
    if media < menor:
        menor = media
    
    if sexo == "M":
        soma_m += media
        cont_m += 1
    else:
        soma_f += media
        cont_f += 1

print("Média da sala:", soma / total)
print("Maior nota:", maior)
print("Menor nota:", menor)

if cont_m > 0:
    print("Média homens:", soma_m / cont_m)
if cont_f > 0:
    print("Média mulheres:", soma_f / cont_f)


# 7 - Ler vários produtos (código, descrição, quantidade e valor) para uma venda, exibir a lista de produtos e o total da venda.

total_venda = 0
produtos = []

while True:
    codigo = input("Código (ou 'fim' para sair): ")
    if codigo == "fim":
        break
    
    descricao = input("Descrição: ")
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor unitário: "))
    
    total = quantidade * valor
    total_venda += total
    
    produtos.append((codigo, descricao, quantidade, valor, total))

print("\nLista de produtos:")
for p in produtos:
    print(f"Código: {p[0]}, Desc: {p[1]}, Qtd: {p[2]}, Valor: {p[3]}, Total: {p[4]}")

print("Total da venda:", total_venda)