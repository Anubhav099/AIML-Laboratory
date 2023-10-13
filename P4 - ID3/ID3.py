import pandas as pd
import numpy as np
from numpy import log2 as log
import pprint

eps = np.finfo(float).eps
df = pd.read_csv("D:\GitHUB\AIML-Lab\P4 - ID3\PlayTennis.csv")

def find_entropy(df):
    target_col = df.keys()[-1]   # get the target column name
    entropy = 0
    target_col_values = df[target_col].unique()

    for value in target_col_values:
        # Count the number of times the value appears in the target column
        value_count = df[target_col].value_counts()[value]
        fraction = value_count / len(df[target_col])
        entropy += -fraction * np.log(fraction)
    
    return entropy

def find_entropy_attribute(df, attribute_name):
    target_col = df.keys()[-1]   # get the target column name
    target_variables = df[target_col].unique()  # get all unique values of the target column
    attribute_values = df[attribute_name].unique()    # get all unique values of the attribute column
    entropy_attribute = 0
    
    for attribute_value in attribute_values:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attribute_name][df[attribute_name] == attribute_value][df[target_col] == target_variable])
            den = len(df[attribute_name][df[attribute_name] == attribute_value])
            fraction = num / (den + eps)
            entropy += -fraction*np.log(fraction+eps)
        
        fraction2 = den / len(df)
        entropy_attribute += -fraction2 * entropy
    
    return abs(entropy_attribute)

def find_best_attribute(df):
    information_gain = []
    for attribute_name in df.keys()[:-1]:
        information_gain.append(find_entropy(df) - find_entropy_attribute(df, attribute_name))
    
    return df.keys()[:-1][np.argmax(information_gain)]

def get_subtable(df, attribute, value):
    return df[df[attribute] == value].reset_index(drop=True)

def build_tree(df, tree=None): 
    target_attribute = df.keys()[-1]   # get the target attribute name
    best_attribute = find_best_attribute(df)
    attribute_values = np.unique(df[best_attribute])
    
    if tree is None:                    
        tree={}
        tree[best_attribute] = {}
    
    for value in attribute_values:
        subtable = get_subtable(df, best_attribute, value)
        col_values, counts = np.unique(subtable[target_attribute], return_counts=True)  

        if len(counts) == 1:
            tree[best_attribute][value] = col_values[0]                                                    
        else:        
            tree[best_attribute][value] = build_tree(subtable)
                   
    return tree




# ------------- testing -------------
print("Given play tennis data set:\n\n", df)

tree = build_tree(df)
print("\nDECISION TREE:")
pprint.pprint(tree)

def predict(test_instance, tree, default = None):
    attribute = next(iter(tree))
    if test_instance[attribute] in tree[attribute].keys():
        result = tree[attribute][test_instance[attribute]]
        if isinstance(result, dict):
            return predict(test_instance, result)
        else:
            return result
    else:
        return default

test_instance = {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak'}
predicted_label = predict(test_instance, tree)
print("Predicted label for test instance:", predicted_label)










# ------------- unrelated -------------
print("\n\nEntropy of the dataset:", find_entropy(df))

def all_yes_rows(df):
    filtered_df = df[df['Play Tennis'] == 'Yes']
    return filtered_df

print(all_yes_rows(df)) # Print all the rows where label = "Yes"

def countRows():
    numRows = len(df)
    return numRows

print("No. of Rows in the dataset =",countRows())

def countCols():
    numCols = df.shape[1]
    return numCols

print("No. of Cols in the dataset =",countCols())