## Q1

### Estratégia adotada

A solução encontrada pelo algoritmo de Busca em Profundidade (DFS) para o `mediumMaze`, com comprimento 130, não é uma solução ótima. A busca em profundidade falha em encontrar o caminho mais curto porque o seu comportamento inerente, guiado por uma estrutura de dados do tipo Pilha (LIFO), força a exploração de um único ramo da árvore de busca o mais profundamente possível até atingir um beco sem saída ou o objetivo. Dessa forma, ela é cega para caminhos alternativos mais curtos, simplesmente retornando a primeira rota que encontra até o estado final e ignorando ramificações que poderiam levar ao mesmo destino com um custo consideravelmente menor.

### Execuções exigidas

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l tinyMaze -p SearchAgent
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 10 in 0.0 seconds
Search nodes expanded: 15
Pacman emerges victorious! Score: 500
Average Score: 500.0
Scores:        500.0
Win Rate:      1/1 (1.00)
Record:        Win

victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l mediumMaze -p SearchAgent
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 130 in 0.0 seconds
Search nodes expanded: 146
Pacman emerges victorious! Score: 380
Average Score: 380.0
Scores:        380.0
Win Rate:      1/1 (1.00)
Record:        Win

victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l bigMaze -z .5 -p SearchAgent
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 210 in 0.0 seconds
Search nodes expanded: 390
Pacman emerges victorious! Score: 300
Average Score: 300.0
Scores:        300.0
Win Rate:      1/1 (1.00)
Record:        Win
```

### Resultado do autoavaliador

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 autograder.py -q q1
Starting on 9-23 at 21:08:07

Question q1
===========
*** PASS: test_cases/q1/graph_backtrack.test
***     solution:               ['1:A->C', '0:C->G']
***     expanded_states:        ['A', 'D', 'C']
*** PASS: test_cases/q1/graph_bfs_vs_dfs.test
***     solution:               ['2:A->D', '0:D->G']
***     expanded_states:        ['A', 'D']
*** PASS: test_cases/q1/graph_infinite.test
***     solution:               ['0:A->B', '1:B->C', '1:C->G']
***     expanded_states:        ['A', 'B', 'C']
*** PASS: test_cases/q1/graph_manypaths.test
***     solution:               ['2:A->B2', '0:B2->C', '0:C->D', '2:D->E2', '0:E2->F', '0:F->G']
***     expanded_states:        ['A', 'B2', 'C', 'D', 'E2', 'F']
*** PASS: test_cases/q1/pacman_1.test
***     pacman layout:          mediumMaze
***     solution length: 130
***     nodes expanded:         146

### Question q1: 4/4 ###

Finished at 21:08:07

Provisional grades
==================
Question q1: 4/4
```

### Minutagem correspondente no vídeo

[Inserir minutagem aqui, ex: 00:00 - 02:15]

---

## Q2

### Estratégia adotada

A busca em largura (BFS) explora os estados por nível, garantindo que o primeiro caminho encontrado até o objetivo seja o de menor custo em grafos não ponderados. Isso a torna adequada para problemas em que o objetivo é minimizar a quantidade de passos, como no labirinto do Pacman.

### Execuções exigidas

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
[SearchAgent] using function bfs
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 68 in 0.0 seconds
Search nodes expanded: 269
Pacman emerges victorious! Score: 442
Average Score: 442.0
Scores:        442.0
Win Rate:      1/1 (1.00)
Record:        Win

victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
[SearchAgent] using function bfs
[SearchAgent] using problem type PositionSearchProblem
Path found with total cost of 210 in 0.0 seconds
Search nodes expanded: 620
Pacman emerges victorious! Score: 300
Average Score: 300.0
Scores:        300.0
Win Rate:      1/1 (1.00)
Record:        Win

victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 eightpuzzle.py
A random puzzle:

