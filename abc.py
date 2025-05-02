import numpy as np

# Activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (XOR logic gate)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Output dataset (XOR output)
y = np.array([[0], [1], [1], [0]])
 
np.random.seed(1)
input_layer_neurons = X.shape[1]
hidden_layer_neurons = 4
output_neurons = 1

weights_input_hidden = 2 * np.random.random((input_layer_neurons, hidden_layer_neurons)) - 1
weights_hidden_output = 2 * np.random.random((hidden_layer_neurons, output_neurons)) - 1

# loop
for epoch in range(10000):
    # Forward pass
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)

    final_input = np.dot(hidden_layer_output, weights_hidden_output)
    final_output = sigmoid(final_input)

    # Error
    error = y - final_output
    if epoch % 1000 == 0:
        print(f'Epoch {epoch} Error:\n', error)

    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)
    d_hidden_layer = d_output.dot(weights_hidden_output.T) * sigmoid_derivative(hidden_layer_output)

    # Update weights
    weights_hidden_output += hidden_layer_output.T.dot(d_output)
    weights_input_hidden += X.T.dot(d_hidden_layer)

# Final output
print("Trained output:")
print(final_output)

