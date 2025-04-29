import numpy as np

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def train_mlp(inputs, outputs, input_size, hidden_size1, hidden_size2, output_size, learning_rate=0.1, epochs=10000):
    np.random.seed(1)

    w1 = np.random.randn(input_size, hidden_size1)
    b1 = np.random.randn(hidden_size1)
    w2 = np.random.randn(hidden_size1, hidden_size2)
    b2 = np.random.randn(hidden_size2)
    w3 = np.random.randn(hidden_size2, output_size)
    b3 = np.random.randn(output_size)

    for epoch in range(epochs):
        # Forward pass
        z1 = np.dot(inputs, w1) + b1
        a1 = relu(z1)

        z2 = np.dot(a1, w2) + b2
        a2 = relu(z2)

        z3 = np.dot(a2, w3) + b3
        output = relu(z3)

        error = outputs - output
        if (epoch + 1) % 1000 == 0:
            print(f"Epoch {epoch + 1}, Error: {np.mean(np.abs(error))}")

        # Backpropagation
        output_delta = error * relu_derivative(output)
        a2_delta = output_delta.dot(w3.T) * relu_derivative(a2)
        a1_delta = a2_delta.dot(w2.T) * relu_derivative(a1)

        w3 += a2.T.dot(output_delta) * learning_rate
        b3 += np.sum(output_delta, axis=0) * learning_rate
        w2 += a1.T.dot(a2_delta) * learning_rate
        b2 += np.sum(a2_delta, axis=0) * learning_rate
        w1 += inputs.T.dot(a1_delta) * learning_rate
        b1 += np.sum(a1_delta, axis=0) * learning_rate

    print("\nFinal weights and biases:")
    print("Weights between input and first hidden layer (w1):\n", w1)
    print("Biases of first hidden layer (b1):\n", b1)
    print("Weights between first hidden and second hidden layer (w2):\n", w2)
    print("Biases of second hidden layer (b2):\n", b2)
    print("Weights between second hidden layer and output layer (w3):\n", w3)
    print("Biases of output layer (b3):\n", b3)

    print("\nTraining complete.")

if __name__ == "__main__":
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) 
    outputs = np.array([[0], [1], [1], [0]])

    input_size = inputs.shape[1]
    hidden_size1 = 4
    hidden_size2 = 4
    output_size = outputs.shape[1]

    # Train the MLP
    train_mlp(inputs, outputs, input_size, hidden_size1, hidden_size2, output_size)