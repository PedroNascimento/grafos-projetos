# class Grafo(object):
#     """
#         Classe base para as classes GrafoListaAdj e GrafoMatrizAdj
#     """
#     def __init__(self, orientado =False):
#         """
#             Grafo se orientado=False ou Dígrafo se orientado=True
#         """
#         self.n, self.m, sefl.orientado = None, None, orientado
#
#     def DefinirN(self, n):
#         # Defifir o número n de vértices.
#         self.n, self.m = n, 0
#
#     def V(self):
#         # Retorna a lista de vértices.
#         for i in range (1, self.n+1):
#             yiedl i
#
#     def E(self, IterarSobreNo=False):
#         """
#             Retorna lista de arestas uv, onde u é um inteiro e v é um
#             inteiro se o grafo é GrafoMatrizAdj
#
#             ou IterarSobreNo=False; v é GrafoListaAdj.NoAresta, caso
#             contrário.
#         """
#         for v in self.V():
#             for w in self.N(v, Tipo = "+" if self.orientado else "*"), IterarSobreNo = IterarSobreNo):
#                 enumerar = True