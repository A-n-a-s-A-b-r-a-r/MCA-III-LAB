import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('Week-11/demo.csv')

# a. Clean independent features
# Assuming cleaning means filling NaN values
data.fillna(data.mean(), inplace=True)

# b. Add one more feature x7 having values between 0 and 1
data['x7'] = np.random.rand(len(data))

# c. Perform scaling
X = data.drop('y', axis=1)
y = data['y']

# Identify categorical columns for one-hot encoding
categorical_cols = ['x1', 'x2']  # Update with actual nominal columns
numerical_cols = X.columns.difference(categorical_cols)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

X_processed = preprocessor.fit_transform(X)

# d. Train dataset using Logistic Regression, Decision Tree, and Random Forest
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier()
}

results = {}

for model_name, model in models.items():
    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    results[model_name] = {'accuracy': accuracy, 'f1_score': f1, 'y_test': y_test, 'y_pred': y_pred}

    # e. Draw confusion matrix of each model
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['0', '1'], yticklabels=['0', '1'])
    plt.title(f'Confusion Matrix for {model_name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

# Compare performances
for model_name, metrics in results.items():
    print(f"{model_name} - Accuracy: {metrics['accuracy']:.2f}, F1 Score: {metrics['f1_score']:.2f}")
