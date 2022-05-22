import requests
from bs4 import BeautifulSoup

# Busca a página e passa para a variavel 'soup'
html = requests.get("https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil#Capitais_estaduais").content
soup = BeautifulSoup(html, 'html.parser')

#Definindo variaveis que serão utilizadas
capitais = 27
lista = []

#1° Busca a tag <a> na página
#2º Atribui todos os links href convertidos em string para a variavel nL
#3º É verificado se na variavel existe '#'. Se existir é adicionado a lista
for link in soup.find_all('a'):
    nL = str(link.get("href"))
    if(nL.count("#")):
        lista.append(nL)

# É verificado o index que começa o nome das capitais
# É printado de acordo com a organização da lista
lugar = lista.index("#Capitais_estaduais")
print (lista[lugar+1:lugar+capitais+1])

