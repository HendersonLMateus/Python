import requests
from bs4 import BeautifulSoup

# Busca a página e atribui a variavel 'soup' #
html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/amanha/cidade/60/fortaleza-ce").content
soup = BeautifulSoup(html, 'html.parser')

# Busca na página, o ID correspondente da temperatura minima e máxima

TempMinF = soup.find_all(id= "min-temp-1")
print(TempMinF)

TempMaxF = soup.find_all(id= "max-temp-1")
print(TempMaxF)

# Transforma o valor encontrado em String e printa a temperatura de acordo
# com o indice na String

Max = str(TempMinF)
Min = str(TempMaxF)
print("Temperatura Minima: "+ Max[43:46])
print("Temperatura Máxima: "+ Min[43:46])

