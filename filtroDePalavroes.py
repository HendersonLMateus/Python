#Digite o caminho do arquivo a ser pesquisado

ler = open(r"C:\Users\PANDA CRAZ1\Desktop\Mateus\pythonUdacity\palavroes.txt")
texto = ler.read()
#print(texto)

palavra = input ("Qual palavra você está procurando? ")
while ("true"):
    if (palavra in texto):
        print ("A palavra está no Texto. Ela aparece ", texto.count(palavra), "vezes")
        break
        
        
    else:
        print ("Tem essa merda aqui nao oh")
        break







