from reportlab.pdfgen import canvas
import requests
from bs4 import BeautifulSoup

html = requests.get("https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil#Capitais_estaduais").content
soup = BeautifulSoup(html, 'html.parser')

lista = []
cont = 800
capitais = 27
x = []

pdf = canvas.Canvas("CapitaisBR.pdf")

for link in soup.find_all('a'):
    nL = str(link.get("href"))
    if(nL.count("#")):
        lista.append(nL)

lugar = lista.index("#Capitais_estaduais")

x = lista[lugar+1:lugar+capitais+1]

b = 0
for a in x:
    pdf.drawString(50,cont,x[b])
    cont -= 15
    b += 1
    if (len(x)== 28): break
    
pdf.save()
