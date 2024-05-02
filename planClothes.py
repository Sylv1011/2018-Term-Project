import numpy as np #Scientific computing package -Array
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt
from csv import reader
from sklearn.model_selection import train_test_split
from random import randrange
from random import seed
from math import sqrt

##source
#https://machinelearningmastery.com/implement-random-forest-scratch-python/

##Machine Learning Random Forest

#According to user's selection, update the dataset by modifying the info
# in a certain cell

#writes for top
def writeFile1(filename,topname,index,decision):
    import csv
    r = csv.reader(open(filename))
    lines = list(r)
    row = int(topname[3:])
    lines[row][index] = decision
    
    writer = csv.writer(open(filename, "w"))
    writer.writerows(lines)

#writes for bottom and dress
def writeFile2(filename,botname,index,decision):
    import csv
    r = csv.reader(open(filename))
    lines = list(r)
    row = int(botname[1:])
    lines[row][index] = decision
    
    writer = csv.writer(open(filename, "w"))
    writer.writerows(lines)

#writes for outwears
def writeFile3(filename,outname,index,decision):
    import csv
    r = csv.reader(open(filename))
    lines = list(r)
    row = int(outname[2:])
    lines[row][index] = decision
    
    writer = csv.writer(open(filename, "w"))
    writer.writerows(lines)
###
#load a csv file and input datas into a 2-D list
def load_csv(filename):
    import csv
    dataset=[]
    with open(filename, "r") as file:
        rows = csv.reader(file)
        for row in rows:
            dataset.append(row)
    #does not return the first row, titles
    return dataset[1:]

#returns a 2d list with top name and all features: all yes features 1 and all
#no features 0
def numCSV(filename):
    dataset = load_csv(filename)
    actual = []
    for row in dataset:
        newRow = []
        newRow.append(row[0])
        for col in range(1,len(row)):
            if row[col] == "n" or row[col] =="" or row[col] =="change" or row[col] =="No":
                newRow.append(0)
            else:
                newRow.append(1)
        actual.append(newRow)
    return actual

def test_num(index, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] == 0:
            left.append(row)
        elif row[index] == 1:
            right.append(row)
    return left, right 
    
#splits the attributes from the result
def splitXandY(data):
    xs = []
    ys = []
    for row in data[1:]:
        xs.append(row[:-1])
        ys.append(row[-1])
    return xs, ys

#helper function, excludes clothing name from the rest of the list
def binaryData(filename):
    run = load_csv(filename)
    result=[]
    for terms in run:
        result += [terms[1:]]
    return result


def convertSubset(filename, lst):
    import csv
    result = []
    tops = set()
    for rows in lst:
        tops.add(rows[0])
    with open(filename, "r") as file:
        rows = csv.reader(file)
        for row in rows:
            if row[0] in tops:
                result.append(row)
    return result
    
# Split a dataset based on an attribute and an attribute value
# If a certain index is "0"/"n": then divide upon that index
def test_split(index, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] == "n" or "change":
            left.append(row)
        elif row[index] == "y" or "save":
            right.append(row)
    return left, right
    
# Avoid overfitting of the dataset to get the best result
# Split a dataset into a train and test set
#convention is 2/3 with replacement
def train_test_split(dataset, split):
    train = list()
    train_size = split * len(dataset)
    dataset_copy = list(dataset)
    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy

#tests the accuracy of the prediction
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds=train_test_split(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores


# Calculate the Gini index for a split dataset
#Gini index, how group fits the class
def gini_index(groups, classes):
    # count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))
    # sum weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size=float(len(group))
        # avoid divide by zero
        if size == 0:
            continue
        score = 0.0
        # score the group based on the score for each class
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        # weight the group score by its relative size
        gini += (1.0 - score)*(size/n_instances)
    return gini
    
# Select the best split point for a dataset
#where gini index is the lowest
def get_split(dataset):
    giniList = []
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset[0])-1):
        for row in dataset:
            groups = test_split(index, dataset)
            gini = gini_index(groups, class_values)
            giniList.append(gini)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    print(giniList)
    return {'index':b_index, 'value':b_value, 'groups':b_groups}

def to_terminal(group):
    outcomes=[row[-1] for row in group]
    return max(set(outcomes),key=outcomes.count)
    

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    # check for max depth
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    # process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth+1)
    # process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth+1)

# Build a decision tree
def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root
    
# Print a decision tree
def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d : %s]' % ((depth*' ', (node['index']+1), node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))

def predict(node, row):
    if row[node['index']] != "n":
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

def decision_tree(train, test, max_depth, min_size):
    tree = build_tree(train, max_depth, min_size)
    predictions = list()
    for row in test:
        prediction = predict(tree, row)
        predictions.append(prediction)
    return(predictions)


dataset = load_csv("Top.csv")
tree=build_tree(dataset,5,3)
print_tree(tree)
# split = get_split(dataset)
# print(split)

seed(1)
n_folds = 0.2
max_depth=5
min_size = 1
print(dataset)
scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)
print('Scores: %s' % scores)
print('Mean Accuracy: %.2f%%' % (sum(scores)/float(len(scores))))

