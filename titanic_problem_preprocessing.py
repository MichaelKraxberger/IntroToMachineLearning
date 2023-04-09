import pandas as pd
import matplotlib.pyplot as plot
import seaborn as seaborn
import sklearn as sk
import sns as sns
from matplotlib import pyplot as plt


# ----------PART 2---------- #
print(f"\n{'_'*25} PART 2 {'_'*25}")
test = pd.read_csv('./test.csv')
train = pd.read_csv('./train.csv')
test_df = pd.DataFrame(test)
train_df = pd.DataFrame(train)
combine = [train_df, test_df]

# Find the correlation between survived and sex (2.1)
print(f"{'-'*20} Question 2.1 {'-'*20}")
print(f"{'-'*10}[Sex -> Survival Rate]{'-'*10}")
print(train_df[['Sex', 'Survived']].groupby(['Sex'], as_index=False,).mean().sort_values(by='Survived', ascending=False))

# Create 2 visualizations about survival correlations
print(f"\n{'-'*20} Question 2.2 {'-'*20}")
print(f"\n{'-'*10}[Sex -> Survived Visualization]{'-'*10}")
sex_survival = seaborn.FacetGrid(train_df, col="Survived")
sex_survival.map(plt.hist, 'Sex', bins=2)
plt.show()

print(f"\n{'-'*10}[Age -> Survived Visualization]{'-'*10}")
age_survival = seaborn.FacetGrid(train_df, col='Survived')
age_survival.map(plt.hist, 'Age', bins=25)
plt.show()

# ------- PRE PROCESSING -------
print(f"\n{'-'*30} PRE-PROCESSING {'-'*30}")
train_df = train_df.drop(['Ticket', 'Cabin', 'Parch', 'SibSp'], axis=1)
test_df = test_df.drop(['Ticket', 'Cabin', 'Parch', 'SibSp'], axis=1)

for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)

for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess', 'Jonkheer', 'Dona'], 'Lady')
    dataset['Title'] = dataset['Title'].replace(['Capt', 'Don', 'Major', 'Sir'], 'Sir')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

title_mapping = {"Col": 1, "Dr": 2, "Lady": 3, "Master": 4, "Miss": 5, "Mr": 6, "Mrs": 7, "Rev": 8, "Sir": 9}
for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)

train_df = train_df.drop(['Name', 'PassengerId'], axis=1)
test_df = test_df.drop(['Name'], axis=1)
combine = [train_df, test_df]

for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map( {'female': 1, 'male': 0} ).astype(int)

common_value = 'S'
data = [train_df, test_df]

for dataset in data:
    dataset['Embarked'] = dataset['Embarked'].fillna(common_value)

ports = {"S": 0, "C": 1, "Q": 2}
data = [train_df, test_df]

for dataset in data:
    dataset['Embarked'] = dataset['Embarked'].map(ports)

meanAge = int(train_df.Age.dropna().mean())
print('Mean Age = ', meanAge)

for dataset in combine:
    dataset['Age'] = dataset['Age'].fillna(meanAge)
    dataset['Fare'] = dataset['Fare'].fillna(test_df['Fare'].dropna().median())

combine[0].to_csv('train_preprocessed.csv',index=False)
combine[1].to_csv('test_preprocessed.csv',index=False)

