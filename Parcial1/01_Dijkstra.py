

"""
Este programa te permitirá ingresar manualmente un grafo y un nodo de inicio, y 
luego calculará las distancias más cortas desde el nodo de inicio a todos los demás nodos. 
Puedes seguir el proceso paso a paso y ver los resultados en la consola.
El grafo representa una ciudad, y cada nodo un lugar turístico dentro de esta.
Puedes calcular la distancia más corta desde un nodo de inicio (que puedes elegir) a los
demás nodos. La vecindad entre grafos representa la distancia.

"""

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def build_graph():
    graph = {}
    num_nodes = int(input("Número de nodos: "))

    for i in range(num_nodes):
        graph[chr(65 + i)] = {}

    for node in graph:
        neighbors = input(f"Ingrese vecinos para {node} (Formato: B:2, C:5, ...): ").split(", ")
        for neighbor in neighbors:
            neighbor, weight = neighbor.split(":")
            graph[node][neighbor] = int(weight)

    return graph

def main():
    graph = build_graph()
    start_node = input("Nodo de inicio: ")

    shortest_distances = dijkstra(graph, start_node)
    print("\nDistancias más cortas desde el nodo de inicio (", start_node, "):")
    for node, distance in shortest_distances.items():
        print(node, ":", distance)

if __name__ == "__main__":
    main()
