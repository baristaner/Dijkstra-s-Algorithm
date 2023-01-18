import heapq
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

def dijkstra(graph, start):
    # initialize distances dictionary, with the start node having distance 0
    distances = {start: 0}
    # initialize priority queue with the start node
    queue = [(0, start)]
    # initialize previous dictionary
    previous = {}
    while queue:
        # dequeue the node with the smallest distance
        current_distance, current_node = heapq.heappop(queue)
        if current_node in distances:
            # we've already processed this node
            continue
        # mark the current node as processed
        distances[current_node] = current_distance
        # update the distances of its neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                previous[neighbor] = current_node
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return previous, distances


# Example usage:
graph = {
    'A': {'B': 2, 'C': 3, 'D': 4},
    'B': {'A': 2, 'D': 6, 'E': 5},
    'C': {'A': 3, 'D': 4, 'F': 2, 'G': 3},
    'D': {'A': 4, 'B': 6, 'C': 4, 'E': 2, 'F': 5},
    'E': {'B': 5, 'D': 2, 'G': 3},
    'F': {'C': 2, 'D': 5, 'H': 4},
    'G': {'C': 3, 'E': 3, 'H': 5},
    'H': {'F': 4, 'G': 5},
}



# create an empty directed graph
G = nx.DiGraph()

# add edges and weights to the graph
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)

# set the layout for the nodes
pos = nx.spring_layout(G)

def run_dijkstra():
    destination = destination_var.get()
    start = start_var.get()
    previous, distances = dijkstra(graph, start)
    path = nx.dijkstra_path(G, start, destination)
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)
    plt.show()

    

root = tk.Tk()
root.title("Dijkstra's Algorithm")
root.geometry("150x120")

label = tk.Label(root, text="Select starting point:")
label.grid(column=0, row=0)

start_var = tk.StringVar()
start_combobox = ttk.Combobox(root, textvariable=start_var)
start_combobox["values"] = list(graph.keys())
start_combobox.current(0)
start_combobox.grid(column=0, row=1)


label = tk.Label(root, text="Select a destination node:")
label.grid(column=0, row=2)

destination_var = tk.StringVar()
destination_combobox = ttk.Combobox(root, textvariable=destination_var)
destination_combobox["values"] = list(graph.keys())
destination_combobox.current(0)
destination_combobox.grid(column=0, row=3)


run_button = tk.Button(root, text="Run", command=run_dijkstra)
run_button.grid(column=0, row=4)

# Draw the graph
nx.draw(G, pos, with_labels=True)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
root.mainloop()