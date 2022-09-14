from gera_lista_exemplo import gera_lista_exemplo
from selection_sort import selection_sort

tamanho_lista = 6
lista_exemplo = gera_lista_exemplo(tamanho_lista)

print(f'Selection Sort: {selection_sort(lista_exemplo)}')