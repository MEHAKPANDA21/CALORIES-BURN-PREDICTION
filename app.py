import streamlit as st
import pickle
import numpy as np

# Load the model
with open('calories_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Custom Gen Z-style CSS with background image and modern glassmorphism
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

        .stApp {
            background: url('https://cdn.wallpapersafari.com/53/58/QhXCN0.jpg') no-repeat center center fixed;
            background-size: cover;
            font-family: 'Poppins', sans-serif;
            color: #ffffff;
        }

        h1 {
            text-align: center;
            color: #ffffff;
            padding-bottom: 20px;
            font-weight: 800;
            text-shadow: 2px 2px 4px #000;
        }

        .css-1cpxqw2 {
            background: rgba(255, 255, 255, 0.15) !important;
            backdrop-filter: blur(10px) !important;
            border-radius: 15px !important;
            padding: 2em !important;
            margin: 1em 0 !important;
            color: #ffffff !important;
        }

        label, .stSelectbox label, .stNumberInput label {
            font-size: 1rem;
            font-weight: 600;
            color: #ffffff;
        }

        input {
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #000000 !important;
    border-radius: 10px !important;
}


        div.stButton > button {
            background-image: linear-gradient(to right, #ff416c, #ff4b2b);
            color: white;
            border-radius: 12px;
            padding: 0.75em 2em;
            font-size: 1rem;
            font-weight: bold;
            border: none;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }

        div.stButton > button:hover {
            transform: scale(1.05);
            background-image: linear-gradient(to right, #ff4b2b, #ff416c);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }

        .stAlert {
    border-radius: 12px;
    background-color: rgba(0, 255, 128, 0.2);
    color: #00ffcc;  /* Bright & visible on dark bg */
    font-size: 18px;
    font-weight: 700;
    text-align: center;
    padding: 1em;
    backdrop-filter: blur(6px);
}


        .css-1v0mbdj, .css-1x8cf1d {
            color: #ffffff !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🔥 Calories Burned Prediction App 💪")

st.markdown("#### 🏃‍♂️ Enter your workout details below to estimate your burn! 🥵")

# UI Layout
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
        

