
import numpy as np
from flask import Flask, request, jsonify, render_template,Response
import pickle
import cv2







app = Flask(__name__)


@app.route('/') # Homepage
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('page2.html')

@app.route('/back')
def back():
    return render_template('index.html')
@app.route('/fire')
def fire():
    return render_template('this is new.html')

@app.route('/next')
def next():
    return render_template('state.html')
@app.route('/previous')
def previous():
    return render_template('page2.html')


if __name__ == "__main__":

  app.run()

