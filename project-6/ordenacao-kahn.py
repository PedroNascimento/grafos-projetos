from collections import deque


# Uma classe para representar um objeto gráfico
class Graph:
    # armazena em grau de um vértice
    indegree = None

    # Construtor
    def __init__(self, edges, n):
        # Uma lista de listas para representar uma lista de adjacências
        self.adjList = [[] for _ in range(n)]

        # inicializa em grau de cada vértice por 0
        self.indegree = [0] * n

        # adiciona arestas ao grafo direcionado
        for (src, dest) in edges:
            # adiciona uma borda da origem ao destino
            self.adjList[src].append(dest)

            # incrementa o grau do vértice de destino em 1
            self.indegree[dest] = self.indegree[dest] + 1


# Função para realizar uma classificação topológica em um determinado DAG
def doTopologicalSort(graph, n):
    # Lista # para armazenar os elementos ordenados
    L = []

    # obtém informações em grau do gráfico
    indegree = graph.indegree

    # Conjunto de todos os nós sem bordas de entrada
    S = deque([i for i in range(n) if indegree[i] == 0])

    while S:

        # remove o nó `n` de `S`
        n = S.pop()

        # adiciona `n` na cauda de `L`
        L.append(n)

        for m in graph.adjList[n]:

            # remove uma aresta de `n` a `m` do gráfico
            indegree[m] = indegree[m] - 1

            # se `m` não tiver outras arestas de entrada, insira `m` em `S`
            if indegree[m] == 0:
                S.append(m)

    # se um grafo tem arestas, então o grafo tem pelo menos um ciclo
    for i in range(n):
        if indegree[i]:
            return None

    return L


if __name__ == '__main__':

    # Lista de arestas do gráfico conforme o diagrama acima
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]

    # número total de nós no gráfico (rotulado de 0 a 7)
    n = 8

    # constrói um gráfico a partir das arestas dadas
    graph = Graph(edges, n)

    # Executar classificação topológica
    L = doTopologicalSort(graph, n)

    if L:
        print(L)  # imprimir ordem topológica
    else:
        print('Graph has at least one cycle. Topological sorting is not possible.')