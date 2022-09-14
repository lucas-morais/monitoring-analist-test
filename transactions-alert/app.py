from dash import Dash, html
import pandas as pd

# import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("dados/pivoted_transactions.csv")

print(df.head())
print(df.dtypes)
colors = {"background": "#111111", "text": "#7FDBFF"}


app.layout = html.Div(
    children=[
        html.H1(
            children="Sistema de Alerta de Transações",
            style={"textAlign": "center", "color": colors["text"]},
        ),
    ],
    style={"background": colors["background"]},
)


if __name__ == "__main__":
    app.run_server(debug=True)
