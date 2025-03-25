#lista por comprencion 
'''
lista=[100 for i in range(10)]
print(lista)

lista=[i for i in range(10)]
print(lista)

lista=[i*i for i in range(10)]
print(lista)
'''
#llenar una lista con una cantidad aleatoria de numeros entre 5 y 15 los numeros debem ir desde 1 hasta el numero aleatorio

import random

num= random.randint (1,15)
lista=[random.randint (1,100) for i in range (1,num)]
print (lista)

pares=[x for x in lista if x%2==0]
impares=[x for x in lista if x%2!=0]
print(pares)
print(impares)
'''for x in lista:
    if x%2==0:
        print(f'{x}es par ')
        print(f'{x}es impar ')'''

