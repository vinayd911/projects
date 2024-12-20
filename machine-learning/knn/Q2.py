import numpy as np
import math

print("Question 2:\n")
trees = { 'T1': (4, 0), 'T2': (0, 4), 'T3': (3, 9), 'T4': (7, 9)}

#load dataset 
def load_data(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            data.append([int(parts[0]), int(parts[1]), int(parts[2])])
    return data

#manhattan distance formula
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

#closest tree with manhattan distance
def add_tree_info(data):
    new_data = []
    for point in data:
        x, y = point[0], point[1]
        min_dist = float('inf')
        closest_tree = None
        
        for tree, coords in trees.items():
            dist = manhattan_distance(x, y, coords[0], coords[1])
            if dist < min_dist:
                min_dist = dist
                closest_tree = tree
        
        #one-hot encoding
        tree_one_hot = [1 if closest_tree == tree else 0 for tree in ['T1', 'T2', 'T3', 'T4']]
        new_data.append(point + [min_dist, closest_tree] + tree_one_hot)
    
    return new_data

#save data to file
def save_to_file(data, filepath):
    with open(filepath, 'w') as f:
        f.write("X\tY\tOccupied\tManhattanDistance\tClosestTree\tTree_T1\tTree_T2\tTree_T3\tTree_T4\n")
        for row in data:
            row_str = '\t'.join(map(str, row))
            f.write(row_str + '\n')

#euclidean distance formula
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

#knn step 1
def knn(train_data, test_point, k, feature_indices):
    distances = []
    
    for train_point in train_data:
        dist = euclidean_distance( *(train_point[i] for i in feature_indices[:2]), *(test_point[i] for i in feature_indices[:2]))
        distances.append((dist, train_point[2]))
    
    distances.sort(key=lambda x: x[0])
    neighbors = [label for _, label in distances[:k]]
    
    prediction = 1 if sum(neighbors) > len(neighbors) / 2 else 0
    return prediction

#knn step 2
def evaluate_knn(data, feature_indices, k, output_file):
    #split dataset start
    np.random.seed(42)
    np.random.shuffle(data)
    
    split_index = int(0.8 * len(data))
    train_data = data[:split_index]
    test_data = data[split_index:]
    
    y_true = []
    y_pred = []
    
    for test_point in test_data:
        y_true.append(test_point[2])
        prediction = knn(train_data, test_point, k, feature_indices)
        y_pred.append(prediction)
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    accuracy = np.mean(np.array(y_true) == np.array(y_pred))
    tp = np.sum((y_true == 1) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    
    #consider case for division by zero
    precision = tp / (tp + fp) if (tp + fp) != 0 else 0
    recall = tp / (tp + fn) if (tp + fn) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    
    confusion_matrix = np.array([[tn, fp], [fn, tp]])
    with open(output_file, 'a') as f:
        f.write(f"K = {k}, Feature set: {feature_indices}\n")
        f.write(f"i. Accuracy = {accuracy}\n")
        f.write(f"ii. Precision = {precision}\n")
        f.write(f"iii. Recall = {recall}\n")
        f.write(f"iv. F1 Score = {f1_score}\n")
        f.write(f"v. Confusion Matrix:\n{confusion_matrix}\n\n")
    
    return accuracy, precision, recall, f1_score, confusion_matrix

#load input file
file_path = 'P1input2024.txt'
data = load_data(file_path)

#tree info to data
data_with_tree_info = add_tree_info(data)

#save to long records
output_file_path = 'P1input2024LongRecords.txt'
save_to_file(data_with_tree_info, output_file_path)

print(f"Data successfully saved to {output_file_path}\n")

output_file = 'P1Output2024.txt'


#feature sets
feature_set_1 = [0, 1]  # X, Y
feature_set_2 = [0, 1, 3]  # X, Y, manhattan distance
feature_set_3 = [0, 1, 3, 4, 5, 6, 7]  # X, Y, manhattan distance, one hot encoding
with open(output_file, 'a') as f:
    f.write("Question 2:\n\n")
#loop for k values
for k in [3, 5, 7]:
    print(f"K = {k}")
    #set 1
    accuracy_set_1, precision_set_1, recall_set_1, f1_set_1, cm_set_1 = evaluate_knn(data_with_tree_info, feature_set_1, k, output_file)
    print(f"i. Set 1 (X, Y):\nAccuracy = {accuracy_set_1}\nPrecision = {precision_set_1}\nRecall = {recall_set_1}\nF1 Score = {f1_set_1}\nConfusion Matrix:\n{cm_set_1}\n")
        
    #set 2
    accuracy_set_2, precision_set_2, recall_set_2, f1_set_2, cm_set_2 = evaluate_knn(data_with_tree_info, feature_set_2, k, output_file)
    print(f"ii. Set 2 (X, Y, Manhattan Distance):\nAccuracy = {accuracy_set_2}\nPrecision = {precision_set_2}\nRecall = {recall_set_2}\nF1 Score = {f1_set_2}\nConfusion Matrix:\n{cm_set_2}\n")
        
    #set 3
    accuracy_set_3, precision_set_3, recall_set_3, f1_set_3, cm_set_3 = evaluate_knn(data_with_tree_info, feature_set_3, k, output_file)
    print(f"iii. Set 3 (X, Y, Manhattan Distance, One Hot Tree):\nAccuracy = {accuracy_set_3}\nPrecision = {precision_set_3}\nRecall = {recall_set_3}\nF1 Score = {f1_set_3}\nConfusion Matrix:\n{cm_set_3}\n")
