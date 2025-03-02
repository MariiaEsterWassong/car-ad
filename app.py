import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

df = df.dropna(subset=['price', 'odometer', 'model_year', 'fuel', 'condition'])

st.sidebar.header('Filters')
selected_fuel = st.sidebar.multiselect('Select fuel type(s)', df['fuel'].unique(), default=df['fuel'].unique())
selected_condition = st.sidebar.multiselect('Select condition(s)', df['condition'].unique(), default=df['condition'].unique())

filtered_df = df[(df['fuel'].isin(selected_fuel)) & (df['condition'].isin(selected_condition))]

st.header('Dataset Overview')
st.write(filtered_df.describe())

st.header('Distribution of Car Prices')
fig_price = px.histogram(filtered_df, x='price', nbins=50, color_discrete_sequence=['blue'])
st.plotly_chart(fig_price)

st.header('Distribution of Odometer Readings')
fig_odometer = px.histogram(filtered_df, x='odometer', nbins=50, color_discrete_sequence=['blue'])
st.plotly_chart(fig_odometer)

st.header('Price vs. Odometer')
fig_scatter = px.scatter(filtered_df, x='odometer', y='price', opacity=0.5, trendline='ols', color_discrete_sequence=['blue'])
st.plotly_chart(fig_scatter)

st.header('Price Distribution by Condition')
fig_condition = px.box(filtered_df, x='condition', y='price', color='condition')
st.plotly_chart(fig_condition)

st.header('Average Price by Fuel Type')
fuel_avg_price = filtered_df.groupby('fuel')['price'].mean().reset_index()
fig_fuel = px.bar(fuel_avg_price, x='fuel', y='price', color_discrete_sequence=['blue'])
st.plotly_chart(fig_fuel)

st.header('Car Price vs Model Year')
fig_year_price = px.scatter(filtered_df, x='model_year', y='price', opacity=0.5, trendline='ols', color_discrete_sequence=['blue'])
st.plotly_chart(fig_year_price)

if st.checkbox('Show raw data'):
    st.write(filtered_df)
