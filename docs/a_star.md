# Algoritmo A* (A Star)

O A* é um algoritmo de busca heurística eficiente para encontrar o caminho mais curto entre dois pontos em um labirinto ou grafo.

## Como funciona

1. Mantém uma lista de nós abertos (a serem explorados) e fechados (já explorados).
2. Para cada nó, calcula o custo total `f(n) = g(n) + h(n)`:
   - `g(n)`: custo do caminho desde o início até o nó atual.
   - `h(n)`: estimativa heurística do custo até o objetivo (ex: distância de Manhattan).
3. Sempre explora o nó com menor `f(n)`.

## Vantagens

- Garante o caminho mais curto se a heurística for admissível.
- Rápido e eficiente em muitos casos.

## Referências

- [Wikipedia: A*](https://pt.wikipedia.org/wiki/A*_Search_Algorithm)