from time import sleep
from sys import exit

menino = 0
menina = 0
meninalista = []
meninolista = []
resposta = "S"
alunos = dict()

def resp(x):
    x = input("Digite S para continuar ou digite EXIT para encerrar o programa").upper()
    if x == "EXIT":
        print("Saindo do programa....")
        sleep(2)
        print("Fim do programa")
        exit()
    if x == "S":
        return

while resposta == "S":
    print("Escola Estadual Fictícia de Oliveira")
    print("Menu de opções")
    print("[1] Adicione um aluno")
    print("[2] Remova um aluno da lista")
    print("[3] Mostre a lista de alunos")
    print("[4] Mostre a quantidade de meninos e de meninas na lista")
    print("[5] Mostre apenas a lista de meninos e/ou de meninas")
    print("[6] Sair do programa")
    alternativa = str(input("Selecione um número que corresponda a alternativa"))

    if alternativa == "1":
        genero = str(input("Digite o gênero da criança M/F")).upper()
        if genero == "M":
            nome = str(input("Digite o nome del(e)"))
            nota = int(input("Digite a nota del(e)"))
            alunos[nome] = nota
            meninolista.append(nome)

        if genero == "F":
            nome = str(input("Digite o nome del(a)"))
            nota = int(input("Digite a nota del(a)"))
            alunos[nome] = nota
            meninalista.append(nome)
            resp(resposta)

    if alternativa == "3":
        for nome, nota in alunos:
            print(nome)
            resp(resposta)


    if alternativa == "4":
        print("A quantidade de meninos é {}, a quantidade de meninas é {}".format(len(meninolista), len(meninalista)))


    if alternativa == "5":
        mostrar=input("Deseja mostrar Meninos[M] e/ou meninas[F]?").upper()
        if mostrar == "M":
            print(meninolista)
        if mostrar == "F":
            print(meninalista)
            resp(resposta)

    if alternativa == "6":
        print("Saindo do programa....")
        sleep(5)
        print("Fim do programa")
        exit()









