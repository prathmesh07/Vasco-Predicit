# -*- coding: utf-8 -*-

import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('model.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# # Bind home function to URL
# @app.route('/')
# def home():
#     return render_template('Heart Disease Classifier.html')


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'Prathmesh':'pass@123','Mihir':'pass@123','Siddharth':'pass@123','Kshitij':'pass@123','Simran':'pass@123','Leela':'pass@123'}

@app.route('/home')
def heello_world():
    return render_template('Heart Disease Classifier.html')

@app.route('/team')
def team():
    return render_template('Team.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/Info')
def Info():
    return render_template('Info.html')

@app.route('/signout')
def helllo_world():
    return render_template("login.html")
database={'Prathmesh':'pass@123','Mihir':'pass@123','Siddharth':'pass@123','Kshitij':'pass@123','Simran':'pass@123','Leela':'pass@123'}


@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('Heart Disease Classifier.html',name=name1)



# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('Heart Disease Classifier.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('Heart Disease Classifier.html', 
                               result = 'The patient is likely to have heart disease!')

if __name__ == "__main__":
    app.run(debug=True)
    
    
