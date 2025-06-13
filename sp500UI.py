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

# Title area
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("📊 StockPark (earnGlad)")
st.markdown("#### Predicting the S&P 500 with style 🧠💸")
st.markdown("---")

# Input area
st.markdown("### 🔢 Enter input features:")
input_features = []
cols = st.columns(2)  # 2-column layout

for i in range(10):
    with cols[i % 2]:  # alternate between columns
        val = st.number_input(f"Feature {i + 1}", value=0.0, format="%.4f")
        input_features.append(val)

# Prediction logic
if st.button("🎯 Predict"):
    input_array = np.array([input_features])
    prediction = model.predict(input_array)[0]
    result = "📈 Price will go UP" if prediction == 1 else "📉 Price will go DOWN"

    st.markdown("---")
    st.success(f"🚀 Prediction: **{result}**", icon="✅")
    st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
