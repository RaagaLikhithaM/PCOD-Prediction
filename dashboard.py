## Dashboard using Streamlit
import streamlit as st
import pickle
import numpy as np

# Load the saved model
model_path = r"C:\Users\drraa\PCOD project\best_model.pkl"  # Use raw string or double backslashes
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Dashboard Title
st.title("PCOS Prediction Dashboard")

# Introduction
st.write("""This dashboard predicts the likelihood of Polycystic Ovary Syndrome (PCOS) based on patient symptoms and medical data.
Please input the required details to get a prediction.
""")

# Patient Input Fields
st.header("Input Patient Data")
overweight = st.selectbox("Overweight (1 for Yes, 0 for No)", [1, 0])
always_tired = st.selectbox("Always Tired (1 for Yes, 0 for No)", [1, 0])
irregular_periods = st.selectbox("Irregular or Missed Periods (1 for Yes, 0 for No)", [1, 0])
cycle_length = st.slider("Cycle Length (days)", min_value=1, max_value=50, value=28)
hair_growth = st.selectbox("Hair Growth on Chin (1 for Yes, 0 for No)", [1, 0])
difficulty_conceiving = st.selectbox("Difficulty in Conceiving (1 for Yes, 0 for No)", [1, 0])
acne = st.selectbox("Acne or Skin Tags (1 for Yes, 0 for No)", [1, 0])

# Composite Features
symptom_severity_score = overweight + irregular_periods + hair_growth + acne + always_tired
interaction_term = overweight * cycle_length

# Create the feature array
features = np.array([
    overweight, always_tired, irregular_periods, cycle_length, hair_growth,
    difficulty_conceiving, acne, symptom_severity_score, interaction_term
]).reshape(1, -1)

# Predict the Output
if st.button("Predict"):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]  # Probability of PCOS

    # Display Results
    st.subheader("Prediction Result")
    st.write("**PCOS Detected**" if prediction == 1 else "**No PCOS Detected**")
    st.subheader("Prediction Probability")
    st.write(f"Probability of PCOS: **{probability:.2f}**")

    # Additional Insights
    st.markdown("### Insights")
    if prediction == 1:
        st.write("""
        - PCOS Detected. Please consult a healthcare provider for further evaluation.
        - Consider lifestyle modifications such as regular exercise and a healthy diet.
        """)
    else:
        st.write("No PCOS detected based on the provided data. Maintain a healthy lifestyle.")

# Footer Section
st.markdown("---")
st.markdown("#### Developed by Raaga Likhitha")
st.markdown("For any issues or suggestions, contact: [dr.raagalikhitha@gmail.com](mailto:dr.raagalikhitha@gmail.com)")
