from typing import Any, List


def selection_sort(lista: List[Any]) -> None:
    """
    Selection Sort
    ===
    BigO: O(n^2)
    ---
    Executa um algoritmo de `ordenação por seleção`. Percorre toda a lista, comparando valor por valor e `troca valores de posição caso o valor atual seja maior que o valor comparado`. Por possuir `dois loops aninhados`, esse algoritmo tem forma `O(n^2)`.
    """
    print(f'Iniciando Selection Sort na lista: {lista}')
    print('-------------------------------------------')

    for indice_atual in range(len(lista)):

        # Inicialmente, o menor valor vai apontar para o primeiro item da lista
        print(f'========= Iteração {indice_atual} ==========')
        indice_menor_valor = indice_atual
        print(f'- Menor valor inicial: {lista[indice_menor_valor]}')

        # Percorre toda a lista a partir do índice atual do loop para frente
        for indice_seguinte in range(indice_atual + 1, len(lista)):

            # Caso algum dos índices seguinte ao índice atual seja menor que o menor valor da lista
            # o valor índice de menor valor é trocado pelo novo menor valor encontrado
            if lista[indice_seguinte] < lista[indice_menor_valor]:
                indice_menor_valor = indice_seguinte
                print(f'- Novo menor valor encontrado: {lista[indice_menor_valor]}')

        # Caso o valor do índice de menor valor seja diferente do índice atual, troca os valores deles
        if indice_menor_valor != indice_atual:
            lista[indice_atual], lista[indice_menor_valor] = lista[indice_menor_valor], lista[indice_atual]
            print(f'Novo menor valor troca de posição com menor valor da iteração.')

        print(f'RESULTADO - Iteração {indice_atual}: {lista}')
        print('----------------------------------------------')

    return lista