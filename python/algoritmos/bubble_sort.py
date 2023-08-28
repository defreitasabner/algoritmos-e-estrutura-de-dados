from utils.decorators import performance_check

@performance_check
def bubble_sort(list):
  for _ in range(len(list)):
    for j in range(len(list) - 1):
      if list[j] > list[j + 1]:
        list[j], list[j + 1] = list[j + 1], list[j]
  return list