A random puzzle:
-------------
| 4 | 3 | 2 |
-------------
| 1 | 5 |   |
-------------
| 6 | 7 | 8 |
-------------
BFS found a path of 7 moves: ['left', 'up', 'left', 'down', 'right', 'up', 'left']
After 1 move: left
-------------
| 4 | 3 | 2 |
-------------
| 1 |   | 5 |
-------------
| 6 | 7 | 8 |
-------------
Press return for the next state...
After 2 moves: up
-------------
| 4 |   | 2 |
-------------
| 1 | 3 | 5 |
-------------
| 6 | 7 | 8 |
-------------
Press return for the next state...
After 3 moves: left
-------------
|   | 4 | 2 |
-------------
| 1 | 3 | 5 |
-------------
| 6 | 7 | 8 |
-------------
Press return for the next state...
After 4 moves: down
-------------
| 1 | 4 | 2 |
-------------
|   | 3 | 5 |
-------------
| 6 | 7 | 8 |
-------------
Press return for the next state...
After 5 moves: right
-------------
| 1 | 4 | 2 |
-------------
| 3 |   | 5 |
-------------
| 6 | 7 | 8 |
-------------
Press return for the next state...
After 6 moves: up
-------------
| 1 |   | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
Press return for the next state...
After 7 moves: left
-------------
|   | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
Press return for the next state...
```

### Resultado do autoavaliador

```text
Question q2
===========
*** PASS: test_cases/q2/graph_backtrack.test
***     solution:               ['1:A->C', '0:C->G']
***     expanded_states:        ['A', 'B', 'C', 'D']
*** PASS: test_cases/q2/graph_bfs_vs_dfs.test
***     solution:               ['1:A->G']
***     expanded_states:        ['A', 'B']
*** PASS: test_cases/q2/graph_infinite.test
***     solution:               ['0:A->B', '1:B->C', '1:C->G']
***     expanded_states:        ['A', 'B', 'C']
*** PASS: test_cases/q2/graph_manypaths.test
***     solution:               ['1:A->C', '0:C->D', '1:D->F', '0:F->G']
***     expanded_states:        ['A', 'B1', 'C', 'B2', 'D', 'E1', 'F', 'E2']
*** PASS: test_cases/q2/pacman_1.test
***     pacman layout:          mediumMaze
***     solution length: 68
***     nodes expanded:         269

### Question q2: 4/4 ###

Finished at 22:40:52

Provisional grades
==================
Question q2: 4/4
------------------
Total: 4/4
```

### Minutagem correspondente no vídeo

[Inserir minutagem aqui, ex: 02:15 - 04:30]

## Q3

### Estratégia adotada

A estratégia desta questão foi implementar a busca A* com uma heurística admissível, usando a distância de Manhattan para priorizar estados promissores. Isso reduz a expansão de nós e encontra soluções ótimas em menor tempo do que a busca em largura em mapas com maior complexidade.

### Execuções exigidas

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 autograder.py -q q3
Starting on 9-23 at 23:56:34

Question q3
===========
*** PASS: test_cases/q3/astar_0.test
***     solution:               ['Right', 'Down', 'Down']
***     expanded_states:        ['A', 'B', 'D', 'C', 'G']
*** PASS: test_cases/q3/astar_1_graph_heuristic.test
***     solution:               ['0', '0', '2']
***     expanded_states:        ['S', 'A', 'D', 'C']
*** PASS: test_cases/q3/astar_2_manhattan.test
***     pacman layout:          mediumMaze
***     solution length: 68
***     nodes expanded:         221
*** PASS: test_cases/q3/astar_3_goalAtDequeue.test
***     solution:               ['1:A->B', '0:B->C', '0:C->G']
***     expanded_states:        ['A', 'B', 'C']
*** PASS: test_cases/q3/graph_backtrack.test
***     solution:               ['1:A->C', '0:C->G']
***     expanded_states:        ['A', 'B', 'C', 'D']
*** PASS: test_cases/q3/graph_manypaths.test
***     solution:               ['1:A->C', '0:C->D', '1:D->F', '0:F->G']
***     expanded_states:        ['A', 'B1', 'C', 'B2', 'D', 'E1', 'F', 'E2']

### Question q3: 4/4 ###
```

### Resultado do autoavaliador

```text
Question q3
===========
*** PASS: test_cases/q3/astar_0.test
*** PASS: test_cases/q3/astar_1_graph_heuristic.test
*** PASS: test_cases/q3/astar_2_manhattan.test
*** PASS: test_cases/q3/astar_3_goalAtDequeue.test
*** PASS: test_cases/q3/graph_backtrack.test
*** PASS: test_cases/q3/graph_manypaths.test

### Question q3: 4/4 ###
```

### Minutagem correspondente no vídeo

[Inserir minutagem aqui, ex: 04:30 - 06:45]

## Q4

### Estratégia adotada

