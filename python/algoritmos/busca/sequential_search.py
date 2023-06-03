from utils.decorators import performance_check

@performance_check
def sequential_search(list, search_value):
    for i in range(len(list) - 1):
        if search_value == list[i]:
            return i
    return -1
