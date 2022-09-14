from typing import Any, List

def insertion_sort(lista: List[Any]):
    for scanIndex in range(1, len(lista)): 
        temp = lista[scanIndex] 
        minIndex = scanIndex
        while minIndex > 0 and temp < data[minIndex - 1]: 
            lista[minIndex] = lista[minIndex - 1] 
            minIndex -= 1
            lista[minIndex] = temp
        print(lista)
    