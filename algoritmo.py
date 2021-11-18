import math
from types import NoneType
lista = []
for item in range(1, 11):
    lista.append(item)
print(lista)

def buscaBinaria(lista, chute):
    inicio = 0
    fim = len(lista)-1
    meio = math.floor((inicio+fim)/2)
    contador = 0
    while inicio <= fim:
        meio = math.floor((inicio+fim)/2)
        if chute > lista[meio]:
            contador += 1
            inicio = meio +1
        elif chute < lista[meio]:
            contador += 1
            fim = meio -1
        elif chute == lista[meio]:
            print(contador)
            return meio
    else:
        return None

indice = buscaBinaria(lista, 7)
print(indice)