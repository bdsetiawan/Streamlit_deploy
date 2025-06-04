import streamlit as st
import joblib
import numpy as np

# Load the AI model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.title("Simple AI Prediction App")

input_val = st.number_input("Enter a number to predict", value=0)

if st.button("Predict"):
    prediction = model.predict(np.array([[input_val]]))
    st.success(f"Prediction: {prediction[0]}")