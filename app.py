import streamlit as st
from fuzzy_logic import get_irrigation_level

st.set_page_config(page_title="Fuzzy Irrigation System", layout="centered")

st.title("🌱 Fuzzy Logic Irrigation Decision System")
st.write("This system determines optimal irrigation levels using fuzzy logic.")

soil = st.slider("Soil Moisture (%)", 0, 100, 40)
temp = st.slider("Temperature (°C)", 0, 50, 25)
hum = st.slider("Humidity (%)", 0, 100, 50)

if st.button("Calculate Irrigation Level"):
    result = get_irrigation_level(soil, temp, hum)

    st.success(f"Irrigation Level: {result:.2f}%")

    if result < 40:
        st.info("Recommended Level: LOW ")
    elif result < 70:
        st.warning("Recommended Level: MEDIUM ")
    else:
        st.error("Recommended Level: HIGH ")
