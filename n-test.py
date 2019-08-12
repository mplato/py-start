import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivatives(x):
    return x * (1 - x)


trainingInput = np.array([[0, 0, 1],
                          [1, 1, 1],
                          [1, 0, 1],
                          [0, 1, 1]])

trainingOutput = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synapitcWheights = 2 * np.random.random((3, 1)) - 1

print('Random starting synaptic weights: ')
print(synapitcWheights)

for i in range(5):
    inputLayer = trainingInput
    output = sigmoid(np.dot(inputLayer, synapitcWheights))
    error = trainingOutput - output
    adjustment = error * sigmoid_derivatives(output)
    synapitcWheights += np.dot(inputLayer.T, adjustment)

print('\nSynaptic weights after training: ')
print(synapitcWheights)

print('\nOutput after training: ')
print(output)
