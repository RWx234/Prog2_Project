from flask import Flask, render_template
from flask import request
from Daten.Drinks import drinks
from Daten.calculate import max_bak_berechnen, min_bak_berechnen
# from datetime import datetime
from Daten.save_data import json_save, sort_data, get_data, line_chart_data, pie_chart_data
from Daten.visualisierung import line_chart, pie_chart


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
        zeit_datum = str(datum+" "+zeit)
        age = int(request.form['age'])
        weight = float(request.form['weight'])
        gender = request.form['gender']
        drink = request.form['drink']
        percent = float(request.form['percent'])
        vol = int(request.form['vol'])
        max_bak = round(max_bak_berechnen(vol, percent, weight, gender, age), 4)
        min_bak = round(min_bak_berechnen(vol, percent, weight, gender, age), 4)
        av_bak = round((max_bak + min_bak) / 2, 4)
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
                        "min_bak": min_bak,
                        "av_bak": av_bak
                      }
        json_save(user_input, "Daten/drink_data.json")
        sort_data("Daten/drink_data.json")
        return render_template("input_saved.html", user_input=user_input)



@app.route('/visualisierung')
def visualisierung():
    # Line Chart
    line_data = line_chart_data("Daten/drink_data.json")
    line_data_av = line_data[0]
    line_data_min = line_data[1]
    line_data_max = line_data[2]
    x_data = list(line_data_av.keys())
    y_data = [list(line_data_max.values()), list(line_data_av.values()), list(line_data_min.values())]
    line_div = line_chart(x_data, y_data)
    # Pie Chart
    pie_data, pie_data_keys, pie_data_values = pie_chart_data("Daten/drink_data.json")
    pie_div = pie_chart(pie_data_values, pie_data_keys)
    return render_template("visualisierung.html",
                           x_data=x_data,
                           y_data=y_data,
                           line_div=line_div,
                           pie_div=pie_div,
                           pie_data=pie_data,
                           pie_data_keys=pie_data_keys,
                           pie_data_values=pie_data_values)


@app.route('/inputs')
def inputs():
    file_data = get_data("Daten/drink_data.json")
    return render_template("inputs.html", file_data=file_data)
