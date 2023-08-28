# Tabela Hash (Hash Table)
Tabelas hash são estrutura de dados do tipo chave-valor, ou seja, todo valor tem uma chave associado a ele. Essa estrutura, permite busca em tempo constante, desde que sejam satisfeitas algumas restrições. Dependendo da linguagem de programação, essa estrutura de dados recebe diferentes nomes: dicionários, mapas, arrays associativos, dentre outros. 

## Implementação
- A própria chave deve ser usada para organizar os dados na memória. 
- Cada entrada da estrutura é composta por um par chave-valor.
- A chave é um identificador único e deve ser vista como um endereço para seu valor.
- Pode ser organizada em memória como um vetor, dado que este permite acesso em tempo constante.
- As chaves podem ser de qualquer tipo de dado, mas para efetuarmos a busca no vetor, precisaremos de uma funçãoq que mapeie chaves em números inteiros.

## Funções Hash (Hash Function)
A função hash mapeia cada chave em um intervalo de `0` a `n-1`, onde `n` é a capacidade do arranjo. Funções Hash são suscetíveis à colisões, isso ocorre quando duas chaves diferentes apontam para o mesmo endereço de memória. Devemos evitar colisões ao máximo e sempre tratá-las, caso ocorram. Uma função hash é considerada boa quando miniminiza a ocorrência de colisões.
### Implementação básica
Inicialmente, vamos precisar converter objetos para o tipo inteiro, para podermos associar a algum índice do vetor. Uma forma simples de fazer isso, seria associar cada um dos caracteres de uma `string`, por exemplo, ao seu valor inteiro na tabela `ASCII`. Dessa forma, a palavra `faca` seria equivalente ao inteiro `267` pois teríamos:
~~~
f = 70
a = 65
c = 67
f + (2 * a) + c = 70 + (65 * 2) + 67 = 267
~~~
Porém, dessa forma, teríamos um problema caso o usuário resolve-se registrar um palídrome da palavra, como por exemplo, `caaf`. Quando a palavra `caaf` passasse pela nossa função hash, resultaria no mesmo inteiro `267`, causando uma colisão.
~~~
f = 70
a = 65
c = 67
'faca' = f + (2 * a) + c = 70 + (65 * 2) + 67 = 267
'caaf' = c + (2 * a) + f = 67 + (65 * 2) + 70 = 267
~~~
Para contornar esse problema, podemos considerar a posição dos caracteres, dessa forma a letra `f` na primeira posição da palavra `faca`, teria um valor diferente da letra `f` na última posição na palavra `caaf`. Então poderíamos, pegar o valor de `f` na tabela hash, multiplicar por uma constante arbitrária elevada ao tamanho da string - a posição de `f`:
~~~
f = 70
a = 65
c = 67
constante = 3
'faca' = f + a + c + a = (70*(3^4-1)) + (65*(3^4-2)) + (67*(3^4-3)) + (65*(3^4-4)) = 
'caaf' = c + a + a + f = (70*(3^4-1)) + (65*(3^4-2)) + (67*(3^4-3)) + (65*(3^4-4)) = 
~~~
Quanto maior o valor dessa constante arbitrária, menor o número de colisões, sendo considerados valores altos os valores 33, 37, 39 e 41, por exemplo. Usando 41 e trabalhando com 50.000 palavras da língua inglesa, chegasse em média à 7 colisões apenas. Porém, um valor alto para a constante, pode levar à um overflow do intervalo dos inteiros, já que o resultado pode ser um número muito alto. Por conta disso, é uma boa prática dividir o valor resultante da operação acima pelo `n`, que é o tamanho do vetor. **Outro ponto importante é que quanto maior o vetor, menor o número de colisões.** Por último, **utilizar números primos para o tamanho do vetor também ajuda a reduzir o número de colisões**, já que irá reduzir a ocorrência de restos de divisão 0, por exemplo.

## Tratamento de Colisões
Colisões ocorrem quando duas chaves `k1` e `k2`, ao passar pela função hash `h`, geram hashs iguais: `h(k1) == h(k2)`. Quando isso ocorre, uma inserção pode sobrescrever valores que já estão ocupados. Por isso, quando ocorre uma colisão, devemos impedir que se faça imediatamente a inserção de um novo item diretamente na tabela hash. Para resolver a colisão, precisamos utilizar um espaço adicional na memória ou um espaço desocupado da própria tabela hash.
### Encadeamento Separado
Trata-se de uma estratégia de alocação de memória adicional. Cada elemento do vetor base da tabela hash, será um ponteiro para uma lista encadeada. Todas inserções que gerarem hash iguais, serão adicionadas na lista encadeada correspondente. Boas funções hash farão com que as listas encadeadas tenham nenhum, um ou poucos elementos.
### Teste Linear
Diferente do encadeamente separado, essa estratégia não aloca memória adicional, mas sim utiliza a memória já alocada para o próprio vetor base. Se tentarmos inserir um novo item e o hash coincidir com a posição de algum outro elemento já alocado no vetor base, então, esse índice será incrementado em 1 até que se ache uma posição vaga para o item. Caso chegue ao final do vetor, ocorre uma exceção de colisão. Sempre que formos buscar o elemento que foi inserido dessa forma, o hash irá nos jogar para o primeiro lugar onde aconteceu a colisão, irá comparar as chaves, caso não encontre, continuará procurando incrementando o índice. Entretanto, temos que tomar cuidado com as deleções nesse caso, já que caso deletemos o elemento na posição onde aconteceu a colisão, nossa busca irá bater lá e dizer que o elemento não existe, sendo que na verdade ele existe, mas está numa posição deslocada. Para corrigir isso, precisamos que a deleção deixe um vestígio para que a busca entenda que já existiu um elemento ali e talvez ela precise continuar incrementando o índice. Existem variações desse método de tratar colisões como o Teste Quadrático e o Hashing Duplo. O teste quadrático consiste em, ao invés de incrementar de um em um, incrementar o quadrado e uma contagem sequência de 1 em diante, até encontrar o lugar, por exemplo: 1^2, 2^2, 3^2,...até achar um índice apropriado. O hasing duplo já consiste e utilizar uma segunda função de hashing caso ocorra uma colisão com a primeira.