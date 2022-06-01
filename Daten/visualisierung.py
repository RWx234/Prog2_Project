import plotly.express as px

line_data = {}
pie_data = {}

for entry in drink_data:
    line_data[drink_data["zeitpunkt"]] = 0.5*(drink_data["max_bak"]+drink_data["min_bak"])
    pie_data[drink_data["drink"]] = drink_data["vol"]


def pie_chart(pie_data, nam, val)
    fig = px.pie(pie_data, values=val, names=nam)
    return fig
