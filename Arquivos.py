"""
arquivo = open("numeros.txt","w")

for linha in range(1,100):
    arquivo.write("%d\n" %linha)
arquivo.close()


arquivo = open("numeros.txt","r")

for linha in arquivo.readlines():
    print (linha)
arquivo.close()


with open("numeros.txt") as f:
    print (f.read())

"""

def adiciona():
    nome = input("Nome para adicionar: ")
    ler = open("nomes.txt","w")
    ler.write(nome)
    ler.close()

def verificaNome():
    nome = input("Nome para verificar: ")
    ler = open("nomes.txt","r")
    txt = ler.read()

    if nome in txt:
        print("esse nome está na lista")
        
    

adiciona()
verificaNome()
