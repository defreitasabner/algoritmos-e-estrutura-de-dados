# Árvores (Tree)
Uma árvore é um conjunto de nós em que existe um nó denominado raiz `r`, que contém zero ou mais subárvores cujas raízes estão diretamente ligadas à raiz `r`. Um subárvore também é uma árvore, logo, a definição de árvore é recursiva. Árvores não são estuturas lineares, pois podem existir mais de um sucessores para o mesmo nó, já que não há um número máximo de sucessores por nó. São estruturas de dados adequadas para representar hierarquia dos dados.
## Nomenclaturas em árvores
- Grau de um nó: número de subárvores do nó
- Nó folha: nó de grau zero, ou seja, sem nós filhos
- Nó interno: nó com grau maior que zero, ou seja, essencialmente todo nó que não é folha
- Descendentes: todos os nós abaixo de um determinado nó
- Altura de um nó: comprimento do caminho mais longo entre o nó até sua folha mais distante
- Altura da árvore: altura do nó raiz
- Profundidade de um nó: distância percorrida da raiz até o nó, sendo a profundidade do nó raiz igual a 0
- Árvore binária: árvore em que abaixo de cada nó só existem no máximo duas subárvores

## Árvores Binárias de Busca
Árvore binária em que, a cada nó, todos os registros com chaves menores que a do nó pai estão na subárvore da esquerda, enquanto que os registros com chaves maiores estão na subárvore da direita. Inserções, remoções e buscas possuem número de comparações proporcional á altura da árvore. Os algoritmos de busca, inserção e remoção, no pior dos casos, terão um número de comparações proporcional à altura da árvore, entretanto, vale ressaltar que os algoritmos são mais eficientes em árvores balanceadas. Árvores degeneradas tendem a ter uma perfomance ruim, que pode ser equiparável a qualquer outra estrutura linear.

### Buscas
Por conta dessa organização, podemos utilizar a seguinte estratégia de busca:
- Se a chave buscada for igual ao nó, então encontramos o nó e a busca é encerrada. 
- Se a chave for maior que o nó, pesquisamos na subávore da direita. 
- Caso contrário, pesquisamos na subárvore da esquerda.
- Se alcançarmos um nó nulo (NULL), então a busca se encerra.

### Inserções
É similar a busca. Supondo que a árvore não tenha repetições, seguiremos o mesmo fluxo da busca, entretando, **somente inserimos o nó quando o espaço que ele irá ocupar está vazio (NULL):
- Se a chave inserida for igual ao nó e a inserção é encerrada. 
- Se a chave inserida for maior que o nó, o inserimos na subávore da direita. 
- Caso contrário, o inserimos na subárvore da esquerda.

### Remoções
Se o nó a ser removido não possui filhos, ele pode ser simplesmente removido. Se o nó possui filhos, então ele deve ser removido e seu filho deve ser colocado no seu lugar. Se o nó possui mais de um filho, então o cenário se torna mais complexo: podemos remover e substituir pelo sucessor lógico ou podemos ou podemos remover e substituir pelo predecessor lógico.
- O sucessor lógico é sempre o elemento mais à esquerda na subárvore da direita.
- O predecessor lógico é sempre o elemento mais á direita na subárvore da esquerda.

## Percursos
Em muitos algoritmos, precisamos percorrer os nós de maneira sistemática, **visitando cada nó apenas uma vez**. Existem três tipos de percursos mais comuns em árvores binárias: pré-ordem, pós-ordem e em-ordem. **A diferença entre os percursos se refere ao momento em que visitamos o nó raiz das árvores** (incluindo subárvores). Sempre visitamos a **subárvore da esquerda antes de visitarmos a subárvore da direita.** Visitar pode significar muitas coisas, mas vamos tratar como se fosse printar os valores presentes nos nós.
### Pré-ordem
A partir da raiz, visitamos primeiramente o nó raiz, depois os nós a esquerda, começando sempre pela raiz antes de seguir à esquerda. Ao chegar no nó folha à esquerda, voltamos o percurso, dessa vez visitando os filhos à direita. Ao chegar na subárvore à direita da raiz, voltamos à visitar primeiramente a raiz, depois os filhos à esquerda e por último os filhos à direita.
### Pós-ordem
A partir da raiz, visitamos primeiramente os nós à esquerda, iniciando no nó folha mais à esquerda. Depois, retornarmos visitando os nós à direita. Por último, concluímos visitando os nós raiz. É um percurso muito útil para métodos destrutores de árvores, pois ele garante que os filhos serão desalocados antes dos nós pais (raízes).
### Em-ordem
A partir da raiz, visitamos primeiramente os nós à esquerda, iniciando no nó folha mais à esquerda. Depois, visitamos o nó raiz. Por último, visitamos os nós à direita. Esse percurso nos retorna os elementos perfeitamente ordenados em ordem crescente numa árvore binária de busca.

## Aplicações da estrutura
Em geral, podem ser usadas em qualquer situação em que queremos organizar os dados por meio de uma chave usada nas buscas. **Quando inserções e remoções são muito frequentes, as árvores são melhores que vetores ordenados em termos de manuntenção da ordem.** Mesmo que os dois tenham um tempo de busca de `O(logn)`, ao se inserir ou remover um elemento num vetor, o custo de refazer a ordenação pode ser muito maior que o de uma árvore.

## Árvores AVL
São árvores capazes de se alto balancear. Durante as operações de inserção e remoção, ocorrem verificações para saber se a operação irá desbalancear a àrvore e, caso ocorra o desbalanceamento, a árvore será remodelada até voltar a estar balanceada. As detecções de desbalanceamento ocorrem devido ao fator de balanceamento. O fator de balanceamento irá informar o quão balanceada uma árvore está em relação as subárvores presentes à esquerda e à direita. Para calcular esse valor, devemos subtrair o fator de balanceamento dos filhos à direita pelos à esquerda. Toda folha inserida tem fator de balanceamento igual a zero. O fator de balanceamento funciona da seguinte forma:
- Ao inserir um filho à esquerda, devemos reduzir o fator de balanceamento da árvore em `-1`.
- Ao insetir um filho à direita, devemos incrementear o fator de balanceamento em `+1`. 
- Caso o fator de balanceamento saia do intervalo `[-1, 1]`, devemos realizar uma rotação para balancear a árvore.

### Rotações
As rotações consistem em tornar um dos nós raízes filhos da subárvore a direita ou a esquerda, o nó raiz da árvore e deslocar a raiz para a esquerda ou direita. Como a verificação do fator de balanceamemnto ocorre a cada inserção ou remoção, a única variação que precisamos verificar é nos casos desse fator de balancemento se tornar `-2` ou `2`. As regras de rotação são:

| Nó desbalanceado | Filho do nó desbalanceado | Tipo de rotação | Direção da rotação |
| ---------------- | ------------------------- | --------------- | ------------------ |
| +2               | 0 ou +1                   | Simples         | Esquerda           |
| +2               | -1                        | Dupla           | Direita (Filho), Esquerda (Pai) |
| -2               | +1                        | Dupla           | Esquerda (Filho), Direita (Pai) |
| -2               | -1 ou 0                   | Simples         | Direita             |

Basicamente, quando os sinais do nó pai desbalanceado e o do seu filho de maior valor forem iguais, a rotação será simples. Quando os sinais forem diferentes ocorrerá uma rotação dupla.