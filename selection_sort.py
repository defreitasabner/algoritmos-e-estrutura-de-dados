from typing import Any, List


def selection_sort(lista: List[Any]) -> None:
    """
    Selection Sort
    ===
    BigO: O(n^2)
    ---
    Executa um algoritmo de `ordenação por seleção`. Percorre toda a lista, comparando valor por valor e `troca valores de posição caso o valor atual seja maior que o valor comparado`. Por possuir `dois loops aninhados`, esse algoritmo tem forma `O(n^2)`.
    """
    for indice_atual in range(len(lista)):
        
        for indice_seguinte in range(indice_atual + 1, len(lista)):

            if lista[indice_seguinte] < lista[indice_atual]:
                print(f'{lista[indice_atual]} maior que {lista[indice_seguinte]}: Trocam de posição.')
                lista[indice_seguinte], lista[indice_atual] = lista[indice_atual], lista[indice_seguinte]
            else:
                print(f'{lista[indice_atual]} menor que {lista[indice_seguinte]}: Não trocam de posição.')

    return lista