from random import randint

def desenhar(vidas):
    if vidas == 0:
        print("  O ")
        print("/ | \\")
        print(" | |")
        print("Você perdeu!")
    elif vidas == 1:
        print("  O ")
        print(" /|\\")
        print("  | ")
    elif vidas == 2:
        print("  O ")
        print(" /| ")
        print("  | ")
    elif vidas == 3:
        print("  O ")
        print("  | ")
        print("  | ")
    elif vidas == 4:
        print("  O ")
    else:
        print("  O ")

def jogar(palavraSecreta, vidas):
    palavraOculta = ['_' for _ in palavraSecreta]
    letrasErradas = []
    
    while vidas > 0 and '_' in palavraOculta:
        print("\nPalavra: " + " ".join(palavraOculta))
        print("Letras erradas: " + ", ".join(letrasErradas))
        print(f"Vidas: {vidas}")
        
        tentativa = input("Digite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        
        if tentativa in palavraSecreta:
            for i in range(len(palavraSecreta)):
                if palavraSecreta[i] == tentativa:
                    palavraOculta[i] = tentativa
            print(f"Boa! A letra '{tentativa}' está na palavra.")
        else:
            if tentativa not in letrasErradas:
                letrasErradas.append(tentativa)
                vidas -= 1
                desenhar(vidas)
                print(f"A letra '{tentativa}' não está na palavra.")
            else:
                print(f"Você já tentou a letra '{tentativa}'.")

    if '_' not in palavraOculta:
        print("\nParabéns! Você adivinhou a palavra:", "".join(palavraOculta))
    else:
        print(f"\nVocê perdeu! A palavra era: {palavraSecreta}")

listaFrutas = ["abacate", "laranja", "banana", "goiaba", "manga", "abacaxi"]
listaUsuario = []

print("=== Menu ===")
print("1. Jogar com palavras pré-definidas\n2. Adicionar palavras e jogar")
opcao = int(input("Digite sua opção: "))

if opcao == 1:
    palavraSecreta = listaFrutas[randint(0, len(listaFrutas)-1)]
elif opcao == 2:
    registrarPalavras = 1
    while registrarPalavras == 1:
        palavra = input("Digite uma palavra: ")
        listaUsuario.append(palavra)
        registrarPalavras = int(input("Deseja registrar mais? \n1. Sim\n2. Não: "))
    palavraSecreta = listaUsuario[randint(0, len(listaUsuario)-1)]

print("Registro de palavras finalizado!")

dificuldade = int(input("1. Fácil\n2. Média\n3. Difícil\nDigite a dificuldade que deseja jogar: "))
if dificuldade == 1:
    vidas = 10
elif dificuldade == 2:
    vidas = 5
elif dificuldade == 3:
    vidas = 3

jogar(palavraSecreta, vidas)
