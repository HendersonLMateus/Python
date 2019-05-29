import random

chute = random.randint(1,10)
while (True):
    a = int(input("Diz um numero: "))
    b = int(input("Diz um numero: "))
    if a == chute or b == chute:
        print("Você acertou, o valor é ", chute)
        break
    else:
        print("Errou")
        if a > chute:
            print("Diminui A")
        elif a < chute:
            print ("Aumenta A ")
        if b > chute:
            print("Diminui B")
        elif b < chute:
            print ("Aumenta B ")
