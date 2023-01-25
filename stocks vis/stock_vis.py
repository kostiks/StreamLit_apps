import yfinance as yf
import streamlit as st
import pandas as pd
import cufflinks as cf
import datetime


st.write("""
# Приложение для просмотра цены акций

Выдача данных по запросу **определенной** компании

**Описание**
- Создание приложения [https://github.com/kostiks]
- С использованием библиотек:  ***streamlit,  yfinance,  datetime,  pandas***

""")


ticker_list = pd.read_csv ('/Users/margaritagordon/projects/streamlit/stocks vis/data/stock_symbols.txt')
ticker_Symbol = st.selectbox('Компания', ticker_list)
start_date = st.date_input('Начало', datetime.date(2019, 1, 1))
end_date = st.date_input('Конец', datetime.date(2022,12,31))
tickerData = yf.Ticker(ticker_Symbol)
tickerDf = tickerData.history(period='1mo', start=start_date, end=end_date)


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.header('**Ticker data**')
st.write(tickerDf)




