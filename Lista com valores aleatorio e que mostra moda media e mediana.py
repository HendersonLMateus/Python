import statistics as st
import random as rd

lista = []
for i in range(int(input("Qual o tamanho da lista? "))):
    lista.append(rd.randint(1,8))
    

print (lista)

moda = st.mode(lista)
print (moda)

media = st.mean(lista)
print (media)

mediana = st.median (lista)
print (mediana)

def listaa(tamanhoLista):
    lista = []
    for i in range(int(tamanhoLista)):
        lista.append(rd.randint(1,8))
    
    print (lista)
    moda = st.mode(lista)
    print (moda)
    media = st.mean(lista)
    print (media)
    mediana = st.median (lista)
    print (mediana)

listaa(10)
