import streamlit as st
import joblib
import numpy as np

# Load the trained model using joblib
model = joblib.load("model.pkl")

# Page configuration
st.set_page_config(page_title="StockPark (earnGlad)", layout="centered")
st.title("📊 StockPark (earnGlad)")
st.subheader("S&P 500 Movement Predictor")

# Input features (example – update as per your model’s needs)
st.markdown("### Enter input features:")
feature1 = st.number_input("Feature 1 (e.g., Previous Close)", value=0.0)
feature2 = st.number_input("Feature 2 (e.g., RSI)", value=0.0)
feature3 = st.number_input("Feature 3 (e.g., MACD)", value=0.0)
# Add/remove inputs as required by your model

# Prediction
if st.button("Predict"):
    input_data = np.array([[feature1, feature2, feature3]])  # Adjust dimensions accordingly
    prediction = model.predict(input_data)[0]
    result = "📈 Price will go UP" if prediction == 1 else "📉 Price will go DOWN"
    st.success(f"Prediction: {result}")
