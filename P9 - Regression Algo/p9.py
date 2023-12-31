import numpy as np
import matplotlib.pyplot as plt

def local_regression(x0, X, Y, tau):
    # formulas:
    # w(x, x0)  = e ^ ((x - x0)^2 / (-2*tau))
    # beta(x0) = (X(transpose) * W * X)^-1 * X(transpose) * W * Y
    # Prediction = beta(x0) * x0

    x0 = [1, x0]
    X = [[1, i] for i in X]
    X = np.asarray(X)

    x_transpose_w = (X.T) * np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau)) # formula = tanspost(X) * exp(||x - orig_x||^2 / (-2*tau))
    # np.exp means 'e' to the power of '()'
    # X.T = transpose of X
    # axis=1 means sum along the row

    prediction = np.linalg.pinv(x_transpose_w @ X) @ x_transpose_w @ Y @ x0
    # @ = matrix multiplication
    # lin_alg = linear algebra
    # p_inv = pseudo inverse

    return prediction

def draw(tau):
    prediction = []
    for orig_val_in_X in domain:
        prediction.append(local_regression(orig_val_in_X, X, Y, tau))

    plt.plot(X, Y, 'o', color='black')
    plt.plot(domain, prediction, color='red')
    plt.show()

X = np.linspace(-3, 3, num=1000) # X -> [-3, -2.994, -2.988, ..., 2.988, 2.994, 3]
Y = np.log(np.abs(X ** 2 - 1) + .5) # Y = log(|X^2 - 1| + 0.5)
domain = X # copy of original X

draw(10)
draw(0.1)
draw(0.01)
draw(0.001)

'''
STEPS:

1. Load the dataset
2. Create a domain of values
3. Create a function to draw the graph
4. Create a function to calculate the local regression

'''