from random import randint

listaFrutas = ["cajá manga","abacate","morango","pera","maçã","banana","pitaya","graviola","kiwi","umbu","caju","cajá","manga","mamão","cupuaçu","amora","acerola","framboesa","mirtilo","melancia","melão","jaca","jabuticaba","maracujá","laranja","mexerica","tangerina","atemoia","cereja","limão","uva","pitanga","açaí","cabeludinha","carambola","abacaxi","pêssego","ameixa","lichia","romã","caqui","goiaba","guaraná"]
listaUsuario = []
print("===MENU===")
print("1. Jogar com palavras pré-definidas\n2. Adicionar palavras e jogar")
opcao = int(input("Digite sua opção: "))
if opcao == 1:
    palavraSecreta = listaFrutas[randint(0,len(listaFrutas)-1)]
    pass
   
elif opcao == 2:
     registrarPalavras = 1
     while registrarPalavras == 1:  
       palavra = input("Digite a sua palavra: ")
       istaUsuario.append(palavra)
       registrarPalavras = int(input("Deseja registrar mais? \n1. sim \n2. não"))
       palavraSecreta = listaUsuario[randint(0,len(listaUsuario)-1)]
print("Registro de palavras finalizado!")

dificuldade = int(imput("1.Fácil\n2.Médio\n3.Difícil\nDigite sua dificuldade:"))

if dificuldade == 1:
    vidas = 10
elif dificuldade == 2:
    vidas = 5
elif dificuldade == 3:
    vidas = 3

listaExibicao = []
for i in palavraSecreta:
    listaExibicao.append(" _ ")
while vidas > 0
   print(listaExibicao)
   chute = ("Digite uma letra: ")
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

