import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('insurancemodelf.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Insurance Premium Predictor", page_icon="💡", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        h1 {
            color: #2C3E50;
            text-align: center;
        }
        .stButton>button {
            background-color: #2C3E50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #1ABC9C;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💡 Medical Insurance Premium Predictor")

st.write("### Enter customer details below to predict insurance charges:")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=100, value=30)
    bmi = st.number_input("BMI i.e Weight / Square of Height", min_value=10.0, max_value=60.0, value=25.0)
    children = st.number_input("Children", min_value=0, max_value=10, value=0)

with col2:
    sex = st.selectbox("Sex", ["Male", "Female"])   # dropped in backend
    smoker = st.selectbox("Smoker", ["Yes", "No"])
    region = st.selectbox("Region", ["NorthWest", "NorthEast", "SouthEast", "SouthWest"])  # dropped in backend

# Preprocess input to match backend features
input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "smoker": [1 if smoker == "Yes" else 0]
})

# Predict button
st.markdown("---")
if st.button("🔮 Predict Premium"):
    prediction = model.predict(input_data)
    st.success(f"### 💰 Predicted Insurance Premium: ₹{prediction[0]:,.2f}")
    