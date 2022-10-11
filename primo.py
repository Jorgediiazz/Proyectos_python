def esPrimo(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True


def totalprimosde1a1000():
    lst=[]
    for i in range(1,1001):
        if(esPrimo(i)):
            lst.append(i)
    return(lst)
print(totalprimosde1a1000())