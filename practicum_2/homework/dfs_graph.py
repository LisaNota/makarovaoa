from queue import LifoQueue
from typing import Any

import networkx as nx

from src.plotting import plot_graph


def visit(node: Any):
    print(f"Wow, it is {node} right here!")


def dfs_iterative(G: nx.Graph, node: Any):
    visited = {n: False for n in G}

    q = LifoQueue()
    q.put(node)

    while not q.empty():
        node = q.get()
        if not visited[node]:
            visit(node)
            visited[node] = True
            for neighbour in G.neighbors(node):
                q.put(neighbour)
    
def topological_sort(G: nx.DiGraph, node: Any):
    visited = {n: False for n in G}
    q = LifoQueue()

    def recursive_top_sort(node):
        visited[node] = True
        for neighbour in G.neighbors(node):
            if not visited[neighbour]:
                recursive_top_sort(neighbour)
        q.put(node)

    recursive_top_sort(node)
    while not q.empty():
        node = q.get()
        visit(node)

if __name__ == "__main__":
    # Load and plot the graph
    G = nx.read_edgelist("practicum_2/homework/graph_2.edgelist", create_using=nx.Graph)
    # plot_graph(G)

    print("Iterative DFS")
    print("-" * 32)
    dfs_iterative(G, node="0")
    print()

    G = nx.read_edgelist(
        "practicum_2/homework/graph_2.edgelist", create_using=nx.DiGraph
    )
    plot_graph(G)
    print("Topological sort")
    print("-" * 32)
    topological_sort(G, node="0")
