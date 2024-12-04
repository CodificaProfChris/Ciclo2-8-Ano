from random import randint
def desenhar():
     print("  O  ")
     print("/ | \\")
     print(" | |")
     print("voce perdeu")

listadias = ["segunda","terça","quarta","quinta","sexta","sab","dom"]
listaUsuario = []
print("===menu===")
print("1.jogar com palavras pre definidas\n2. adicionar novas palavras")
opcao = int(input("digite sua opçao: "))
if opcao == 1:
    palavrasecreta = listadias[randint(0,len(listadias)-1)]
    pass
elif opcao == 2:
 registrar_palavras = 1
 while registrar_palavras == 1:
   palavra = input("digite uma palavra: ")
   listaUsuario.append(palavra)
   registrar_palavras=int(input("deseja registar mais?\n1 sim \n2 nao"))
 palavrasecreta = listadias[randint(0,len(listadias)-1)]
print("registro finalizado")
dificuldade = int(input("1.Fácil \n 2. Média \n 3.Difícil \n Digite a dificuldade que deseja jogar: "))
if dificuldade == 1:
 vidas = 10
if dificuldade == 2:
 vidas = 5
if dificuldade == 3:
    vidas = 3
listaExibicao = []
for i in palavrasecreta:
    listaExibicao.append(" _ ")
while vidas > 0:
    print (listaExibicao)
    chute = input("digite uma letra:")
    if chute in palavrasecreta:
        for letra in range(0,len(palavrasecreta)):
            if palavrasecreta[letra] == chute:
                listaExibicao[letra] = chute
    else:
        print("a palavra nao tem essa letra")
        vidas=vidas-1
    if " _ " not in listaExibicao:
        print(listaExibicao)
        print("voce ganhou")
        print("pontos:",vidas*10)
        break
if vidas == 0: 
   desenhar()
        