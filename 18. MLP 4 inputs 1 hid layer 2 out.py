import numpy as np

def step(x):
    return 1 if x > 0 else 0

def train_mlp(inputs, outputs, input_size, hidden_size1, output_size, learning_rate=0.1, epochs=10000):
    np.random.seed(1)

    for epoch in range(epochs):
        # Forward pass
        w1 = np.random.randn(input_size, hidden_size1)
        b1 = np.random.randn(hidden_size1)
        w2 = np.random.randn(hidden_size1, hidden_size2)
        b2 = np.random.randn(hidden_size2)

        z1 = np.dot(inputs, w1) + b1
        a1 = step(z1)

        z2 = np.dot(a1, w2) + b2
        output = step(z2)

        if np.array_equal(outputs, output):
            print(f"Epoch {epoch}: Training complete.")
            break

    print("\nFinal weights and biases:")
    print("Weights between input and first hidden layer (w1):\n", w1)
    print("Biases of first hidden layer (b1):\n", b1)
    print("Weights between first hidden and output layer (w2):\n", w2)
    print("Biases of output layer (b2):\n", b2)

    print("\nTraining complete.")

if __name__ == "__main__":
    
    inputs = np.array([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1],
                       [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1],
                       [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
                       [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]])

    outputs = np.array([[0, 0], [0, 1], [0, 1], [0, 0], [1, 0], [1, 0], [1, 1], [1, 1],
                        [0, 1], [0, 0], [1, 1], [1, 0], [0, 1], [0, 1], [1, 0], [1, 1]])
    
    input_size = inputs.shape[1]
    hidden_size1 = 4
    hidden_size2 = 4
    output_size = outputs.shape[1]

    # Train the MLP
    train_mlp(inputs, outputs, input_size, hidden_size1, hidden_size2, output_size)