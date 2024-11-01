import networkx as nx
import matplotlib.pyplot as plt

#initiate graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(range(1, 11))

# Add edges
edges = [
    (1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
    (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6), (5, 7), (6, 7),
    (6, 8), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9), (8, 9),
    (8, 10), (9, 10)
]

G.add_edges_from(edges)


# Draw the graph
nx.draw(G, with_labels=True, node_color="lightblue", node_size=500, font_size=16)
plt.show()


#Function to return the number of nodes
def count_nodes(graph):
    # Get all nodes in the graph and count them
    return graph.number_of_nodes()

print("Graph G has " + str(count_nodes(G)) + " nodes")
