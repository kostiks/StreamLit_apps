import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import altair as alt
import requests
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_book = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_djwnoxew.json")
st_lottie(lottie_book, speed=2, height=150, key="initial")


tips_df = pd.read_csv ('./data/tips.csv')
tips_df["tip_percentage"] = (tips_df["tip"] / tips_df["total_bill"]) * 100

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (0.1, 2, 0.2, 1, 0.1)
)

row0_1.title("Data Analyze of restuarant tips with defferent types of visualization")


with row0_2:
    add_vertical_space()
    row0_2.subheader(
    """
      A Streamlit web app by [Konstantin G.](https://github.com/kostiks) using:   ***'pandas'*** and ***'altair'***"""
)


st.write("")
row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
    (0.1, 1, 0.1, 2, 0.1)
)

with row3_1:
    st.subheader("Histogram of the total bill")
    add_vertical_space()
    add_vertical_space()
    test = alt.Chart(tips_df).mark_bar().encode(
    alt.X('total_bill',title='Total Bill', bin=alt.Bin(maxbins=30)),
    alt.Y('count()',title='Count'))

    st.altair_chart(test, use_container_width=True)
    st.markdown('The graph makes it clear that the largest number (32) among all accounts is in the range from 16 to 18')

with row3_2:
    st.subheader("Tips and Total bill data based on the day of the week, and the number of dishes")
    res = alt.Chart(tips_df).mark_point(filled=True).encode(
    alt.X('total_bill',title='Total Bill'),
    y='tip', color='day', size='size')
    st.altair_chart(res, use_container_width=True)
    st.markdown('The scatterplot shows the relationship between tips and total bill. The color of the values indicates the day of the week, and the size increases relative to the number of dishes in the order.')
add_vertical_space()
row4_space1, row4_1, row4_space2, row4_2, row4_space3 = st.columns(
    (0.1, 2, 0.1, 1, 0.1)
)

with row4_1:
     st.subheader("Scatterplot of total bill and tips by smokers and non smokers")
     add_vertical_space()
     add_vertical_space()
     res = alt.Chart(tips_df).mark_point(filled=True).encode(
     x="total_bill", 
     y="tip",color='smoker').configure_point(
     size=100) 
     st.altair_chart(res, use_container_width=True)
     st.markdown('''The scatterplot shows the relationship between tips and total bill. The color of the values indicates the category: smoking and non-smoking guests''')
    
with row4_2:
    st.subheader("Amount of tips by day with gender separation")
    res = alt.Chart(tips_df).mark_bar().encode(
    alt.X('day',),
    alt.Y('sum(tip)'), color='sex')
    st.altair_chart(res, use_container_width=True)
    st.markdown('The bar shows data on the amount of tips by day of the week, divided by sex')

add_vertical_space()
row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns(
    (0.1, 1.5, 0.1, 1.5, 0.1)
)
with row5_1:
    st.subheader("Graff of tips depending on time")
    res = alt.Chart(tips_df).mark_bar().encode(
    alt.X('tip_percentage',title='Tip %', bin=alt.Bin(maxbins=20)),
    alt.Y('count()',title='Count'), color='time')
    st.altair_chart(res, use_container_width=True)
    st.markdown('The chart shows the distribution of tips as a percentage depending on the time of visit')
    

with row5_2:
    st.subheader("Distribution of tips depending on gender")
    graph = alt.Chart(tips_df).mark_point(filled=True).encode(
    x='day',
    y='tip', color='sex').configure_point(
    size=100)
    st.altair_chart(graph, use_container_width=True)
    st.markdown('Visualization of tips distribution depending on gender by days of the week')






