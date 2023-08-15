# Lista Lineares
São estruturas de dados na qual **cada elemento é precedido por um elemento e sucedido por outro elemento, com exceção do primeiro que não tem predecessor e do último que não tem sucessor.** Isso gera uma ordem nos elementos, que pode ser a ordem de inclusão. As estruturas de pilha e fila são listas lineares. Existem dois tipos de listas lineares: sequenciais e encadeadas.

| Vantagens | Sequenciais | Encadeadas |
| -------------- | :---------: | :--------: |
| Acesso em tempo constante | :white_check_mark: | :x: |
| Busca binária | :white_check_mark: | :x: |
| Não exige deslocamentos de memória | :x: | :white_check_mark: |
| Tamanho flexível | :x: | :white_check_mark: |

## Listas Lineares Sequenciais
São listas em que **a ordem lógica dos elementos é a mesma da ordem física**. Ou seja, os **elementos vizinhos** numa lista linear sequencial também estão em **posições vizinhas na memória**. Essa posição confere acesso em tempo constante a qualquer elemento, já que dado o índice do elemento e seu tipo, basta uma operação matemática simples para encontrá-lo.
### Vantagens das listas lineares sequenciais
- Tempo constante para acesso a qualquer elemento da lista
- Em vetores ordenados, por conta do tempo constante, é possível aplicar algoritmo de busca binária
### Desvantagens das lista lineares sequenciais
- Necessário **alocar espaço suficiente para todos os elementos ao inicializar** a lista (independente se essa inicialização foi estática ou dinâmica). Caso falte espaço, será necessário copiar todos os elementos para uma nova região de memória, com um vetor maior. Caso sobre espaço, você pode estar desperdiçando memória que pode nunca ser utilizada.
- **Manter a ordem** pode ser muito custoso, pois talvez seja necessário **muitos deslocamentos em memória**. Por exemplo, caso seja necessário inserir um novo elemento no início ou no meio do vetor, será necessário deslocar todos elementos sucessores para uma posição adiante na memória. O mesmo ocorre para remoções.

## Listas Lineares Encadeadas
É um tipo de lista linear em que **a ordem lógica não é a mesma da ordem física**. Os elementos possuem predecessores e sucessores, assim como as demais listas lineares, entretanto esses **elementos ficam espalhados na memória em posições que podem ou não ser vizinhas**. Para que seja mantida a ordem lógica, **cada elemento precisa indicar o endereço do seu sucessor**.
### Vantagens das listas lineares encadeadas
- É possível aumentar ou diminuir o tamanho da lista durante a execução do programa.
- Operações de inserção ou remoção, ou qualquer outra alteração na ordem lógica, não exigem deslocamento de memória.
### Desvantagens das listas lineares encadeadas
- Para encontrar um elemento nesse tipo de lista, precisamos percorrer todos os seus predecessores, um por um. Logo, a principal desvantangem dessas listas é que o **acesso não tem tempo constante**.
- A busca binária não faz mais sentido nesse tipo de lista, já que para obtermos o elemento do meio da lista ordenada, teríamos que acessar todos os seus predecessores, ou seja, metade da lista.