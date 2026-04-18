# exemplo 

from random import*
num = randint(0,1000)
i = 0 
controle = 0

while controle == 0:
    i =i+1
    x = int(input("Digite um numero inteiro:"))
    if num == x:
        print("Parabens, voce acertou em %d tentativas 😁" %i)
        controle = 1
    elif num > x:
        print("O numero pensado é maior!")
    else:
        print("O numero pensado é menor!")