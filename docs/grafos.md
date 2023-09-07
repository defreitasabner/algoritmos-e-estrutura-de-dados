# Grafos
Um grafo pode ser representado pela forma `G = (V,E)`, no qual `V` é o conjunto de vértices (*vertex*) e `E` o conjunto de arestas (*edges*). Cada aresta é representada por um par de vértices. Pode ser não-direcionado ou direcionado. Grafos não-direcionados são grafos nos quais a relação entre as arestas não tem sentido definido, ou seja, se existe uma aresta ligando os vértices `A` e `B`, é possível transitar tanto de `A` para `B`, quanto de `B` para `A` através da mesma aresta. Já no caso de grafos direcionados, as arestas possuem um sentido único, ou seja, uma aresta que vai de `A` para `B` não permite o caminho de `B` para `A`.

## Grau do vértice
Chamamos de grau de um vértice o número de arestas que incidem sobre ele. Em grafos não direcionados, o grau de um vértice é exatamente o número de arestas que incidem sobre ele. Em grafos direcionados, o grau de um vértice é o número de arestas que saem mais o número de arestas que chegam num vértice. Em casos de laços próprios (*self-loops*), que só ocorrem em grafos direcionados, o grau do vértice é automaticamente dois, pois existe uma saída (dele mesmo) e uma entrada (nele mesmo).

## Caminho
Um caminho de `v1` a `vn` é um sequência de vértices, tal que `(vi, vi+1)` seja elemento das arestas para todo `i` dentro do intervalo `1` a `n-1`, ou seja, desde que existam arestas entre os vértices. Em grafos não-direcionados, basta que existam as arestas conectando os vértices de partida e o de chegada, diretamente ou passando por outros vértices. Em grafos direcionaodos, vale a mesma coisa, entretanto a direção da aresta importa, então mesmo que exista uma aresta conectando diretamente `A` e `B`, se ela está na direção de `B` para `A` apenas, então não existe caminho de `A` para `B`.

## Formas de representação
Tradicionalmente, além da representação visual, grafos são representados por uma matriz de adjacências ou por uma coleção de listas de adjacências. vale ressaltar que existem vantagens e desvantagens em cada uma das representações e que, independente da representação, representamos apenas os vizinhos diretos de cada vértice. Pode ser que existam caminhos através do acesso à esses vizinhos diretos, nesses casos, existem métodos para descobrir isso de uma forma não-visual (como o produto de matrizes, por exemplo).
### Matriz de adjacências
Seja `G = (V,E)` um grafo com `n` vértices, uma matriz de adjacências `A` é uma matriz `n x n` tal que:
- `A[i,j] = 1`, se houver uma aresta ligando o vértice `i` para o `j`
- `A[i,j] = 0` se não houver ligação entre os vértices
### Lista de adjacências
Uma lista de adjacências de um grafo com `n` vértices consiste de um arranjo de `n` listas encadeadas, uma para cada vértice do grafo. Cada elemento encadeado representa um vizinho direto do vértice.
### Vantagens e desvantagens de cada representação
- A representação por matriz de adjacências exige a alocação de memória no momento da declaração da matriz, o que pode levar a problemas de falta de memória conforme o grafo cresce ou de desperdício de memória caso seja alocado mais memória do que o necessário
- Em grafos densos, com muitas arestas em relação ao número de vértice, as listas de adjacência ocupam mais memória do que as matrizes
- Matrizes de adjacência ocupam o mesmo espaço em grafos esparsos ou densos, já que o `0` ocupa o mesmo espaço que o `1`
- Listas de adjacência são melhores para realizarmos buscas, pois já temos todos os adjacentes do nó encadeados
- Verificar se existe aresta entre dois vértices, dados seus índices, é melhor com matrizes de adjacência, pois trata-se apenas de verificação de índices, que é feita em tempo constante
- Encontrar os predecessores de um vértice é melhor em matrizes, pois basta verificar a coluna do vértice na matriz. Já em listas, precisaríamos varrer todas as listas para te certeza

## Aplicações da estrutura
Grafos podem nos ajudar a representar, dentre muitos outros exemplos:
- Cidades conectadas por estradas
- Pessoas conectadas por relacionamentos
- Páginas web conectadas por links
- Átomos conectados por ligações químicas
- Filmes conectados por preferência de usuário
- Seres vivos conectados por relações ecológicas