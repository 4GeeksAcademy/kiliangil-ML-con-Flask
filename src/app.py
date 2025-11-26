from utils import db_connect
engine = db_connect()

# your code here

from flask import Flask, request, render_template
from pickle import load
import joblib

app = Flask(__name__)

model = joblib.load("mejor_modelo_tree.pkl")
class_dict = {
    "0": "No Diabético",
    "1": "Diabético"
}
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        # Obtain values from form
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])
        val3 = float(request.form["val3"])
        val4 = float(request.form["val4"])
        val5 = float(request.form["val5"])
        val6 = float(request.form["val6"])
        
        data = [[val1, val2, val3, val4, val5, val6]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)