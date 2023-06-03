from utils.gera_lista_exemplo import gera_lista_exemplo
from algoritmos.ordenacao.bubble_sort import bubble_sort
from algoritmos.ordenacao.insertion_sort import insertion_sort
from algoritmos.ordenacao.selection_sort import selection_sort

sample_list = gera_lista_exemplo(1000)

bubble_sort(sample_list)
selection_sort(sample_list)
insertion_sort(sample_list)