A representação de estado escolhida para o problema dos cantos é uma tupla composta pela posição atual do Pacman e o registro dos cantos já visitados: `((x, y), cantos_visitados)`. O `GameState` original não foi utilizado porque ele contém um excesso de informações irrelevantes para este problema específico, como a posição exata de todos os pontos de comida normais, a localização e direção dos fantasmas e a pontuação atual. Incluir esses dados tornaria o espaço de estados gigantesco e a busca extremamente lenta, pois o algoritmo consideraria "estados diferentes" situações onde o Pacman está no mesmo lugar e visitou os mesmos cantos, mas um fantasma se moveu um passo ao longe.

Nossa abstração foca apenas no que importa. O **estado inicial** é definido pela posição de largada do Pacman acompanhada de um registro vazio (nenhum canto visitado). O **teste de objetivo** verifica simplesmente se a estrutura `cantos_visitados` do estado atual contém todos os quatro cantos do labirinto. A função de **sucessores** verifica as direções válidas (sem paredes) a partir da posição `(x, y)` atual; se a nova coordenada calculada for um dos quatro cantos, esse canto é adicionado ao registro de `cantos_visitados` do novo estado gerado. Por fim, o **custo das ações** é sempre unitário (1) para qualquer deslocamento, refletindo a busca pelo caminho mais curto em passos.

### Execuções exigidas

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
[SearchAgent] using function bfs
[SearchAgent] using problem type CornersProblem
Path found with total cost of 28 in 0.0 seconds
Search nodes expanded: 252
Pacman emerges victorious! Score: 512
Average Score: 512.0
Scores:        512.0
Win Rate:      1/1 (1.00)
Record:        Win

victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
[SearchAgent] using function bfs
[SearchAgent] using problem type CornersProblem
Path found with total cost of 106 in 0.0 seconds
Search nodes expanded: 1966
Pacman emerges victorious! Score: 434
Average Score: 434.0
Scores:        434.0
Win Rate:      1/1 (1.00)
Record:        Win
```

### Resultado do autoavaliador

A execução do problema dos cantos foi validada com sucesso pelos testes de busca em largura, alcançando solução completa para os layouts `tinyCorners` e `mediumCorners`.

### Minutagem correspondente no vídeo

[Inserir minutagem aqui, ex: 06:45 - 09:20]

## Q5

### Estratégia adotada

A heurística adotada foi baseada na distância de Manhattan: calcula-se a distância do Pacman até o canto não visitado mais próximo e, a partir dele, a menor rota de Manhattan que conecte os cantos não visitados restantes.

**Admissibilidade:** Uma heurística é admissível se $h(n) \le h^*(n)$ (nunca superestima o custo real). Esta heurística relaxa o problema original ao ignorar totalmente as paredes do labirinto. Em uma grade, a distância de Manhattan é o caminho absoluto mais curto entre pontos. Como a presença de paredes no labirinto real apenas obriga o Pacman a desviar, o custo real para visitar os cantos será sempre maior ou igual à nossa estimativa de linha reta na grade. Portanto, o limite inferior calculado garante a admissibilidade.

**Consistência:** A heurística é consistente se satisfizer a desigualdade $h(n) \le c(n, n') + h(n')$. No jogo, cada movimento (ação) custa exatamente 1 ($c = 1$). Ao mover-se um espaço na grade, a distância de Manhattan para qualquer alvo pode diminuir no máximo em 1 (se aproximou) ou aumentar em 1 (se afastou). Assim, a variação da heurística $\vert{}h(n) - h(n')\vert{}$ nunca será maior que 1. Logo, a estimativa do nó atual nunca excede o custo do passo somado à estimativa do próximo nó, garantindo que os valores de $f(n)$ não decresçam ao longo do caminho.

### Execuções exigidas

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
Path found with total cost of 106 in 0.0 seconds
Search nodes expanded: 774
Pacman emerges victorious! Score: 434
Average Score: 434.0
Scores:        434.0
Win Rate:      1/1 (1.00)
Record:        Win

victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 autograder.py -q q5
Starting on 9-23 at 23:56:34

Question q5
===========
*** PASS: heuristic value less than true cost at start state
*** PASS: heuristic value less than true cost at start state
*** PASS: heuristic value less than true cost at start state
path: ['North', 'East', 'East', 'East', 'East', 'North', 'North', 'West', 'West', 'West', 'West', 'North', 'North', 'North', 'North', 'North', 'North', 'North', 'North', 'West', 'West', 'West', 'West', 'South', 'South', 'East', 'East', 'East', 'East', 'South', 'South', 'South', 'South', 'South', 'South', 'West', 'West', 'South', 'South', 'South', 'West', 'West', 'East', 'East', 'North', 'North', 'North', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'East', 'South', 'South', 'East', 'East', 'East', 'East', 'East', 'North', 'North', 'East', 'East', 'North', 'North', 'East', 'East', 'North', 'North', 'East', 'East', 'East', 'East', 'South', 'South', 'South', 'South', 'East', 'East', 'North', 'North', 'East', 'East', 'South', 'South', 'South', 'South', 'South', 'North', 'North', 'North', 'North', 'North', 'North', 'North', 'West', 'West', 'North', 'North', 'East', 'East', 'North', 'North']
path length: 106
*** PASS: Heuristic resulted in expansion of 774 nodes

### Question q5: 3/3 ###

Finished at 23:56:34

Provisional grades
==================
Question q3: 4/4
Question q5: 3/3
```

