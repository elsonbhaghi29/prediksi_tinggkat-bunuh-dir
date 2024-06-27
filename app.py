
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.pkl')

st.title('Suicide Rate Prediction')

# Input dari user
year = st.number_input('Year', min_value=1950, max_value=2018, value=2000)
age_group = st.selectbox('Age Group', ('10-14 years', '15-19 years', '20-24 years', '25-34 years', '35-44 years', '45-54 years', '55-64 years', '65-74 years', '75-84 years', '85 years and over'))

# Mapping age group to numerical value
age_map = {'10-14 years': 1, '15-19 years': 2, '20-24 years': 3, '25-34 years': 4, '35-44 years': 5, '45-54 years': 6, '55-64 years': 7, '65-74 years': 8, '75-84 years': 9, '85 years and over': 10}
age_num = age_map[age_group]

# Prediction
prediction = model.predict([[year, age_num]])
st.write(f'Predicted Suicide Rate: {prediction[0]:.2f} per 100,000 residents')
