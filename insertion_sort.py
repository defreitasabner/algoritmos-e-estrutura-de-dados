from typing import Any, List

def insertion_sort(lista: List[Any]):
    
    # Percorre toda a lista do início ao fim
    for indice_atual in range(1, len(lista)): 
        menor_valor = lista[indice_atual] 
        indice_menor_valor = indice_atual
        
        while indice_menor_valor > 0 and menor_valor < lista[indice_menor_valor - 1]: 
            lista[indice_menor_valor] = lista[indice_menor_valor - 1] 
            indice_menor_valor -= 1
            lista[indice_menor_valor] = menor_valor
