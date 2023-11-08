import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
import pickle


df = pd.read_csv("./train.csv")
df.set_index('PassengerId', inplace=True)
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Embarked']]
df = df.dropna()
em = df[['Embarked', 'Sex']]
em = pd.get_dummies(em)
df = pd.concat([df, em], axis=1)
df = df.drop(['Embarked','Sex'], axis = 1)

X = df.drop('Survived', axis=1)
y = df[['Survived']]

X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2, random_state=42)


lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train.values.ravel())
lr_predictions = lr.predict(X_test)
accuracy = accuracy_score(y_test, lr_predictions)
print(f'Precisión del modelo: {accuracy:.2f}')

pickle.dump(regressor, open('model.pkl','wb'))