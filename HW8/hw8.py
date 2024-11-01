import matplotlib.pyplot as plt
import networkx as nx

# Create a graph object
graph = nx.Graph()

# Add nodes and edges (replace with your actual data)
graph.add_edge("A", "B", weight=1)
graph.add_edge("B", "C", weight=2)
graph.add_edge("A", "C", weight=3)
graph.add_edge("C", "D", weight=4)


# Calculate shortest path between two nodes
shortest_path = nx.shortest_path(graph, source="A", target="D", weight="weight")
print("Shortest path:", shortest_path)


# Calculate the shortest path lengths from one node to all other nodes
shortest_path_lengths = nx.shortest_path_length(graph, source="A", weight="weight")
print("Shortest path lengths from A:", shortest_path_lengths)

# Example of visualizing the graph
nx.draw(graph, with_labels=True)
plt.show()