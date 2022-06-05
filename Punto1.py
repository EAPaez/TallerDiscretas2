
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def creacionGrafo():
    # Entrada de datos
    text = open("input_Punto1.txt")
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


def matrizToList(lista):
    dicci.clear()
    for i in range(len(lista)):
        dicci[i+1] = []
        for j in range(len(lista)):
            if(lista[i][j] == 1):
                dato = j
                dicci[i+1].append(dato+1)


def dfs(visitado, dicci, nodo):

    if nodo not in visitado:
        resultado.append(nodo)
        visitado.add(nodo)
        for vecino in dicci[nodo]:
            dfs(visitado, dicci, vecino)



grafo = nx.Graph()  # Se crea el grafo
nodos = []
creacionGrafo()  # Metodo con el que se crea el grafo
matriz = nx.adjacency_matrix(grafo).todense()  # Toma la matriz de adyacencia
lista = matriz.tolist()  # Convierte la matriz de adyacencia en una lista
dicci = dict()  # Diccionario creado para crear la lista de adyacencia
matrizToList(lista)  # Metodo con el que se pasa la matriz a una lista
visitado = set()
resultado = []
dfs(visitado, dicci, 1)  # Metodo para realizar la busqueda por profundidad


# print(matriz) # Con este print se puede visualizar la matriz de adyacencia
# print(lista)  # Con este print se puede visualizar la matriz de adyacencia en formato lista
# print(dicci)  # Con este print se puede visualizar la lista de adyacencia
# print(grafo.nodes) # Con este print se puede visualizar todos los nodos
# print(grafo.edges) # Con este print se puede visualizar la conexion que existe entre los nodos
# plt.show()         # Con esta funcion se visualiza graficamente el grafo
print()
print('______________________   Punto 1   ____________________________________')
print()
print('-Nodos:', len(grafo.nodes))
print('-Aristas:', len(grafo.edges))
print("-El recorrido lexicográficamente menor es:", resultado)
print()
print('_______________________________________________________________________')

