from utils.decorators import performance_check
from typing import Any, List

@performance_check
def selection_sort(lista: List[Any]) -> None:
    for i in range(len(lista)):
        lower_value_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[lower_value_index]:
                lower_value_index = j
        if lower_value_index != i:
            lista[i], lista[lower_value_index] = lista[lower_value_index], lista[i]
    return lista