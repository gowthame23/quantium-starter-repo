import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read the processed data file
df = pd.read_csv("formatted_data.csv")

# Convert date column to datetime and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create Dash app
app = Dash(__name__)

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

# Axis labels
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# App layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)