from flask import Flask,request, url_for, redirect, render_template, jsonify
from preprocessing import TextPreprocessing
import pickle

app = Flask(__name__)


def predict_news(text):
    y = pipeline.predict([text])
    return y
def loadModels(name_file):
    with open('models/'+name_file+'.tk', 'rb') as pickle_file:
            model = pickle.load(pickle_file)
    return model

pipeline = loadModels('pipeline')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    new_request = request.form
    y = predict_news(new_request['News'])
    return render_template('home.html',pred='News is {}'.format(y))

if __name__ == '__main__':
    app.run(debug=True)
