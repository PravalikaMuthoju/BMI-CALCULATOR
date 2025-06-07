import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.title("⚖️ Body Mass Index (BMI) Calculator")

st.write("Calculate your BMI by entering your height in centimeters and weight in kilograms.")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=160.0, step=0.1, help="Enter your height in centimeters")
with col2:
    weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=55.0, step=0.1, help="Enter your weight in kilograms")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        bmi_rounded = round(bmi, 2)

        # Display BMI value
        st.markdown(f"### Your BMI is: <span style='color:blue'>{bmi_rounded}</span>", unsafe_allow_html=True)

        # BMI category logic
        if bmi < 18.5:
            category = "Underweight"
            color = "orange"
            tip = "Try to eat a balanced diet and consult a doctor if needed."
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = "green"
            tip = "Great job! Keep maintaining your healthy lifestyle! 💪"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "orange"
            tip = "Consider exercising regularly and watching your diet."
        else:
            category = "Obese"
            color = "red"
            tip = "Please consult a healthcare professional for advice."

        st.markdown(f"### Category: <span style='color:{color}; font-weight:bold'>{category}</span>", unsafe_allow_html=True)
        st.info(tip)
    else:
        st.error("Please enter valid height and weight.")

st.markdown("---")
st.write("**Example inputs:** Height = 160 cm, Weight = 55 kg")
