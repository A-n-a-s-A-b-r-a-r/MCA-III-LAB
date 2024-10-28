import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generate random values for x
np.random.seed(42)  # For reproducibility
x = np.random.rand(1000)

# Generate k and calculate y
k = np.random.rand(1000)
y = 3 * x + k

# Prepare data for regression
X = x.reshape(-1, 1)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Check the score
score = model.score(X_test, y_test)
print(f"Linear Regression model R^2 score: {score:.4f}")
