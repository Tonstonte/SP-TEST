import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("model.pkl")

# Set page config
st.set_page_config(
    page_title="StockPark (earnGlad)",
    page_icon="📈",
    layout="centered"
)

# Inject custom CSS
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

# UI start
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("📊 StockPark (earnGlad)")
st.markdown("#### Predicting the S&P 500 — one indicator at a time 🧠📈")
st.markdown("---")

# Feature labels
feature_labels = [
    "Open Price", "High Price", "Low Price", "Close Price (Previous Day)",
    "Volume", "Relative Strength Index (RSI)", "Exponential Moving Average (EMA 10)",
    "Simple Moving Average (SMA 50)", "MACD", "Volatility Index (VIX)"
]

### 🎯 Manual Input Prediction
st.markdown("### 🔢 Manual Input:")
input_features = []
cols = st.columns(2)

for i, label in enumerate(feature_labels):
    with cols[i % 2]:
        val = st.number_input(label, value=0.0, format="%.4f")
        input_features.append(val)

if st.button("📍 Predict One"):
    input_array = np.array([input_features])
    prediction = model.predict(input_array)[0]
    result = "📈 Price will go UP" if prediction == 1 else "📉 Price will go DOWN"
    st.success(f"🚀 Prediction: **{result}**", icon="✅")
    st.balloons()

st.markdown("---")

### 📁 CSV Upload Section
st.markdown("### 📂 Batch Upload via CSV")
uploaded_file = st.file_uploader("Upload a CSV with the 10 required indicators", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        if df.shape[1] != 10:
            st.error("❌ CSV must have exactly 10 columns (features).")
        else:
            predictions = model.predict(df)
            df["Prediction"] = ["UP" if p == 1 else "DOWN" for p in predictions]
            st.success("✅ Predictions completed!")

            st.dataframe(df.head())

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="stockpark_predictions.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Error processing file: {e}")

st.markdown("</div>", unsafe_allow_html=True)


]

 
