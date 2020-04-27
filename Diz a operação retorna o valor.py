n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
op = input("Qual operação deseja fazer: + - * / ")

def case(op):
    if op == "+":
        soma = n1 + n2
        return soma
    elif op == "-":
        menos = n1 - n2
        return menos
    elif op == "*":
        vezes = n1 * n2
        return vezes
    elif op == "/":
        divisao = n1 / n2
        return divisao

a=case(op)
print (a)
