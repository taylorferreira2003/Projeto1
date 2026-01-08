import streamlit as st
import yfinance as yf

@st.cache_data
def carregar_dados(acoes):
    cotacoes = yf.download(
        tickers=acoes,
        start="2010-01-01",
        end="2025-12-01"
    )
    cotacoes = cotacoes["Close"]  
    return cotacoes

acoes = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA", "VALE3.SA", "ABEV3.SA", "GGBR4.SA"]

dados = carregar_dados(acoes)

st.title("Análise de Cotações das Ações")

lista_acoes = st.multiselect("Escolha as ações para visualizar:", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})
    
st.line_chart(dados)

st.write("##### Este aplicativo exibe as cotações históricas das ações de 2010 a 2025.")
