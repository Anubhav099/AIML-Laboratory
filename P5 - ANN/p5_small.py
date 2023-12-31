import numpy as np

x = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
x = x / np.amax(x, axis=0) # axis=0 means column-wise max
y = y / 100

def sigmoid(x): # 1 / (1 + e^-x)
    return 1 / (1 + np.exp(-x)) 

def derivatives_sigmoid(x):
    return x * (1 - x)

hidden_weight = np.random.uniform(size=(2, 3)) # 2 inputs, 3 hidden neurons
output_weight = np.random.uniform(size=(3, 1)) # 3 hidden neurons, 1 output
hidden_bias = np.random.uniform(size=(1, 3)) # 1 bias, 3 hidden neurons
output_bias = np.random.uniform(size=(1, 1)) # 1 bias, 1 output

for _ in range(5000):
    hidden_layer_activation = sigmoid(np.dot(x, hidden_weight) + hidden_bias)
    output_layer_activation = sigmoid(np.dot(hidden_layer_activation, output_weight) + output_bias)

    delta_output = (y - output_layer_activation) * derivatives_sigmoid(output_layer_activation)
    delta_hidden_layer = delta_output.dot(output_weight.T) * derivatives_sigmoid(hidden_layer_activation)

    hidden_weight += x.T.dot(delta_hidden_layer) * 0.1
    output_weight += hidden_layer_activation.T.dot(delta_output) * 0.1

print("Input:\n", x)
print("Actual Output:\n", y)
print("Predicted Output:\n", output_layer_activation)
