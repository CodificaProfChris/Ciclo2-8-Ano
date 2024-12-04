from random import randint

def desenhar():
    print("  o")
    print("/ | \\")
    print(" /\\")
    print("Você perdeu!")


listaFrutas = ["abacate", "banana", "cereja", "bergamota", "pitaya", "amora", "kiwi"]
listaUsuario = []

print("⧜𝗠𝗲𝗻𝘂⧜")
print("1. Jøgar cøm p✩lavras pr𝑒-d𝑒f𝑖nidas.\n2. Jøgar cøm p𝓁avras c⧫stømizadas.")
opcao = int(input("Cøløque su𝒶 e𝓈colℎ𝒶:"))

if opcao == 1:
    palavraSecreta = listaFrutas[randint(0,len(listaFrutas)-1)]
    pass
if opcao == 2:
    registrarPalavras = 1
    while registrarPalavras == 1:
            palavra = input("D𝒾g𝒾𝓉𝑒 u𝓂𝒶 p𝒶l𝒶𝓋𝓇𝒶:")
            listaUsuario.append(palavra)
            registrarPalavras = int(input("D𝑒s𝑒j𝒶 r𝑒gistr𝒶r m𝒶is?\n1. Sim!\nNão"))
    palavraSecreta = listaUsuario[randint(0,len(listaUsuario)-1)]
    print("R𝑒g𝑖str𝑜 d𝑒 palav𝓇as f𝒾n𝒶l𝒾zad𝒐!")
            
dificuldade = int(input("E𝓈colh𝒶 u𝓂𝒶 d𝒾ficuldade::\n1. Fácil\n2. Médio\n3. Difícil\n4. Impossível"))
if dificuldade == 1:
    vidas = 10
if dificuldade == 2:
    vidas = 5
if dificuldade == 3:
    vidas = 3
if dificuldade == 4:
    vidas = 1
    
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
        print("A palavra não contem essa letra.")
        vidas = vidas -1
    if " _ " not in listaExibicao:
        print(listaExibicao)
        print("Você ganhou essa partida! Parabéns.")
        print("Pontos: ", vidas * 10)
        break
    
if vidas == 0:
    desenhar()
    #print("Você perdeu!")
    
