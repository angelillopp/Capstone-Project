from flask import Flask, jsonify, request, render_template
import joblib
import socket
import json
import pandas as pd
import os

from functions import train_model, model_predict

MODEL_DIR = "models"
DATA_DIR = "data"

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route('/train', methods=['GET'])
def train_form():
    return render_template('train.html')

@app.route('/train', methods=['POST'])
def train():
    folder_name = request.form['folder_name']
    train_model(folder_name)

    return (jsonify("Model trained succesfully."))

@app.route('/predict', methods=['GET'])
def predict_form():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    start_date = request.form['start_date']
    end_date = request.form['end_date'] 
    prediction = model_predict(start_date, end_date)
    result = 'The total revenue between ' + start_date + ' and ' + end_date + ' is ' + str(sum(prediction))
    
    return (jsonify(result))
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)