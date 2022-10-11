#Sucesión de Fibonacci

def fibonacci_rec(n):
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return fibonacci_rec(n-2)+fibonacci_rec(n-1)
        return fibonacci_rec(n)

n= int(input("Dime un número: "))
print(fibonacci_rec(n))