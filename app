import streamlit as st
import requests

st.set_page_config(
    page_title="Smart Energy Auditor",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Smart Energy Auditor")

st.markdown("""
### Smart Energy Management System
Calculate electricity consumption
and estimate solar energy requirements.
""")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose a page",
    ["Home", "Energy Calculator", "Solar Estimator"]
)

if page == "Home":
    st.header("Welcome!")
    st.write("Monitor and analyze your energy consumption.")

elif page == "Energy Calculator":
    st.header("Electricity Consumption Calculator")

    power = st.number_input(
        "Device Power (Watts)", min_value=0
    )

    hours = st.number_input(
        "Operating Hours per Day",
        min_value=0.0,
        max_value=24.0
    )

    if st.button("Calculate"):
        daily = power * hours / 1000
        monthly = daily * 30

        st.metric("Daily Consumption", f"{daily:.2f} kWh")
        st.metric("Monthly Consumption", f"{monthly:.2f} kWh")

elif page == "Solar Estimator":
    st.header("Solar Energy Estimator")

    daily_usage = st.number_input(
        "Daily Energy Consumption (kWh)",
        min_value=0.0
    )

    sunlight = st.number_input(
        "Peak Sun Hours",
        min_value=1.0,
        value=5.0
    )

    efficiency = 0.80

    if st.button("Estimate Solar System"):
        required_capacity = daily_usage / (sunlight * efficiency)

        st.success(
            f"Required Solar Capacity: {required_capacity:.2f} kW"
        )
