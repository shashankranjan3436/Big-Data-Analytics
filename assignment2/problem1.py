import findspark
import matplotlib.pyplot as plt
findspark.init() 

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Creating a Spark configuration
conf = SparkConf().setAppName("PageRankSpark")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

# Load the dataset
data_path = " https://snap.stanford.edu/data/web-Google.html"  
lines = sc.textFile(data_path)

# Parse the data and prepare edges
edges = lines.filter(lambda line: not line.startswith("#")).map(lambda line: tuple(map(int, line.strip().split("\t"))))
links = edges.groupByKey().cache()

# Initializing ranks
ranks = links.mapValues(lambda _: 1.0)

# Performing 10 (or accordingly) iterations of PageRank algorithm
iterations = 10
for _ in range(iterations):
    contribs = links.join(ranks).flatMap(
        lambda url_rank_links: [(dest, url_rank_links[1][1] / len(url_rank_links[1][0])) for dest in url_rank_links[1][0]]
    )
    ranks = contribs.reduceByKey(lambda x, y: x + y).mapValues(lambda rank: rank * 0.85 + 0.15)

# Collecting the results
result = ranks.collect()

# Printing the PageRank for each node
for (node, rank) in result:
    print(f"Node: {node}, Rank: {rank}")

# Close the Spark context
sc.stop()

# Extract the ranks and create a list
rank_values = [rank for (_, rank) in result]

# Plot the distribution of ranking scores
plt.hist(rank_values, bins=20, edgecolor="black")
plt.xlabel("PageRank Score")
plt.ylabel("Frequency")
plt.title("Distribution of PageRank Scores")
plt.show()