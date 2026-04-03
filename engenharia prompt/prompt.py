# meu codigo para somar os numeros

# a = int(input("digite o primeiro numero:"))
# b = int(input("digite o primeiro numero:"))

# somar = a + b
# print("a soma dos numeros é:", somar)


# codigo com o githubcopilot

# def somar(a, b):
#     return a + b

# exemplo 2 
# for i in range(0,11,2):
#     print(i)
 
# exemplo 3: calcular o fatorial de n
# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)

# Exemplo de uso
# numero = int(input("Digite um número para calcular o fatorial: "))
# print(f"O fatorial de {numero} é: {fatorial(numero)}")

# exemplo de codigo com outra ia
# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fatorial(n - 1)

# n = int(input("Digite um número: "))
# print(fatorial(n))


# exercicio 4 
# faça correção do codigo 
# def media(lista): 
#     return sum(lista) / len(lista) # esqueceu tratar lista vazia


# teste unitario para a funcao media

# def media(numeros):
#     if len(numeros) == 0:
#         raise ValueError("Lista não pode ser vazia")
#     return sum(numeros) / len(numeros)

# import unittest

# class TestMedia(unittest.TestCase):

#     def test_media_normal(self):
#         self.assertEqual(media([2, 4, 6]), 4)

#     def test_media_um_elemento(self):
#         self.assertEqual(media([10]), 10)

#     def test_media_com_negativos(self):
#         self.assertEqual(media([-2, -4, -6]), -4)

#     def test_media_mista(self):
#         self.assertEqual(media([-2, 2]), 0)

#     def test_lista_vazia(self):
#         with self.assertRaises(ValueError):
#             media([])

# if __name__ == "__main__":
#     unittest.main()


# refatorar o codigo

# a = 0
# for i in range(10):
#     a = a+i

# versão refatorada

# crie um programa que onde ele e de uma confeitaria mostrando os seus doces e preços dando sujestoes de sabores ou algo que o usuario goste
# Cardápio da confeitaria
# doces = {
#     "brigadeiro": 5.0,
#     "beijinho": 4.5,
#     "bolo de chocolate": 7.0,
#     "bolo de morango": 7.5,
#     "cupcake de baunilha": 6.0,
#     "torta de limão": 8.0
# }

# def mostrar_cardapio():
#     print("\n🍩 CARDÁPIO DA CONFEITARIA 🍩")
#     for doce, preco in doces.items():
#         print(f"- {doce.title()} : R$ {preco:.2f}")

# def sugerir(gosto):
#     sugestoes = []
    
#     if "chocolate" in gosto:
#         sugestoes.append("brigadeiro")
#         sugestoes.append("bolo de chocolate")
    
#     if "morango" in gosto:
#         sugestoes.append("bolo de morango")
    
#     if "leve" in gosto or "azedo" in gosto:
#         sugestoes.append("torta de limão")
    
#     if "doce" in gosto:
#         sugestoes.append("beijinho")
#         sugestoes.append("cupcake de baunilha")
    
#     return sugestoes

# # Programa principal
# print("Bem-vindo à confeitaria! 🎂")

# mostrar_cardapio()

# gosto = input("\nQue tipo de doce você gosta? (ex: chocolate, morango, doce, leve): ").lower()

# recomendados = sugerir(gosto)

# if recomendados:
#     print("\n✨ Sugestões para você:")
#     for item in recomendados:
#         print(f"- {item.title()} (R$ {doces[item]:.2f})")
# else:
#     print("\nNão encontrei uma sugestão exata, mas veja nosso cardápio!")

# # Escolha do usuário
# escolha = input("\nQual doce você quer comprar? ").lower()

# if escolha in doces:
#     print(f"\n🧾 Você escolheu {escolha.title()} - R$ {doces[escolha]:.2f}")
#     print("Obrigado pela compra! 😄")
# else:
#     print("\n❌ Doce não encontrado no cardápio.")

#exemplo 7 
#crie uma função que recebe uma lista de numeros e retorna os numeros impares:

# numeros  = []
# impar = numeros % 2 != 0

# print(impar)


# def numeros_impares(lista):
#     return [num for num in lista if num % 2 != 0]