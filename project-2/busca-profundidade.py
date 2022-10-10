# Representação de um Grafo em Lista Adjacente

adj_list = {
    "A":["B", "C"],
    "B":["D", "E"],
    "C":["B", "F"],
    "D":[],
    "E":["F"],
    "F":[],
}

color = {} # W -> white; G -> gray; B -> black
parent = {}
trav_time = {} # [start, end]
dfs_traversal_output = []

# Inicialização
for node in adj_list.keys():
    color[node] = 'W'
    parent[node] = None
    trav_time[node]= [0, 0]

print(color)
print(parent)
print(trav_time)
print()

time = 0
def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1

for u in adj_list.keys():
    if color[u] == "W":
        dfs_util("A")
print(dfs_traversal_output)
print(parent)
print(trav_time)
print()

for node in adj_list.keys():
    print(node, " ->", trav_time[node])

