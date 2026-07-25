import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Eco-Loop Building Agent Dashboard", layout="wide")

st.title("🌱 Eco-Loop Building Agent: Closed-Loop Dashboard")
st.markdown("Real-time monitoring and AI-driven forward injection control for EnergyPlus simulations.")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Zone Temperature", value="24.0 °C", delta="-1.3 °C")
with col2:
    st.metric(label="Energy Consumption", value="13.85 kWh", delta="-0.21 kWh")
with col3:
    st.metric(label="PMV Thermal Comfort", value="0.15", delta="Optimal")
with col4:
    st.metric(label="Carbon Intensity", value="205 g/kWh", delta="-5.5")

st.markdown("---")
st.subheader("📈 Live Performance Metrics Stream")

chart_data = pd.DataFrame({
    'Time Step': ['Step 1', 'Step 2', 'Step 3', 'Step 4', 'Step 5'],
    'Temperature (°C)': [25.5, 25.3, 24.8, 24.3, 24.0],
    'Energy (kWh)': [14.2, 14.06, 13.95, 13.90, 13.85]
})

st.line_chart(chart_data.set_index('Time Step'))

st.markdown("---")
st.subheader("🧠 Cognitive Engine & Forward Injection Status")
st.info("The Llama 3 cognitive engine continuously evaluates zone telemetry via MCP tools and applies automated set-point modifications back to the EnergyPlus model.")
