"""
Created on Fri Aug 16 03:47:32 2023

@author: SK RANJAN
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC  # You can use a different model here

# Loading and preprocessing the dataset
data = pd.read_csv("C:/Users/SK RANJAN/Downloads/train.csv")
X = data[['action_type', 'platform', 'city']]
y = data['reference'] 

# Normalizing numerical features
scaler = StandardScaler()
X['city'] = scaler.fit_transform(X['city'].values.reshape(-1, 1))

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training a ranking model 
model = SVC()  # Use a different ranking model
model.fit(X_train, y_train)

# Evaluate the model
# ...

# Rank hotels using the trained model
hotel_rankings = model.predict(X)  # Use the entire dataset for ranking

# Display hotel rankings
sorted_hotels = sorted(zip(hotel_rankings, data['Trivago']), reverse=True)
for rank, hotel_name in sorted_hotels:
    print(f"Rank {rank}: {Trivago}")