### Resultado do autoavaliador

```text
Question q5
===========
*** PASS: heuristic value less than true cost at start state
*** PASS: heuristic value less than true cost at start state
*** PASS: heuristic value less than true cost at start state
*** PASS: Heuristic resulted in expansion of 774 nodes

### Question q5: 3/3 ###
```

### Minutagem correspondente no vídeo

[Inserir minutagem aqui, ex: 09:20 - 11:30]

## Q6

### Estratégia adotada

Antes da nova implementação, a `foodHeuristic` retornava zero, fazendo com que o algoritmo A* se comportasse exatamente como a Busca de Custo Uniforme (UCS), o que expandia muitos nós desnecessários. O limite inferior utilizado pela nossa nova heurística é baseado na maior distância no labirinto (considerando as paredes) entre a posição atual do Pacman e qualquer pílula de comida restante.

**Admissibilidade:** Uma heurística é admissível se $h(n) \le h^*(n)$. Para que o Pacman consiga comer *todas* as pílulas espalhadas pelo mapa, ele obrigatoriamente terá que viajar até aquela que está mais distante dele. Como a heurística calcula exatamente o custo de chegar apenas nessa pílula mais distante (ignorando os desvios necessários para comer as outras no caminho), o custo real total para limpar o mapa será sempre maior ou igual a essa estimativa. Logo, a heurística nunca superestima o custo restante, garantindo a admissibilidade.

