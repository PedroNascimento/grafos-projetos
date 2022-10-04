class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        # Caso sejam grafo direcionais simples
        self.grafo[u-1][v-1] = 1 # caso seja grafo múltiplo, trocar = por +=

        # Caso seja um grafo não direcionado, usar lógica abaixo
        # self.grafo[v-1][u-1] = 1

    def mostra_matriz(self):
        print('A Matriz de Adjacência é: ')
        for i in range(self.vertices):
            print(self.grafo[i])

g = Grafo(4)

g.adiciona_aresta(1,2)
#g.adiciona_aresta(2,1)
g.adiciona_aresta(3,4)
g.adiciona_aresta(2,3)

g.mostra_matriz()