from flask import Flask, render_template
from flask import request
from Daten.Drinks import drinks
from Daten.calculate import bak_berechnen


# Create a Flask Instance
app = Flask(__name__)
# CSRF Key - For Webform
app.config['SECRET_KEY'] = "SecretKey"
# WTF_CSRF_ENABLED = False


# Create a route decorator
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/erfassung', methods=['GET', 'POST'])
def erfassung():
    drink_list = drinks
    if request.method.lower() == "get":
        return render_template('erfassung.html', drink_list=drink_list)
    if request.method.lower() == "post":
        name = request.form['name']
        time = request.form['time']
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        gender = request.form['gender']
        drink = request.form['drink']
        percent = float(request.form['percent'])
        vol = int(request.form['vol'])
        bak = bak_berechnen(vol, percent, weight, gender, age)
        user_input = {
                        "name": name,
                        "age": age,
                        "gender": gender,
                        "weight": weight,
                        "time": time,
                        "drink": drink,
                        "percent": percent,
                        "vol": vol,
                        "bak": bak
                      }
        return render_template("input_saved.html", user_input=user_input)



@app.route('/visualisierung')
def visualisierung():
    return render_template("visualisierung.html")


# https://plotly.com/python/line-charts/ -> Line Chart