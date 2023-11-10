import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    embarked_mapping = {
        'C': (1,0,0),
        'Q': (0,1,0),
        'S': (0,0,1)
    }
    Embarked_C, Embarked_Q, Embarked_S = embarked_mapping.get(request.form['Embarked'], (0, 0, 0))

    sex_mapping = {
        'female': (1, 0),
        'male': (0, 1)
    }
    Sex_female, Sex_male = sex_mapping.get(request.form['Sex'], (0, 0))

    tr_request = {
        'Pclass': request.form['Pclass'],
        'Age': request.form['Age'],
        'SibSp': request.form['SibSp'],
        'Parch': request.form['Parch'],
        'Embarked_C': Embarked_C,
        'Embarked_Q': Embarked_Q,
        'Embarked_S': Embarked_S,
        'Sex_female': Sex_female,
        'Sex_male': Sex_male
    }
    
    int_features = [float(x) for x in tr_request.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
  
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Survived = {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    output_serializable = output.tolist()
    return jsonify(output_serializable)

if __name__ == "__main__":
    app.run(debug=True)