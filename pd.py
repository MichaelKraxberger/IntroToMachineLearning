from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC, SVC
import warnings
warnings.filterwarnings('ignore')

# read in dataframe
df = pd.read_csv(r"pd_speech_features.csv")

# assign X and y classes
X = df.drop('class',axis=1).values
y = df['class'].values

# perform scaling for later
scaler = StandardScaler()
X_Scale = scaler.fit_transform(X)

# build the pca
pca2 = PCA(n_components=3)
# fit the scaled data
principalComponents = pca2.fit_transform(X_Scale)

# make a dataframe to reassign the data
principalDf = pd.DataFrame(data = principalComponents, columns = ['component 1', 'component 2', 'component 3'])
finalDf = pd.concat([principalDf, df[['class']]], axis = 1)
X = finalDf.drop('class',axis=1).values
y = finalDf['class'].values

# assign to train and test classes
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,random_state=0)
# fit to svc and print
svc = SVC()
svc.fit(X, y)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, y_train) * 100, 2)
print("svm accuracy =", acc_svc)
