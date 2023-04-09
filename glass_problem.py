import warnings

import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC

warnings.filterwarnings("ignore")

glass = pd.read_csv("./glass.csv")
X = glass.iloc[:, :-1].values
y = glass.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print(f"{'_' * 20}Naive-Bayes{'_' * 20}")

classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Accuracy!

print('accuracy is', accuracy_score(y_pred, y_test))

print(f"\n{'_' * 20}Linear SVM{'_' * 20}")
# add the max_iter parameter and see the resutls
X = glass.iloc[:, :-1].values
y = glass.iloc[:, -1].values
svc = LinearSVC()


svc.fit(X, y)

Y_pred = svc.predict(X_test)

acc_svc = round(svc.score(X_train, y_train) * 100, 2)

print("svm accuracy =", acc_svc)

