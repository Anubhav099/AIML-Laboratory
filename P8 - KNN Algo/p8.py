from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
print("\n IRIS FEATURES \ TARGET NAMES:", iris_dataset.target_names)
for i in range(len(iris_dataset.target_names)):
    print("\n [{}]:[{}]".format(i,iris_dataset.target_names[i]))

x_train, x_test, y_train, y_test = train_test_split(iris_dataset.data, iris_dataset.target, random_state=0)
kn = KNeighborsClassifier(n_neighbors=5)
kn.fit(x_train, y_train)

# x_test -> list of input features [][4]
# y_test -> list of target output []
for i in range(len(x_test)):
    cur_row = x_test[i]
    row_array = np.array([cur_row])
    prediction = kn.predict(row_array) # 0, 1 or 2
    print("\nActual: [{}] [{}]\nPredicted:{} {}".format(y_test[i], iris_dataset.target_names[y_test[i]], prediction, iris_dataset.target_names[prediction]))

print("\nTEST SCORE[ACCURACY]: {:.2f}\n".format(kn.score(x_test, y_test)))



''' 
iris_dataset KEYS :
['data', 'target', 'target_names']

STEPS:
1. Load the iris dataset
2. Split the dataset into training and testing sets
3. Create a KNN classifier
4. Fit the model using the training sets
5. Predict the output for the test dataset
6. Print the actual and predicted values

'''