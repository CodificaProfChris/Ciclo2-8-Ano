from random import randint 

def desenhar():
    print("  O ")
    print("/ | \\")
    print(" | |")
    print("Você perdeu!")

listaFrutas = ["abacate", "laranja", "banana", "goiaba", "manga", "abacaxi"]
listaUsuario = []

print("=== Menu ===")
print("1. Jogar com palavras pré-definidas\n2. Adicionar palavras e jogar")
opcao = int(input("Digite sua opção: "))


if opcao == 1:
    palavraSecreta = listaFrutas[randint(0,len(listaFrutas)-1)]
    pass
elif opcao == 2:
    registrarPalavras = 1
    while registrarPalavras == 1:
        palavra = input("Digite uma palavra: ")
        listaUsuario.append(palavra)
        registrarPalavras = int(input("Deseja registrar mais? \n1. sim\n2. não"))
    palavraSecreta = listaUsuario[randint(0,len(listaUsuario)-1)]
print("Registro de palavras finalizado!")


dificuldade = int(input("1.Fácil\n2. Média\n3.Difícil\nDigite a dificuldade que deseja jogar: "))
if dificuldade == 1:
    vidas = 10
elif dificuldade == 2:
    vidas = 5
elif dificuldade == 3:
    vidas = 3


listaExibicao = []
for i in palavraSecreta:
    listaExibicao.append(" _ ")

while vidas > 0:
    print(listaExibicao)
    chute = input("Digite uma letra: ")
    if chute in palavraSecreta:
        for letra in range(0,len(palavraSecreta)):
            if palavraSecreta[letra] == chute:
                listaExibicao[letra] = chute
    else:
        print("A palavra não contém esta letra")
        vidas = vidas - 1
        
    if " _ " not in listaExibicao:
        print(listaExibicao)
        print("Você ganhou o jogo, parabéns!")
        print("pontos: ", vidas * 10)
        break

if vidas == 0:
    desenhar()
    #print("Você perdeu!")

