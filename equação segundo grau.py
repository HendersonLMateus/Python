a = int(input("Digite o A "))
b = int(input("Digite o B "))
c = int(input("Digite o C "))

delta = (b**2) - (4*a*c)

x1 = (-b - (delta**(1/2)))/(2*a)
x2 = (-b + (delta**(1/2)))/(2*a)

print ("O delta é: ",delta,"sua raiz é :", (delta**(1/2)))
print ("X negativo é: ",x1)
print ("X positivo", x2)
