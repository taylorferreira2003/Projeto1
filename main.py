import streamlit as st
import pandas as pd
import yfinance as yf
 
# criar as funções de carregamento de dados
    # cotações do Itaú - ITUB4 - 2010 a 2025
@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(start="2010-01-01", end="2025-12-01")
    cotacoes_acao = cotacoes_acao[["Close"]]
    return cotacoes_acao

# prepara as visualizações
dados = carregar_dados("ITUB4.SA")
print(dados)


# criar a interface do streamlit
st.title("Análise de Cotações do Itaú (ITUB4)")

#criar o grafico
st.line_chart(dados)

st.write("""##### Este aplicativo exibe as cotações históricas do Itaú (ITUB4) de 2010 a 2025.""")