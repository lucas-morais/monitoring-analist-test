import streamlit as st
import pandas as pd

from plotting_tools import line_plot

# Configuração pandas
pd.options.display.float_format = "{:,.2f}".format

st.title("Análise: Checkout Data")

df = pd.read_csv("dados/checkout_data.csv")

st.header("Dados")
st.write(df.head(10).round(2).style.highlight_null())
st.header("Dados Nulos")
na = df.isna().sum()
na.rename("NA", inplace=True)
st.write(na)

##
df.fillna(0, inplace=True)
df["time"] = pd.to_datetime(df["time"], format="%Hh").dt.strftime("%H")
df.set_index("time", inplace=True)


st.subheader(
    "Para simplificar a análise, os valores"
    + " indefinnidos serão substituídos por '0'.",
)

st.write(df.describe())
st.write(df.T.describe())
markers = [6, 10]
st.pyplot(
    line_plot(
        y="today",
        data=df,
        title="HOJE",
        xlabel="Hora",
        ylabel="POS",
        markers=markers,
    )
)
st.pyplot(
    line_plot(
        y="yesterday", data=df, title="ONTEM", xlabel="Hora", ylabel="POS"
    )
)
st.pyplot(
    line_plot(
        y="same_day_last_week",
        data=df,
        title="MESMO DIA NA SEMANA PASSADA",
        xlabel="Hora",
        ylabel="POS",
    )
)
st.pyplot(
    line_plot(
        y="avg_last_7days",
        data=df,
        title="MÉDIA DA SEMANA PASSADA",
        xlabel="Hora",
        ylabel="POS",
    )
)

st.pyplot(
    line_plot(
        y="avg_last_30days",
        data=df,
        title="MÉDIA DO ÚLTIMO MÊS",
        xlabel="Hora",
        ylabel="POS",
        markers=markers,
    )
)
