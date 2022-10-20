# Atividade 2

## Descrição

Implementar um algoritmo que realize a Busca em Profundidade em um grafo.

- [X] Implementar funções que informe se o elemento foi ou não encontrado e em qual posição/chamada se encontra, não de pertencer ao grafo;
- [ ] Realizar testes com grafos de diversas densidades;
- [X] Escolher se a representação será por Matriz ou lista de Adjacência.

## Algoritmo em Grafos - DFS
#### Busca em Profundidade

````
DFS(G)
for cada vertice u E V[G]  <--|
    u.cor = BRANCO            | O(V) -> Custo e complexidadedo Algoritmo
    u.PI = NULO <-------------|
tempo = 0 // Global       ----> O(1)

for cada vertice u E V[G] <--|
    if u.cor == BRANCO       |  O(V)
        DFS_VISITA(G, u) <---|
````
```
DFS_VISITA()
tempo = tempo + 1  <--|
u.d = tempo           | O(V)
u.cor = CINZA <-------|

for cada v E adv[u]  <-------|
    if v.cor ==BRANCO        |  O(E)
        v.PI = u             |
        DFS_VISITA[G, v] <---|
u.cor = PRETO
tempo = tempo + 1
u.f = tempo

```
### Complexidade final de tempo
tempo = O(V+E)




