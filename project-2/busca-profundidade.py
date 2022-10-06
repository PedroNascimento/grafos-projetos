grafo = [ [1]
          [2,3],
          [1,4],
          [0],
          [1]
          ]

def dfs(grafo):
    def dfs_recursiva(grafo, vertice, visitados):
        visitados.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs_recursiva(grafo, vizinho)

    visitados = set()
    for vertice in grafo:
        if not vertice in visitados:
            dfs_recursiva(grafo, vertice)

