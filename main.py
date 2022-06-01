from flask import Flask, render_template
from flask import request
from Daten.Drinks import drinks
from Daten.calculate import max_bak_berechnen, min_bak_berechnen
from datetime import datetime
from Daten.save_data import json_save, sort_data, get_data
from Daten.visualisierung import pie_chart


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
        zeit = request.form['time']
        datum = request.form['date']
        # datum und zeit in datetime format umwandeln
        # zeit_datum = datetime.strptime(str(datum+" "+zeit), "%Y-%m-%d %H:%M")
        zeit_datum = str(datum+" "+zeit)
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        gender = request.form['gender']
        drink = request.form['drink']
        percent = float(request.form['percent'])
        vol = int(request.form['vol'])
        max_bak = max_bak_berechnen(vol, percent, weight, gender, age)
        min_bak = min_bak_berechnen(vol, percent, weight, gender, age)
        user_input = {
                        "name": name,
                        "age": age,
                        "gender": gender,
                        "weight": weight,
                        "zeitpunkt": zeit_datum,
                        "drink": drink,
                        "percent": percent,
                        "vol": vol,
                        "max_bak": max_bak,
                        "min_bak": min_bak
                      }
        json_save(user_input, "Daten/drink_data.json")
        sort_data("Daten/drink_data.json")
        return render_template("input_saved.html", user_input=user_input)



@app.route('/visualisierung')
def visualisierung():
    data = get_data("Daten/drink_data.json")
    pie = pie_chart(data, "drink", "vol")
    return render_template("visualisierung.html", pie=pie)


@app.route('/inputs')
def inputs():
    file_data = get_data("Daten/drink_data.json")
    return render_template("inputs.html", file_data=file_data)


# https://plotly.com/python/line-charts/ -> Line Chart
