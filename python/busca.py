from utils.gera_lista_exemplo import gera_lista_exemplo
from algoritmos.busca.sequential_search import sequential_search
from algoritmos.busca.binary_search_tree import BinarySearchTree

sample_list = gera_lista_exemplo(1000)
search_value = sample_list[-1] # pior cenário

sequential_search(sample_list, search_value)

tree = BinarySearchTree.create_from_list(sample_list)
tree.search(search_value)
