import plotly.express as px
from plotly.offline import plot


# Line Chart erstellen
def line_chart(x_data, y_data):
    fig = px.line(x=x_data, y=y_data, title="BAK Verlauf",
                  labels={"x": "Uhrzeit", "value": "Blutalkoholkonzentration",
                          "variable": "Legende (Werte in Promille)"})
    # Y-Werte benennen
    fig.data[0].name = "Max. BAK"
    fig.data[1].name = "Geschätzte BAK"
    fig.data[2].name = "Min. BAK"
    fig.update_traces(mode="lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified")
    div_line = plot(fig, output_type="div")
    return div_line


# Pie Chart Volumen erstellen
def pie_ml(value_data, key_data):
    fig = px.pie(values=value_data, names=key_data, title="Anteil Getränke in mL",
                 color_discrete_sequence=px.colors.sequential.Plasma_r)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    div_pie = plot(fig, output_type="div")
    return div_pie


# Pie Chart BAK erstellen
def pie_bak(value_data, key_data):
    fig = px.pie(values=value_data, names=key_data, title="Anteil Getränke in BAK",
                 color_discrete_sequence=px.colors.sequential.Plasma_r)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    div_pie = plot(fig, output_type="div")
    return div_pie
