from typing import Any

import matplotlib.pyplot as plt
import networkx as nx

from src.plotting import plot_graph
from queue import PriorityQueue


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # set of nodes included into MST
    rest_set = set(G.nodes())  # set of nodes not yet included into MST
    mst_edges = set()  # set of edges constituting MST

    q = PriorityQueue()

    mst_set.add(start_node)
    rest_set.remove(start_node)

    for neighbour in G.neighbors(start_node):
        q.put((G.edges[(start_node, neighbour)]['weight'], (start_node, neighbour)))

    while len(rest_set) > 0:
        v, edge = q.get()
        v = edge[1]
        
        if v not in mst_set:
            mst_edges.add(edge)
            mst_set.add(v)
            rest_set.remove(v)

            for neighbour in G.neighbors(v):
                if neighbour in rest_set:
                    q.put((G.edges[(v, neighbour)]['weight'], (v, neighbour)))

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
