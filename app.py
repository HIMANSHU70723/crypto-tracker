import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title(" Cryptocurrency Liquidity Prediction")

st.markdown("""
This app predicts **cryptocurrency liquidity ratio** using:
- Moving Averages (7-day, 14-day)
- Price Volatility
- Trading Liquidity Ratio
""")

# Input fields
ma7 = st.number_input(" 7-day Moving Average", min_value=0.0, format="%.4f")
ma14 = st.number_input(" 14-day Moving Average", min_value=0.0, format="%.4f")
volatility = st.number_input("Volatility (7-day Std Dev)", min_value=0.0, format="%.4f")
liquidity_input = st.number_input("Liquidity Ratio (Volume / (High - Low))", min_value=0.0, format="%.4f")

# Predict button
if st.button("Predict Liquidity"):
    input_features = np.array([[ma7, ma14, volatility, liquidity_input]])
    prediction = model.predict(input_features)[0]
    st.success(f" Predicted Liquidity Ratio: {prediction:.6f}")
