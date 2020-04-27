"""
def fatorialRecursivo(num):
    if (num == 0):
        return 1
    else :
        return fatorialRecursivo(num-1)

fatorialRecursivo (3)


"""

def fatorial(n):
     if n == 0 or n == 1:
         return 1
     else:
         f = n * fatorial(n-1)
         return f
a = fatorial(5)
print (a)
