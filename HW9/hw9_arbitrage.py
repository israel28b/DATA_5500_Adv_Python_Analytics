import requests
from itertools import permutations

import networkx as nx


# Create dictionary to store the selected 7 cryptocurrencies and their ticker symbols
currencies = {
    'ripple': 'xrp',
    'cardano': 'ada',
    'bitcoin-cash': 'bch',
    'eos': 'eos',
    'litecoin': 'ltc',
    'ethereum': 'eth',
    'bitcoin': 'btc'
}



# Create the directed graph
g = nx.DiGraph()

# Construct the API URL to get exchange rates for all currency pairs
url1 = "https://api.coingecko.com/api/v3/simple/price?ids="
url2 = "&vs_currencies="
ids = ','.join(currencies.values())
vs_currencies = ','.join(currencies.values())
url = f"{url1}{ids}{url2}{vs_currencies}"

# Retrieve exchange rates from the coingecko API and add edges to the graph
try:
    req = requests.get(url)
    req.raise_for_status()
    data = req.json()

    # Add weighted edges to the graph for each currency pair
    #The change is in this loop:
    for c1, c2 in permutations(currencies.keys(), 2):
        if currencies[c2] in data.get(currencies[c1], {}):
            rate = data[currencies[c1]][currencies[c2]]
            # Adding both forward and reverse edges with their respective rates:
            g.add_edge(currencies[c1], currencies[c2], weight=rate)  
            g.add_edge(currencies[c2], currencies[c1], weight=1/rate) # Adding reverse edge


# Error handling in case issues arise with retriving data
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except KeyError as e:
    print(f"KeyError: {e}")
except Exception as e:
    print(f"Error: {e}")


# Function to calculate the weight of a path by multiplying all edge weights
def calculate_path_weight(path, graph):
    weight = 1.0
    for i in range(len(path) - 1):
        weight *= graph[path[i]][path[i + 1]]['weight']
    return weight

# Variables to store maximum and minimum path weight factors
max_path_factor = float('-inf')
min_path_factor = float('inf')
max_path_info = None
min_path_info = None

# Find arbitrage opportunities by checking all paths from each currency to each other currency
for n1, n2 in permutations(g.nodes, 2):
    print(f"Paths from {n1} to {n2} ----------------------------------")
    
    # Find all simple paths from n1 to n2
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        forward_weight = calculate_path_weight(path, g)
        print(f"Path {path} Weight: {forward_weight}")

        # Find the reverse path and calculate its weight
        reverse_path = path[::-1]
        reverse_weight = calculate_path_weight(reverse_path, g)
        print(f"Reverse Path {reverse_path} Weight: {reverse_weight}")

        # Calculate the arbitrage by multiplying forward and reverse weights
        path_factor = forward_weight * reverse_weight
        print(f"Path Factor (forward * reverse): {path_factor}\n")

        # Check if this path factor is a new max or min
        if path_factor > max_path_factor:
            max_path_factor = path_factor
            max_path_info = (path, reverse_path, forward_weight, reverse_weight, path_factor)
        
        if path_factor < min_path_factor:
            min_path_factor = path_factor
            min_path_info = (path, reverse_path, forward_weight, reverse_weight, path_factor)

# Display results
print("\nHighest Path Factor:")
print(f"Path: {max_path_info[0]} | Reverse Path: {max_path_info[1]}")
print(f"Forward Weight: {max_path_info[2]}, Reverse Weight: {max_path_info[3]}")
print(f"Factor: {max_path_info[4]}")

print("\nLowest Path Factor:")
print(f"Path: {min_path_info[0]} | Reverse Path: {min_path_info[1]}")
print(f"Forward Weight: {min_path_info[2]}, Reverse Weight: {min_path_info[3]}")
print(f"Factor: {min_path_info[4]}")