from flask import Flask,render_template,request
import os
import pandas as pd
import numpy as np

df = pd.read_csv('Maternal Health Risk Data Set.csv')

df = df.drop_duplicates()

ca_val = []
co_val = []

for column in df.columns:
    if df[column].nunique() <= 10:
        ca_val.append(column)
    else:
        co_val.append(column)

X = df.drop('RiskLevel', axis=1)
y = df['RiskLevel']


app = Flask(__name__)
@app.route("/")
def home():
    image = "img.jpg"
    return render_template("home.html",image=image)

@app.route("/predict",methods=["GET","POST"])
def predict():
    image = "me2.gif"
    age = request.form['age']
    sbp = request.form['sbp']
    dbp = request.form['dbp']
    bls= request.form['bls']
    temp = request.form['temp']
    hr = request.form['hr']
    form_array= np.array([[age,sbp,dbp,bls,temp,hr]])
    print(form_array)

    from sklearn import tree

    # Applying Decision Tree
    # Create tree object
    decision_tree = tree.DecisionTreeClassifier(criterion='gini')

    # Train DT based on scaled training set
    decision_tree.fit(X, y)

    print("Accuracy:", decision_tree.score(X, y))
    print("According to Decision Tree your risk prediction is :")

    y_pred = decision_tree.predict(form_array)
    if (y_pred == 'high risk'):
        str = 'HIGH RISK!!!'
    elif (y_pred == 'mid risk'):
        str = 'MID RISK!!'
    elif (y_pred == 'low risk'):
        str = 'LOW RISK!!'
    result=str


    return render_template("result.html",result = result,image=image)

if __name__ == "__main__":
    app.run(debug=True)

























