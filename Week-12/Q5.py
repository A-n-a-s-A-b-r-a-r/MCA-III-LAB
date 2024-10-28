import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Generate random values for x1 and x2
np.random.seed(42)  # For reproducibility
x1 = np.random.rand(1000)
x2 = np.random.rand(1000)

# Generate c based on 1000 random values between 0 and 1
c = np.random.rand(1000)

# Calculate y based on the given function
y = x1**12 + 3*x2**2 + c

# Create a DataFrame for features
X = pd.DataFrame({'x1': x1, 'x2': x2})

# Polynomial regression
poly = PolynomialFeatures(degree=12)  # Adjust degree as necessary
X_poly = poly.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions and scoring
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)

print(f"R^2 score of the Polynomial Regression model: {score:.4f}")
