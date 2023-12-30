from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

iris_dataset=load_iris()

#display the iris dataset
print("\n IRIS FEATURES \ TARGET NAMES: \n ", iris_dataset.target_names)
for i in range(len(iris_dataset.target_names)):
    print("\n[{0}]:[{1}]".format(i,iris_dataset.target_names[i]))

# print("\n IRIS DATA :\n",iris_dataset["data"])
#split the data into training and testing data

X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)
#train and fit the model
kn = KNeighborsClassifier(n_neighbors=5)
kn.fit(X_train, y_train)
for i in range(len(X_test)):
    x = X_test[i]
    x_new = np.array([x])
    prediction = kn.predict(x_new)
    print("\nActual : {0} {1}, Predicted:{2} {3}".format(y_test[i], iris_dataset["target_names"][y_test[i]], prediction, iris_dataset["target_names"][ prediction]))
print("\nTEST SCORE[ACCURACY]: {:.2f}\n".format(kn.score(X_test, y_test)))
