import numpy as np
from get_training import *

class NeuralNetwork():
    def __init__(self):
        self.synaptic_weights = 2 * np.random.random((7, 1)) - 1

    def sigmoid(self, x):
        result = 1 / (1 + np.exp(-x))
        return result

    def sigmoid_derivative(self, x):
        result = x * (1 - x)
        return result

    def train(self, training_inputs, training_outputs, iterations):
        for i in range(iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output

def main():
    neural_network = NeuralNetwork()
    training_inputs = get_training_inputs()
    training_outputs = get_training_outputs()

    print("--- Training I/O ---")
    print(training_inputs)
    print(training_outputs)

    neural_network.train(training_inputs, training_outputs, 50000)

    print("--- Synaptic weights after training ---")
    print(neural_network.synaptic_weights)

    A = str(input("Input 1: "))
    B = str(input("Input 2: "))
    C = str(input("Input 3: "))
    D = str(input("Input 4: "))
    E = str(input("Input 5: "))
    F = str(input("Input 6: "))
    G = str(input("Input 7: "))

    print("--- Output: ---")
    print("Near (1) -> likely to be late.\nNear (0) -> likely to be on-time.")
    print("Result: ", end = "")
    print(neural_network.think(np.array([A, B, C, D, E, F, G])))

if __name__ == "__main__":
    main()