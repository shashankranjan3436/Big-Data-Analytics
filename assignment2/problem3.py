from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TrivagoRanking").getOrCreate()

data_path = "D:\web-Google.txt" 
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Select relevant columns from data
selected_cols = ["FromNodeId", "ToNodeId"]
df_selected = df.select(selected_cols)

from pyspark.sql.functions import col

# Define weights for different criteria
w_fromNodeId = 0.4
w_toNodeId = 0.3

# Calculating the ranking score
df_ranked = df_selected.withColumn(
    "rank",
    w_fromNodeId * col("Frome_Node_ID") +
    w_toNodeId * col("To_Node_ID")
)

# Ordering the DataFrame by rank in descending order
df_ranked = df_ranked.orderBy(col("rank").desc())

# Shows the top ranked entries
df_ranked.show()

spark.stop()