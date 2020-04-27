import matplotlib.pyplot as plt

print ("Aqui")

x = [100,50]
y = [2,10]

x1 = [70,80]
x2 = [5,8]

y1 = [60,90]
y2 = [4,7]

plt.bar(x,y,label ="Grupo 1")
plt.bar (x1,x2,label = "Grupo 2")
plt.bar (y1,y2,label = "Grupo 3")
plt.title("Grafico")

plt.legend()
plt.show()
