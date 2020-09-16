from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import keras
from keras.models import load_model
import numpy as np

app = Flask(__name__)

model = load_model('export_model_v7.tf')

@app.route("/")
def input_veiw():
    x = ""
    y = 2
    return render_template("index.html", x=x, y=y)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        x = request.form.get("review")
        if x != "" and not x.isspace():
            y = model.predict(np.array([x,]))[0][0]
            return render_template("index.html", x=x, y=y)

    x = ""
    y = 2
    return render_template("index.html", x=x, y=y)
