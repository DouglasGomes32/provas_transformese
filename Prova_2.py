import random

def escolher_palavra():
    palavras = ["python", "serasa", "transformese", "java", "backend"]
    palavra = random.choice(palavras)
    return palavra

def exibir_palavras(palavra, letra_correta):
    exibicao = ''
    for letra in palavra:
        if letra in letra_correta:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def jogar_forca():
    palavra = escolher_palavra()
    letra_correta = []
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print(exibir_palavras(palavra, letra_correta))

    while True:
        letra = input("Digite uma letra: ")

        if letra in letra_correta:
            print("Voce ja digitou essa letra")
            continue

        if letra in palavra:
            letra_correta.append(letra)
            print(exibir_palavras(palavra, letra_correta))
        else:
            tentativas -= 1
            print("Voce errou! agora voce tem", tentativas, "tentativas")
            print(exibir_palavras(palavra, letra_correta))

        if "_" not in exibir_palavras(palavra, letra_correta):
            print("Parabens! voce ganhou")
            break

        if tentativas == 0:
            print("Infelizmente voce perdeu, a palavra correta era:", palavra)
            break

jogar_forca()