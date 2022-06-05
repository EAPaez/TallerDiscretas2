import networkx as nx
import matplotlib.pyplot as plt
import spicy as spicy

# inicializar Grafo
grafo = nx.Graph()

# Convertir a Grafo indirecto
grafo = grafo.to_undirected()

# Parametros del grafo
grafo.add_nodes_from([1, 2, 3, 4, 5])
grafo.add_edges_from([(2, 3), (3, 4), (4, 1), (1, 5), (2,5 )])

# Dibujar el grafo
nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True)
plt.show()

# crear matriz dispersa
# print(nx.adjacency_matrix(grafo))

# crear Matriz de adyacencia
#print(nx.adjacency_matrix(grafo).todense())

# crear Matriz de incidencia
#print(nx.incidence_matrix(grafo).todense())

