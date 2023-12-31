import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float) # input data # X_train
y = np.array(([92], [86], [89]), dtype=float) # output # y_train
X = X / np.amax(X,axis=0) # maximum of X array longitudinally # normalize # amax = array max
y = y / 100 # max test score is 100 # normalize

def sigmoid(x): # activation function # activation_function
    return 1 / (1 + np.exp(-x)) # sigmoid function # sigmoid_function

#Derivative of Sigmoid Function
def derivatives_sigmoid(x): #derivative of sigmoid # sigmoid_derivative
    return x * (1 - x) # sigmoid derivative 

epoch = 5000 #Setting training iterations #i.e. how many times to train the dataset # number_of_training_iterations
lr = 0.1 #Setting learning rate #i.e. how much the weight changes after each iteration # learning_rate
inputlayer_neurons = 2 #number of features in data set #i.e. number of columns # number_of_features
hiddenlayer_neurons = 3 #number of hidden layers neurons #i.e. number of rows # number_of_hidden_layers
output_neurons = 1 #number of neurons at output layer #i.e. number of rows # number_of_output_neurons

#weight and bias initialization
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons)) #wh = weight hidden # weight_hidden
bh = np.random.uniform(size=(1, hiddenlayer_neurons)) #bh = bias hidden # bias_hidden
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons)) #wout = weight output # weight_output
bout = np.random.uniform(size=(1, output_neurons)) #bout = bias output # bias_output

for i in range(epoch): #i.e. for each iteration 
    #Forward Propogation
    hinp1 = np.dot(X, wh) #dot product of X (input) and first set of 3x2 weights # hidden_layer_input
    hinp = hinp1 + bh #add bias # hidden_layer_input
    hlayer_act = sigmoid(hinp) #activation function # hidden_layer_activation
    outinp1 = np.dot(hlayer_act, wout) #dot product of hidden layer (i.e. hlayer_act) and second set of 3x1 weights # output_layer_input
    outinp = outinp1 + bout #add bias # output_layer_input
    output = sigmoid(outinp) #final activation function # output_layer_activation

    #Backpropagation
    EO = y - output #error output # error_output
    outgrad = derivatives_sigmoid(output)   #apply derivative of sigmoid to error # output_gradient
    d_output = EO * outgrad #multiplication of error and sigmoid # delta_output
    EH = d_output.dot(wout.T) # how much hidden layer wts contributed to error # error_hidden

    #how much hidden layer wts contributed to error 
    hiddengrad = derivatives_sigmoid(hlayer_act) #apply derivative of sigmoid to hidden layer error # hidden_gradient
    d_hiddenlayer = EH * hiddengrad #multiplication of error and sigmoid # delta_hidden_layer

    # dotproduct of nextlayererror and currentlayerop
    wout += hlayer_act.T.dot(d_output) * lr #update output layer weights # weight_output
    wh += X.T.dot(d_hiddenlayer) * lr #update hidden layer weights # weight_hidden

print("Input: \n" + str(X)) #print input data
print("Actual Output: \n" + str(y)) #print output
print("Predicted Output: \n" ,output) #print predicted output