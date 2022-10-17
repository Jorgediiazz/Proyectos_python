import random
'''
Definir una función que devuelva una
lista con 20 números random
'''
# lista_numeros()
# devuelve por ejemplo ---> [2,4,3,4,5,17,3,4,7,9,10,12,15,16,18,29,98,87, 65, 30]
# len(lista_numeros()) --> 20
# type(lista_numeros)) --> <class 'list'>
def lista_numeros():
    cont=0
    lst=[]
    while(cont<20):
        numale=random.randint(0,100)
        cont+=1
        lst.append(numale)
    return lst

print("Lista numeros aleatorios", lista_numeros())






'''
Definir una función que dado una lista
filtre los números pares
'''
# filtra_lista_pares([1,2,3,4])
# devuelve ---> [2,4]
'''
def filtra_lista_pares(lst):
    lista2=[]
    for i in lst:
        if(i % 2 == 0):
            lista2.append(i)
    return lista2
lst_test=lista_numeros()
print("Lista para sacar los pares",lst_test)
print("Lista de solo pares", filtra_lista_pares(lst_test))
'''




'''
Definir una función que dado una lista y un número
devuelva
   - True si se encuentra el número en la lista
   - False e.c.c.
'''
def busqueda_num(lst, num):
    for i in lst:
        if(i==num):
            print("El numero ", num, " está en la lista")
            return True
        else:
            print("El numero ", num, " no está en la lista")
            return False
        
lista = lista_numeros()
print(lista)
numero=int(input("Dime un numero: "))
busqueda_num(lista,numero)