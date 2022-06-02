import plotly.express as px
from plotly.offline import plot


def line_chart(line_data, x_data, y_data):
    fig = px.line(x=x_data, y=y_data)
    div_line = plot(fig, output_type="div")
    return div_line


def pie_chart(pie_data, value_data, key_data):
    fig = px.pie(values=value_data, names=key_data)
    div_pie = plot(fig, output_type="div")
    return div_pie
