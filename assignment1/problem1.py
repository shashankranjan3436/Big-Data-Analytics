"""
Created on Fri Aug 14 19:56:02 2023

@author: SK RANJAN
"""
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
# READ PAGERANK SCORES THROUGH HADOOP
data = "https://snap.stanford.edu/data/web-Google.txt"
def read_scores(data):
    scores = {}
    with open(data, 'r') as file:
        for line in file:
            node, score, _ = line.strip().split('\t')
            scores[node] = float(score)
    return scores

# GENERATING AND PLOTTING THE GRAPH
def generate_graph(scores):
    G = nx.DiGraph()

    for node in scores:
        G.add_node(node, score=scores[node])

    for node in scores:
        neighbors = adjacency_lists.get(node, [])
        for neighbor in neighbors:
            G.add_edge(neighbor, node)  # REVERSING EDGE FOR BETTER VISUALIZATION

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, node_size=200, node_color=[scores[n] for n in G.nodes()], cmap='viridis', edge_color='gray')
    plt.title('PageRank Visualization')
    plt.colorbar(label='PageRank Score')
    plt.show()

if __name__ == '__main__':
    iteration = 10 
    scores = read_scores(f'output/iteration_{iteration}/part-00000')
    adjacency_lists = {}  
    
    generate_graph(scores)
    

