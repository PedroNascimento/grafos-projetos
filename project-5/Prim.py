'''
    Algoritmo de Prim

    Dado o grafo G, o algoritmo constrói uma árvore geradora T de G com custo mínimo

    escolher um vértice qualquer 'v' em V(G); -> vértice escolhido para ser a raiz de T
    V(T) <- {v}; E(T) <- O/; -> inicialização de T

    para j = 1, ..., n-1 faça
        seja e = xy a aresta de peso mínimo com um extremo x em V(T) e outro y em V(G) \ V(T)
        acrescente e a E(T)
        acrescente y a V(T)
    fim-para
    retorne T

    9 14 -> 9 nós e 14 arestas

    0 1 4
    0 7 8
    1 2 8
    1 7 11
    2 3 7
    2 5 4
    2 8 2
    3 4 9
    3 5 14
    4 5 10
    5 6 2
    6 7 1
    6 8 6
    7 8 7
'''


import heapq
import random

n, m = input().split()  # Ler número de vértices e arestas
n = int(n)
m = int(m)

H = []
n_out = [[]*n for i in range(n)]

for j in range(m):                 # Ler as m arestas do dígrafo
    a, b, c = input().split()      # Ler aresta de 'a' para 'b' com custo 'c'
    a = int(a)
    b = int(b)
    c = int(c)
    n_out[a].append((b,c))
    n_out[b].append((a,c))

raiz = random.randint(0,n-1)
for (x,c) in n_out[raiz]:
    heapq.heappush(H, (c, raiz, x))

n_edges = 0
custo_tot = 0
marcados = [raiz]
arv_ger_min = []

while n_edges < n-1:
    while True:
        (c, a, b) = heapq.heappop(H)
        if b not in marcados:
            break
    marcados.append(b)
    print(a, b)
    print(marcados)
    custo_tot += c
    arv_ger_min.append((a,b))
    n_edges += 1
    for (x,c) in n_out[b]:
        if x not in marcados:
            heapq.heappush(H, (c,b,x))


print(custo_tot)
print(arv_ger_min)


