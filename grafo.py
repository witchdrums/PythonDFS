# Add a vertex to the dictionary
def agregar_nodo(nodo):
  global grafo
  global num_nodos
  if nodo in grafo:
    print("Nodo ", nodo, " ya existe.")
  else:
    num_nodos = num_nodos + 1
    grafo[nodo] = []

def unir_nodos(nodo1, nodo2, costo):
  global grafo
  if nodo1 not in grafo:
    print("Nodo ", nodo1, " no existe.")
  elif nodo2 not in grafo:
    print("Nodo ", nodo2, " no existe.")
  else:
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    camino = [nodo2, costo]
    grafo[nodo1].append(camino)

# Print the graph
def pintar_grafo():
  global grafo
  for nodo in grafo:
    for aristas in grafo[nodo]:
      print(nodo, "   ->   ", aristas[0], " |   Costo: ", aristas[1])

# driver code
grafo = {}
# stores the number of vertices in the graph
num_nodos = 0
agregar_nodo("Arad")
agregar_nodo("Zerind")
agregar_nodo("Oradea")
agregar_nodo("Timisoara")
agregar_nodo("Sibiu")
agregar_nodo("Lugoj")
agregar_nodo("Rimnicu Vilcea")
agregar_nodo("Fagaras")
agregar_nodo("Mehadia")
agregar_nodo("Dobreta")
agregar_nodo("Craiova")
agregar_nodo("Pitesti")
agregar_nodo("Giurgiu")
agregar_nodo("Bucarest")
agregar_nodo("Urziceni")
agregar_nodo("Hirsova")
agregar_nodo("Eforie")
agregar_nodo("Vaslui")
agregar_nodo("Iasi")
agregar_nodo("Neamt")

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
unir_nodos("Arad", "Zerind", 75)
unir_nodos("Arad", "Sibiu", 140)
unir_nodos("Arad", "Timisoara", 118)
unir_nodos("Zerind", "Arad", 75)
unir_nodos("Zerind", "Oradea", 71)
unir_nodos("Oradea", "Zerind", 71)
unir_nodos("Oradea", "Sibiu", 151)
unir_nodos("Timisoara", "Arad", 118)
unir_nodos("Timisoara", "Lugoj", 111)
unir_nodos("Sibiu", "Oradea", 151)
unir_nodos("Sibiu", "Arad", 140)
unir_nodos("Sibiu", "Fagaras", 99)
unir_nodos("Sibiu", "Rimnicu Vilcea", 80)
unir_nodos("Lugoj", "Timisoara", 111)
unir_nodos("Lugoj", "Mehadia", 70)
unir_nodos("Rimnicu Vilcea", "Sibiu", 80) 
unir_nodos("Rimnicu Vilcea", "Pitesti", 97) 
unir_nodos("Rimnicu Vilcea", "Craiova", 146) 
unir_nodos("Fagaras", "Sibiu", 99)
unir_nodos("Fagaras", "Bucarest", 211)
unir_nodos("Mehadia", "Lugoj", 70)
unir_nodos("Mehadia", "Dobreta", 75)
unir_nodos("Dobreta", "Mehadia", 75)
unir_nodos("Dobreta", "Craiova", 120)
unir_nodos("Craiova", "Dobreta", 120)
unir_nodos("Craiova", "Rimnicu Vilcea", 146)
unir_nodos("Craiova", "Pitesti", 138)
unir_nodos("Pitesti", "Craiova", 138)
unir_nodos("Pitesti", "Rimnicu Vilcea", 97)
unir_nodos("Pitesti", "Bucarest", 101)
unir_nodos("Bucarest", "Pitesti", 101)
unir_nodos("Bucarest", "Fagaras", 211)
unir_nodos("Bucarest", "Urziceni", 85)
unir_nodos("Bucarest", "Giurgiu", 90)
unir_nodos("Giurgiu", "Bucarest", 90)
unir_nodos("Urziceni", "Bucarest", 85)
unir_nodos("Urziceni", "Vaslui", 142)
unir_nodos("Urziceni", "Hirsova", 98)
unir_nodos("Hirsova", "Urziceni", 98)
unir_nodos("Hirsova", "Eforie", 86)
unir_nodos("Eforie", "Hirsova", 86)
unir_nodos("Vaslui", "Urziceni", 142)
unir_nodos("Vaslui", "Iasi", 92)
unir_nodos("Iasi", "Vaslui", 92)
unir_nodos("Iasi", "Neamt", 87)
unir_nodos("Neamt", "Iasi", 87)

def get_grafo():
  return grafo