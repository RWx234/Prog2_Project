import plotly.express as px
from plotly.offline import plot


def line_chart(x_data, y_data):
    fig = px.line(x=x_data, y=y_data, title="Promilleverlauf",
                  labels={"x": "Uhrzeit", "value": "Blutalkoholkonzentration",
                          "variable": "Legende", "wide_variable_0": "Max. BAK",
                          "wide_variable_1": "Geschätzte BAK", "wide_variable_2": "Min. BAK"})
    div_line = plot(fig, output_type="div")
    return div_line


def pie_chart(value_data, key_data):
    fig = px.pie(values=value_data, names=key_data)
    div_pie = plot(fig, output_type="div")
    return div_pie
