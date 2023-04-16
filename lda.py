import warnings

import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

warnings.filterwarnings('ignore')

# Part 1
print(f"\n{'_' * 20}Part 1{'_' * 20}")
# create the dataframe
df = pd.read_csv(r"Iris.csv")
scaler = StandardScaler()
# read in x and y
X = df.iloc[:, 0:4]
y = df.iloc[:, -1]

# assign training and test data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3,random_state=0)
# scale x
X_Scale = scaler.fit_transform(X_train)

# instantiate and fit data to lda
lda = LDA(n_components=2)
lda_train = lda.fit_transform(X_Scale, y_train)

# create dataframe for viewing
principalDf = pd.DataFrame(data=lda_train, columns=['component 1', 'component 2'])

finalDf = pd.concat([principalDf, df[['Species']]], axis=1)
print(finalDf.head())