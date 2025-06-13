import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

# Set custom page config
st.set_page_config(
    page_title="StockPark (earnGlad)",
    page_icon="📈",
    layout="centered"
)

# Inject CSS for background and style
st.markdown("""
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1611971261374-601b3fba07ae?auto=format&fit=crop&w=1470&q=80');
        background-size: cover;
        background-attachment: fixed;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
    }
    label, input, .stButton>button {
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Start main UI box
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("📊 StockPark (earnGlad)")
st.markdown("#### Predicting the S&P 500 with smart indicators 🧠💸")
st.markdown("---")

# Feature names
feature_labels = [
    "Open Price",
    "High Price",
    "Low Price",
    "Close Price (Previous Day)",
    "Volume",
    "Relative Strength Index (RSI)",
    "Exponential Moving Average (EMA 10)",
    "Simple Moving Average (SMA 50)",
    "MACD",
    "Volatility Index (VIX)"
]

# Input layout
st.markdown("### 🔢 Enter market indicators:")
input_features = []
cols = st.columns(2)

for i, label in enumerate(feature_labels):
    with cols[i % 2]:
        val = st.number_input(label, value=0.0, format="%.4f")
        input_features.append(val)

# Prediction button
if st.button("🎯 Predict"):
    input_array = np.array([input_features])
    prediction = model.predict(input_array)[0]
    result = "📈 Price will go UP" if prediction == 1 else "📉 Price will go DOWN"

    st.markdown("---")
    st.success(f"🚀 Prediction: **{result}**", icon="✅")
    st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

   

