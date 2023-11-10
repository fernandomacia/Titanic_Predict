import requests

url = 'http://localhost:5000/results'

# Datos del PassengerId 1 con Survived 0
r = requests.post(url,json={
    'Pclass': 3, 
    'Age': 22.0, 
    'SibSp': 1, 
    'Parch': 0, 
    'Embarked_C': 0, 
    'Embarked_Q': 0, 
    'Embarqued_S': 1, 
    'Sex_female': 0, 
    'Sex_male': 1})

print(f'El resultado del PassengerId 1 deberia ser Survived 0 y es: {r.json()}')

# Datos del PassengerId 2 con Survived 1
r = requests.post(url,json={
    'Pclass': 1, 
    'Age': 38.0, 
    'SibSp': 1, 
    'Parch': 0, 
    'Embarked_C': 1, 
    'Embarked_Q': 0, 
    'Embarqued_S': 0, 
    'Sex_female': 1, 
    'Sex_male': 0})

print(f'El resultado del PassengerId 2 deberia ser Survived 1 y es: {r.json()}')