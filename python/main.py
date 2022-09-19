from gera_lista_exemplo import gera_lista_exemplo
from insertion_sort import insertion_sort
from selection_sort import selection_sort

tamanho_lista = 6
lista_exemplo = gera_lista_exemplo(tamanho_lista)

selection_sort(lista_exemplo)
insertion_sort(lista_exemplo)