
from collections import defaultdict

# Classe para criação do grafo direcionado e que usa representação de lista de adjacência
class Graph:
    # Função para contruir a lista
    def __init__(self):
        self.graph = defaultdict(list)

    # Função que irá adicionar os vértices no grafo
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Função para imprimir a BFS do grafo, recebe o primeiro nó a ser visitado
    def BFS(self, s):

        # Marca todos os vértices como não visitados.
        visited = [False] * (len(self.graph))

        # Cria uma fila vazia para o BFS
        queue = []

        # Pegar o nó de origem, marcar como visitado e inserir ele na fila
        queue.append(s)
        visited[s] = True

        # Será executado enquanto a fila não for vazia
        while queue:
            # Retira o último vértice inserido na fila e imprime
            s = queue.pop(0)
            print(s, " ")

            """
                Obter todos os vértices adjacentes dos vértices desenfileirados.
                Se um adjacente não foi visitado, será marcado como visitado e
                colocado na fila        
            """

            for i in self.graph[s]:
                print(visited[i])
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    # Criação do grafo
g = Graph()
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(0, 4)
g.addEdge(1, 4)
g.addEdge(2, 4)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(5, 1)

vertice = int(input("A execução do BFS deve iniciar de qual vértice? "))
g.BFS(vertice)



