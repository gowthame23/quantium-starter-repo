import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("formatted_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date")

app = Dash(__name__)

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)