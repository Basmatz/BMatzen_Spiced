from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix


ypred1 = [0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1]*50
ytrue1 = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]*50

ypred = [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]*10
ytrue = [1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]*10

print("\n\nModel 1: \n", confusion_matrix(ypred1, ytrue1), end="\n\n")
print("Precision: ", precision_score(ypred1, ytrue1))
print("Accuracy: ", accuracy_score(ypred1, ytrue1))
print("Recall: ", recall_score(ypred1, ytrue1))
print("F1: ", f1_score(ypred1, ytrue1))
print("\n\n")
print("Model 2: \n", confusion_matrix(ypred, ytrue), end="\n\n")
print("Precision: ", precision_score(ypred, ytrue))
print("Accuracy: ", accuracy_score(ypred, ytrue))
print("Recall: ", recall_score(ypred, ytrue))
print("F1: ", f1_score(ypred, ytrue))
