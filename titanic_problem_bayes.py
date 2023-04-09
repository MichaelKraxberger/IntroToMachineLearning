import warnings

import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

warnings.filterwarnings("ignore")

train = pd.read_csv('./train_preprocessed.csv')
test = pd.read_csv('./test_preprocessed.csv')

x_train = train.iloc[:, :-1]
y_train = train.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)

classifier = GaussianNB()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Acuuracy!!
print("Accuracy is:", accuracy_score(y_pred, y_test))
