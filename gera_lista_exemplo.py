import random
from typing import List

def gera_lista_exemplo(tamanho_lista: int) -> List[int]:
    
    lista_exemplo = []

    for i in range(tamanho_lista):
        valor_aleatorio = int(((random.random() * 99) % 100))
        if valor_aleatorio in lista_exemplo:
            while valor_aleatorio in lista_exemplo:
                valor_aleatorio = int(((random.random() * 99) % 100))
        lista_exemplo.append(valor_aleatorio)

    print(f'Lista de exemplo gerada: {lista_exemplo}')

    return lista_exemplo