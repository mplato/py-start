import numpy as np


def sigmoid(x):
    return 1/(1 + np.exp(-x))


trainingInput = np.array([[0, 0, 1],
                          [1, 1, 1],
                          [1, 0, 1],
                          [0, 1, 1]])

trainingOutput = np.array([[0, 1, 1, 1]]).T

np.random.seed(1)

synapitcWheights = 2 * np.random.random((3, 1)) - 1
