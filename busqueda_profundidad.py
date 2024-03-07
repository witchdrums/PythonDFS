import random
import grafo

# Inicializar grafo de Romania:
GRAFO = grafo.get_grafo()

INDICE_FRONTERA = 1 # ciudad: [nombre de la ciudad : frontera] - La frontera siempre es el índice 1
INDICE_NOMBRE = 0 # el nombre de la ciudad siempre es el índice 0
ciudad_actual = list(GRAFO.items())[0]
ciudad_destino = list(GRAFO.items())[13]
ruta = []
ciudades_visitadas = []

def busqueda_profundidad(ultima_ciudad_visitada):

  nombre_ciudad_actual = ultima_ciudad_visitada[INDICE_NOMBRE]
  ciudades_visitadas.append(nombre_ciudad_actual)

  if nombre_ciudad_actual == ciudad_destino[INDICE_NOMBRE]:
    ruta.append(nombre_ciudad_actual)
    return
  
  # get_siguiente_ciudad regresa una ciudad con hojas nuevas; si no la encuentra, regresa None
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

    # repetir búsqueda con la nueva ciudad:
    busqueda_profundidad(siguiente_ciudad)

# regresa None si no hay una ciudad con hojas nuevas:
def get_siguiente_ciudad(ciudad_actual):
  frontera = ciudad_actual[INDICE_FRONTERA]
  nombre_siguiente_ciudad = ""
  nombre_siguiente_ciudad = get_siguiente_nombre_random(frontera)

  if (nombre_siguiente_ciudad == ""):
    return None
  else :
    siguiente_ciudad = get_ciudad(nombre_siguiente_ciudad)
    return siguiente_ciudad

# Regresa el nombre aleatorio de una hoja nueva; regresa "" si no hay hojas nuevas.
def get_siguiente_nombre_random(frontera):
  siguiente_nombre = ""
  while len(frontera) > 0:
    ciudad = frontera.pop(random.randint(0,len(frontera)-1)) 
    if not ciudad[INDICE_NOMBRE] in ciudades_visitadas:
      siguiente_nombre = ciudad[INDICE_NOMBRE]
      break
  return siguiente_nombre

def get_ciudad(nombre_ciudad):
  # al usar grafo.get("Arad"), recibimos la pura frontera: ["Zerind", "Sibiu", "Timisoara"]
  # pero requerimos que obtener nombre + frontera: ["Arad", ["Zerind", "Sibiu", "Timisoara"]]
  # El nombre es necesario para buscar a los otros nodos en el diccionario,
  # por lo que es necesario "reconstruir":
  frontera_ciudad = GRAFO.get(nombre_ciudad)
  return [nombre_ciudad, frontera_ciudad]

# se puede probar con otras ciudades:
ciudad_actual = get_ciudad("Rimnicu Vilcea")
ciudad_destino = get_ciudad("Bucarest")

busqueda_profundidad(ciudad_actual)
print("\nFINAL: " + ruta.__str__())
