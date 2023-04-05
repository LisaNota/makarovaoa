from typing import Any

import networkx as nx
from queue import PriorityQueue
import numpy as np

from src.plotting import plot_graph


def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = {}  # key = destination node, value = list of intermediate nodes
    shortest_paths[source_node] = [source_node]

    q = PriorityQueue()
    q.put((0, source_node))

    visited = []
    distance = {n: np.inf for n in G.nodes}
    distance[source_node] = 0
    
    while not q.empty():
        dist, node = q.get()
        if node not in visited:
            visited.append(node)
        for neighbour in G.neighbors(node):
            if neighbour not in visited: 
                newdist = dist + G.edges[neighbour, node]['weight']
                if newdist < distance[neighbour]:
                    distance[neighbour] = newdist
                    shortest_paths[neighbour] = [neighbour] + shortest_paths[node]
                    q.put((distance[neighbour], neighbour))

    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
