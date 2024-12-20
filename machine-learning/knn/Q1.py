import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix

print("Question 1: \n")
#load dataset 
file_path = "P1input2024.txt"
data = pd.read_csv(file_path, sep="\t", header=None, names=['X', 'Y', 'Occupied'])

#split dataset to x feature and y target
x = data[['X', 'Y']]
y = data['Occupied']

#split to 80 train 20 test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

#knn function
def func_knn(k):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1_scor = f1_score(y_test, y_pred)
    conf_mat = confusion_matrix(y_test, y_pred)

    print(f"K={k}")
    print(f"i. Accuracy: {accuracy}")
    print(f"ii. Recall: {recall}")
    print(f"iii. Precision: {precision}")
    print(f"iv. f1 score: {f1_scor}")
    print(f"v. Confusion Matrix:\n{conf_mat}\n")
    
    return accuracy, recall, precision, f1_scor, conf_mat

#loop for k values
results = {}
for k in [3, 5, 7]:
    results[k] = func_knn(k)

#save results to file
with open("P1Output2024.txt", "w") as f:
    f.write(f"Question 1:\n")
    for k, (accuracy, recall, precision, f1, cm) in results.items():
        f.write(f"K={k}\n")
        f.write(f"i. Accuracy: {accuracy}\n")
        f.write(f"ii. Recall: {recall}\n")
        f.write(f"iii. Precision: {precision}\n")
        f.write(f"iv. F1 Score: {f1}\n")
        f.write(f"v. Confusion Matrix:\n{cm}\n\n")

print("Executed, results saved to P1Output2024.txt\n")