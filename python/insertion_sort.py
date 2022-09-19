from typing import Any, List

def insertion_sort(lista: List[Any]):
    
    print(f'Iniciando Insertion Sort na lista: {lista}')
    print('-------------------------------------------')
    
    # Percorre toda a lista do início ao fim
    for indice_atual in range(1, len(lista)):
        print(f'========= Iteração {indice_atual} ==========')
        print(f'Lista Inicial da Iteração: {lista}')
        menor_valor = lista[indice_atual]
        indice_menor_valor = indice_atual
        print(f'- Menor valor: {menor_valor}')
        
        # Caso o índice do menor valor seja maior que zero e
        # o menor valor seja menor que o valor anterior a ele, substitui os valores
        while indice_menor_valor > 0 and menor_valor < lista[indice_menor_valor - 1]: 
            print(f'-> {menor_valor} é menor que o valor anterior ({lista[indice_menor_valor - 1]}) - TROCA')
            lista[indice_menor_valor] = lista[indice_menor_valor - 1] 
            indice_menor_valor -= 1 # diminui o índice de menor valor para coincidir com a nova posição
            lista[indice_menor_valor] = menor_valor
            print(lista)

    return lista
