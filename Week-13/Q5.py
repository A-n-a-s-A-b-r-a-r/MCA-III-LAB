import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess data: Flatten and normalize
x_train = x_train.reshape(-1, 28*28).astype('float32') / 255
x_test = x_test.reshape(-1, 28*28).astype('float32') / 255

# Create binary labels for digit 8
y_train_binary = (y_train == 8).astype(int)
y_test_binary = (y_test == 8).astype(int)

# Convert labels to categorical
y_train_binary = to_categorical(y_train_binary)
y_test_binary = to_categorical(y_test_binary)

# Build the model
model = Sequential([
    Flatten(input_shape=(28*28,)),
    Dense(128, activation='relu'),
    Dense(2, activation='softmax')  # Output for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train_binary, epochs=10, batch_size=32, validation_split=0.1)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test_binary)
print(f"Test Accuracy: {accuracy:.4f}")

# Performance discussion
# The model's accuracy will indicate how well it classifies images of digit 8. 
# Consider metrics like precision, recall, and F1 score for a deeper understanding.