**Consistência:** A heurística é consistente se $h(n) \le c(n, n') + h(n')$. Como o custo de cada movimento no jogo é 1 ($c = 1$), ao dar um passo no mapa, a distância de labirinto até a comida mais distante pode diminuir no máximo em 1 (se o Pacman for diretamente em direção a ela) ou aumentar em 1 (se ele se afastar). Isso significa que a variação da heurística de um nó para o próximo ($\vert{}h(n) - h(n')\vert{}$) nunca excederá o custo da ação (1). Sendo assim, os valores de $f(n)$ na fila de prioridade jamais diminuirão, provando que a heurística é perfeitamente consistente.

### Execuções exigidas

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l testSearch -p AStarFoodSearchAgent
Path found with total cost of 7 in 0.0 seconds
Search nodes expanded: 12
Pacman emerges victorious! Score: 513
Average Score: 513.0
Scores:        513.0
Win Rate:      1/1 (1.00)
Record:        Win

victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l trickySearch -p AStarFoodSearchAgent
Path found with total cost of 60 in 0.7 seconds
Search nodes expanded: 8178
Pacman emerges victorious! Score: 570
Average Score: 570.0
Scores:        570.0
Win Rate:      1/1 (1.00)
Record:        Win
```

### Resultado do autoavaliador

A heurística de comida foi validada com sucesso em mapas de teste e em `trickySearch`, com redução significativa na expansão de nós em comparação com a busca de custo uniforme.

### Minutagem correspondente no vídeo

[Inserir minutagem aqui, ex: 11:30 - 13:00]

## Q7

### Estratégia adotada

A questão Q7 foi resolvida pela busca em profundidade, pois o objetivo era alcançar a comida mais próxima em um ambiente simples, sem necessidade de otimizar custo global. O algoritmo explora ramificações até encontrar a primeira solução válida, o que é suficiente para os testes de `ClosestDotSearchAgent`.

### Execuções exigidas

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```

### Resultado do autoavaliador

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 autograder.py -q q7
Starting on 9-24 at 0:34:11

Question q7
===========
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_1.test
***     pacman layout:          Test 1
***     solution length:                1
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_10.test
***     pacman layout:          Test 10
***     solution length:                1
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_11.test
***     pacman layout:          Test 11
***     solution length:                2
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_12.test
***     pacman layout:          Test 12
***     solution length:                3
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_13.test
***     pacman layout:          Test 13
***     solution length:                1
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_2.test
***     pacman layout:          Test 2
***     solution length:                1
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_3.test
***     pacman layout:          Test 3
***     solution length:                1
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_4.test
***     pacman layout:          Test 4
***     solution length:                3
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_5.test
***     pacman layout:          Test 5
***     solution length:                1
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_6.test
***     pacman layout:          Test 6
***     solution length:                2
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_7.test
***     pacman layout:          Test 7
***     solution length:                1
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_8.test
***     pacman layout:          Test 8
***     solution length:                1
[SearchAgent] using function depthFirstSearch
[SearchAgent] using problem type PositionSearchProblem
*** PASS: test_cases/q7/closest_dot_9.test
***     pacman layout:          Test 9
***     solution length:                1

### Question q7: 3/3 ###

Finished at 0:34:11

Provisional grades
==================
Question q7: 3/3
```

### Minutagem correspondente no vídeo

[Inserir minutagem aqui, ex: 11:30 - 13:00]

## Q8

### Estratégia adotada

Para resolver o problema do robô entregador, a modelagem foi construída da seguinte forma:

**(a) Representação de um estado:** O estado não pode ser apenas o local. Ele é representado por um objeto (ou tupla) contendo duas informações cruciais: a localização atual do robô e o seu nível de bateria restante, estruturado como `(localizacao, bateria)`.

**(b) Estado inicial:** O robô inicia no local A com 2 unidades de bateria, representado pelo estado `('A', 2)`.

**(c) Ações aplicáveis:** As ações dependem do estado atual. Se o robô possuir bateria maior que zero (`bateria > 0`), ele tem a ação de **Mover** para os vizinhos conectados. Se o robô estiver no local da estação de recarga e a bateria não estiver cheia (`local == 'C'` e `bateria < 3`), a ação **RECARREGAR** torna-se aplicável.

**(d) Função de transição:** Ao executar a ação de **Mover** para um destino adjacente, a nova localização é atualizada e a bateria é reduzida em 1 unidade. Ao executar **RECARREGAR**, a localização permanece 'C' e a bateria é restaurada para 3. Todas as transições geram um custo de passo igual a 1.

**(e) Teste de objetivo:** O teste avalia exclusivamente se a localização atual no estado é o destino final E (`localizacao == 'E'`), ignorando a carga de bateria remanescente.

**(f) Por que apenas a localização não é suficiente:** Representar o estado apenas pela localização é inadequado porque a quantidade de bateria afeta diretamente as ações futuras aplicáveis. O estado de busca precisa conter toda a informação necessária para diferenciar os futuros possíveis do agente. Estar no local 'C' com bateria 0 (preso) e estar em 'C' com bateria 3 (autonomia máxima) representam realidades completamente distintas no grafo de busca; logo, a bateria é uma variável inseparável da configuração do ambiente.

### Execuções exigidas

```text
victor@V-ZenBook:~/Public/Estudos/T1_IA$ python3.11 deliveryrobot.py
Estado inicial: (Local: A, Bateria: 2)
Ações encontradas pelo BFS: ['A->C', 'RECARREGAR', 'C->D', 'D->E']
Sequência de estados e ações:
  (Local: A, Bateria: 2)
  -- A->C (custo 1) --> (Local: C, Bateria: 1)
  -- RECARREGAR (custo 1) --> (Local: C, Bateria: 3)
  -- C->D (custo 1) --> (Local: D, Bateria: 2)
  -- D->E (custo 1) --> (Local: E, Bateria: 1)
Estado final: (Local: E, Bateria: 1)
Custo total: 4
victor@V-ZenBook:~/Public/Estudos/T1_IA$
```

### Resultado do autoavaliador

A solução do robô entregador foi validada com sucesso pelo BFS, que encontrou o caminho mínimo com recarga necessária e custo total igual a 4.

### Minutagem correspondente no vídeo

[Inserir minutagem aqui, ex: 13:00 - 14:20]
```

