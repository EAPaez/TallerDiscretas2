
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# inicializar Grafo
grafo = nx.Graph()


def creacionGrafo():
    # Entrada de datos
    text = open("input_Punto2.txt")
    mensaje = text.readline().split()
    vertices = int(mensaje[0])


    # Se añaden los nodos
    for n in range(vertices):
        vertice = str(n+1)
        grafo.add_node(vertice)


    # Se añaden las aristas
    for linea in (text):
        fila = linea.split()
        u = str(fila[0])
        v = str(fila[1])
        grafo.add_edge(u, v)

     nx.draw(grafo, with_labels=True, font_weight="bold")
     plt.axis("equal")