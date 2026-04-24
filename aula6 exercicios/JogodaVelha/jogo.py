tabuleiro = [" " for _ in range(9)]

jogador = "X"

rodadas = 0

ganhou = False



while rodadas < 9 and not ganhou:

    

    print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")

    print("---|---|---")

    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")

    print("---|---|---")

    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\n")

    

    pos = int(input(f"Jogador {jogador}, escolha uma posição (0-8): "))

    

    if tabuleiro[pos] != " ":

        print("Posição ocupada! Tente novamente.")

        continue

    

    tabuleiro[pos] = jogador

    rodadas += 1

    

    if (

        (tabuleiro[0] == tabuleiro[1] == tabuleiro[2] == jogador) or

        (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] == jogador) or

        (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] == jogador) or

        (tabuleiro[0] == tabuleiro[3] == tabuleiro[6] == jogador) or

        (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] == jogador) or

        (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] == jogador) or

        (tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == jogador) or

        (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == jogador)

    ):

        ganhou = True

        print(f"\nJogador {jogador} venceu!")

        break

    

    if jogador == "X":

        jogador = "O"

    else:

        jogador = "X"





print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")

print("---|---|---")

print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")

print("---|---|---")

print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\n")



if not ganhou:

    print("Deu empate!")