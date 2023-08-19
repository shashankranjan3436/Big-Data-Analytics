"""
Created on Fri Aug 15 15:03:51 2023

@author: SK RANJAN
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# LOAD THE DATASET AND CREATE THE GRAPH
data = "https://snap.stanford.edu/data/web-Google.txt"
G = nx.read_edgelist(data, create_using=nx.DiGraph)

# CALCULATE PAGERANK USING NETWORKX
individual_pagerank = nx.pagerank(G, alpha=0.85)

# PLOT THE DISRTIBUTION OF RANKING SCORES
plt.hist(list(individual_pagerank.values()), bins=50, alpha=0.7, color='b')
plt.xlabel('Ranking Score')
plt.ylabel('Number of Nodes')
plt.title('Distribution of Personalized PageRank Scores')
plt.show()

# IDENTIFY NODES WITH SIMILAR NODE
Similar_score_node = [node for node, score in individual_pagerank.items() if 0.1 <= score <= 0.2]

# PRINT SIMILAR SCORE NODES AND THE SCORES
print("Nodes with Similar Scores:")
for node in Similar_score_node:
    print(f"Node {node}: Personalized PageRank Score = {individual_pagerank[node]:.4f}")
