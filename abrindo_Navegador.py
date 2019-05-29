import webbrowser
import time

parada = 3

while (parada != 0):
       print ("Abrindo navegador...")
       time.sleep(3)
       webbrowser.open("https://www.youtube.com/watch?v=cVikZ8Oe_XA&start_radio=1&list=RDcVikZ8Oe_XA")
       parada = parada -1

