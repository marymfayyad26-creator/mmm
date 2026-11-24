import streamlit as st

from energy import calculate_energy, calculate_cost
from solar import calculate_solar_capacity, calculate_panel_count

st.set_page_config(
    page_title="Smart Energy Auditor",
    page_icon="⚡",
    layout="centered"
)

st.title("⚡ Smart Energy Auditor")
st.write("Analyze your electricity consumption and explore solar energy solutions.")

page = st.sidebar.selectbox(
    "Choose a tool",
    ["Home", "Energy Calculator", "Solar Estimator"]
)

if page == "Home":
    st.header("Welcome!")
    st.write("Use this application to estimate your electricity consumption and solar energy needs.")

elif page == "Energy Calculator":
    st.header("Electricity Consumption Calculator")

    power = st.number_input("Device Power (Watts)", min_value=0.0, value=100.0)
    hours = st.number_input("Daily Operating Hours", min_value=0.0, max_value=24.0, value=5.0)
    days = st.number_input("Number of Days", min_value=1, max_value=31, value=30)
    price = st.number_input("Electricity Price per kWh", min_value=0.0, value=1.0)

    if st.button("Calculate Energy"):
        energy = calculate_energy(power, hours, days)
        cost = calculate_cost(energy, price)

        st.success(f"Monthly Energy Consumption: {energy:.2f} kWh")
        st.info(f"Estimated Electricity Cost: {cost:.2f}")

elif page == "Solar Estimator":
    st.header("Solar Panel Estimator")

    daily_usage = st.number_input("Daily Energy Usage (kWh)", min_value=0.0, value=5.0)
    sunlight = st.number_input("Peak Sunlight Hours", min_value=0.1, max_value=12.0, value=5.0)
    panel_watt = st.number_input("Solar Panel Power (Watts)", min_value=1, value=500)

    if st.button("Estimate Solar System"):
        capacity = calculate_solar_capacity(daily_usage, sunlight)
        panels = calculate_panel_count(capacity, panel_watt)

        st.success(f"Required Solar Capacity: {capacity:.2f} kW")
        st.info(f"Estimated Number of Panels: {panels}")
