from utils.decorators import performance_check
from typing import Any, List

@performance_check
def insertion_sort(list: List[Any]) -> List[Any]:
    for i in range(1, len(list)):
        lower_value = list[i]
        lower_value_index = i
        while lower_value_index > 0 and lower_value < list[lower_value_index - 1]:
            list[lower_value_index] = list[lower_value_index - 1] 
            lower_value_index -= 1
            list[lower_value_index] = lower_value
    return list
