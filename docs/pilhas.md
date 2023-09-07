# Pilhas (Stack)
As pilhas são estruturas de dados no qual cada novo elemento é inserido no topo da pilha. No momento da remoção, apenas o elemento mais ao topo da pilha pode ser removido. Podemos resumir o funcionamento das pilhas como: **O último que entra é o primeiro a sair**. Para ilustrar, pense numa pilha de papéis sobre uma mesa qualquer, na qual, você só consegue acessar os papéis mais ao fundo da pilha se remover os papéis que estão no topo da pilha.

## Operações típicas de pilhas
### Inserir (insert / push)
Empilha um novo elemento no topo da pilha.
### Remover (remove / pop)
Desempilha o elemento mais ao topo da pilha.
### Topo (top)
Acessa o elemento do topo da pilha, sem desempilhá-lo.
### Vazia (empty)
Verifica se a pilha está vazia.

## Principais usos:
Modelagem de situações onde vamos precisar guardar os elementos na ordem que ele entraram na sequência, para lembrar sempre qual foi o último elemento armazenado, que será sempre o primeiro a ser removido nessa estrutura de dados. **Pilhas são usadas para gerenciar chamada de funções**. Quando chamamos uma função no nosso código, ela é adicionada à pilha. **Se uma função que já está na pilha chama uma nova função, a nova função chamada é adicionada à pilha, sendo empilhada logo acima da função que a chamou.** Quando as funções executam seu retorno, elas são removidas da pilha e o programa volta à execução da função logo abaixo dela na pilha, até que não exista nenhuma função na pilha.