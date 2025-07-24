import streamlit as st
import pickle
import numpy as np

# Load the model
with open('calories_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Custom CSS styling (unchanged colors)
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #f8ffae, #43c6ac);
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
        }

        h1 {
            text-align: center;
            color: #003366;
            padding-bottom: 20px;
        }

        .stNumberInput > div > div > input {
            background-color: #ffffff !important;
            color: #000 !important;
        }

        div.stButton > button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            padding: 0.5em 2em;
            font-size: 16px;
            font-weight: bold;
            transition: 0.3s;
        }

        div.stButton > button:hover {
            background-color: #105a8d;
            color: #fff;
        }

        .stAlert {
            border-radius: 10px;
            background-color: #dff0d8;
            color: #3c763d;
            font-size: 18px;
        }

        label {
            font-weight: bold;
            font-size: 15px;
        }

    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🔥 Calories Burned Prediction App 💪")

st.markdown("#### 🏃‍♂️ Enter your workout details below to estimate your burn! 🥵")

# UI Layout with Columns
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("👤 Gender", ["Male", "Female"])
    age = st.number_input("🎂 Age", min_value=1, max_value=120, value=25)
    height = st.number_input("📏 Height (in cm)", min_value=50, max_value=250, value=170)
    body_temp = st.number_input("🌡️ Body Temperature (°C)", min_value=30.0, max_value=45.0, value=37.0)

with col2:
    weight = st.number_input("⚖️ Weight (in kg)", min_value=10, max_value=200, value=70)
    duration = st.number_input("⏱️ Workout Duration (in minutes)", min_value=1, max_value=300, value=30)
    heart_rate = st.number_input("❤️ Heart Rate (bpm)", min_value=40, max_value=200, value=80)

# Encode gender
gender_encoded = 1 if gender == "Male" else 0

# Prediction
if st.button("⚡ Predict Calories Burned"):
    features = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])
    try:
        calories = model.predict(features)[0]
        st.success(f"🔥 Estimated Calories Burned: **{calories:.2f} kcal** 🏋️‍♀️")
    except Exception as e:
        st.error(f"🚫 An error occurred: {e}")
