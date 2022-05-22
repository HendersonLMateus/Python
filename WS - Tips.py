import requests
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup

html = requests.get("https://oddslot.fr/foot-matchs-du-jour/?page=10").content
soup = BeautifulSoup(html, 'html.parser')

pdf = canvas.Canvas("Tips.pdf")

partida = []
cont = 800
b = 0

#Partidas -resultado
x = soup.find_all("strong")
for child in x:
    partida.append(str(child.contents))
    
#jogo1
p = partida
del(p[0:4])
casa = p[0]
fora = p[1]
por = p[4]
por = por[2:5]
res = p[8]
res = res[2:4]

print("Jogo 1: \n Casa: "+casa
      +"\n Fora: "+fora+
      " \n O resultado é: "+res+
      " \n Porcentagem de: "+por)

casa2 = p[12]
fora2 = p[13]
res2 = p[20]
res2 = res2[2:4]
por2 = p[16]
por2 = por2[2:5]

p2 = [casa2,fora2,res2,por2]

print("Jogo 2: \n Casa: "+casa2
      +"\n Fora: "+fora2+
      " \n O resultado é: "+res2+
      " \n Porcentagem de: "+por2)

for i in p2:
    pdf.drawString(50,cont,p2[b])
    cont -= 15
    b += 1
    
pdf.save()
