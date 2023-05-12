def bubble_sort(list):
  for iteration in range(len(list)):
    for index in range(len(list) - 1):
      if list[index] > list[index + 1]:
        list[index], list[index + 1] = list[index + 1], list[index]