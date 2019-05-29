"""
import urllib.request
pagina = urllib.request.urlopen(
    "http://beans.itcarlow.ie/prices-loyalty.html")
texto2 = pagina.read().decode("utf-8")
preco2 = texto2 [250:255]
print (preco2)

"""

import urllib.request
pagina = urllib.request.urlopen(
    "http://beans.itcarlow.ie/prices.html")
texto = pagina.read().decode("utf-8")
preco = float(texto [234:238])
print (preco)

while preco >= 5.29:
        print ("Comprou a ",preco)




