import random

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


# pintar_grafo()
    # Reminder: the second element of each list inside the dictionary
    # denotes the edge weight.
# print ("Internal representation: ", grafo)

########### VALIDAR REPETIDOS
# lista = [1, 2, 3]
# print(lista.__contains__(4))

########### ALGORITMO:

# ARAD es BUCAREST? No                          <--- programa recibe nodo de ARAD primero
# Push ARAD a Queue -> [ARAD]                   <--- se pushea el NODO, no el nombre solito
# Obten frontera -> [ZERIND, SIBIU, TIMISOARA]
# Obten hoja 1 (ZERIND)
# ZERIND en Queue? No

# ZERIND es BUCAREST? No
# Push ZERIND a Queue -> [ARAD, ZERIND]
# Obten frontera [ARAD, ORADEA]
# Obten hoja 1 [ARAD]                           <--- while?
# ARAD en Queue? Sí
# Obten hoja 2 [ORADEA]
# ORADEA en Queue? No

# ORADEA es BUCAREST? No
# Obten ORADEA.frontera [ZERIND, SIBIU]
# Obten hoja 1 (ZERIND)

# Obtener frontera
# print(grafo.get("Arad"))

# Obtener primera HOJA ( ["Zerind", 75] ):
# print(grafo.get("Arad")[0])

# Obtener NOMBRE de hoja ("Zerind"):
# print(grafo.get("Arad")[0][0])

INDICE_FRONTERA = 1 # ciudad: [nombre de la ciudad : frontera] - La frontera siempre es el índice 1
INDICE_NOMBRE = 0 # el nombre de la ciudad siempre es el índice 0
ciudad_actual = list(grafo.items())[0]
ciudad_destino = list(grafo.items())[13]
ruta = []
ciudades_visitadas = []

def busqueda_profundidad(ultima_ciudad_visitada):
  nombre_ciudad_actual = ultima_ciudad_visitada[INDICE_NOMBRE]
  ciudades_visitadas.append(nombre_ciudad_actual)
  if nombre_ciudad_actual == ciudad_destino[INDICE_NOMBRE]:
    ruta.append(nombre_ciudad_actual)
    return
  
  siguiente_ciudad = get_siguiente_ciudad(ultima_ciudad_visitada)
  if siguiente_ciudad == None:
    print("ERROR:" + ruta.__str__())
    
    # podar ciudad sin hojas:
    ruta.pop()

    # regresar a la última ciudad:
    nombre_ultima_ciudad_visitada = ruta[-1]
    ultima_ciudad_visitada = get_ciudad(nombre_ultima_ciudad_visitada)

    # repetir búsqueda con la última ciudad visitada, a ver si tiene hojas nuevas.
    busqueda_profundidad(ultima_ciudad_visitada)

  else:
    # si podamos, ya no hay que agregar la ciudad actual a la ruta:
    if nombre_ciudad_actual not in ruta:
      ruta.append(nombre_ciudad_actual)

    busqueda_profundidad(siguiente_ciudad)

# regresa None si no hay una ciudad con hojas nuevas:
def get_siguiente_ciudad(ciudad_actual):
  frontera = ciudad_actual[INDICE_FRONTERA]
  nombre_siguiente_ciudad = ""
  nombre_siguiente_ciudad = get_siguiente_nombre_random(frontera)

  # si la ciudad elegida no tiene hojas nuevas:
  if (nombre_siguiente_ciudad == ""):
    return None
  else :
    siguiente_ciudad = get_ciudad(nombre_siguiente_ciudad)
    return siguiente_ciudad

# regresa "" si la frontera no tiene una hoja que no haya sido visitada:
def get_siguiente_nombre(FRONTERA):
  for ciudad in FRONTERA:
    if not ciudad[INDICE_NOMBRE] in ciudades_visitadas:
      ciudades_visitadas.append(ciudad[INDICE_NOMBRE])
      return ciudad[INDICE_NOMBRE]
  
# igual al anterior pero random, para probar distintos escenarios de ruteo:
def get_siguiente_nombre_random(frontera):
  siguiente_nombre = ""
  while len(frontera) > 0:
    ciudad = frontera.pop(random.randint(0,len(frontera)-1)) 
    if not ciudad[INDICE_NOMBRE] in ciudades_visitadas:
      siguiente_nombre = ciudad[INDICE_NOMBRE]
      break
  return siguiente_nombre

def get_ciudad(nombre_ciudad):
  # el diccionario regresa la frontera del siguiente nodo SIN su nombre, 
  # el cual es necesario para buscar a los otros nodos en el diccionario,
  # por lo que es necesario "reconstruir" el siguiente nodo:
  frontera_ciudad = grafo.get(nombre_ciudad)
  return [nombre_ciudad, frontera_ciudad]

ciudad_actual = get_ciudad("Arad")
ciudad_destino = get_ciudad("Bucarest")

busqueda_profundidad(ciudad_actual)
print("\nFINAL: " + ruta.__str__())
