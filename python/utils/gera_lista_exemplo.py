import random
from typing import List

def gera_lista_exemplo(tamanho_lista: int) -> List[int]:
    return random.sample(range(0, tamanho_lista), tamanho_lista)