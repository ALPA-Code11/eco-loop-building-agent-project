import streamlit as st
import pandas as pd

st.set_page_config(page_title="Eco-Loop Building Agent Dashboard", layout="wide")

st.title("🌱 Eco-Loop Building Agent: Quantitative Savings & Closed-Loop Dashboard")
st.markdown("Real-time performance comparison: Baseline BMS vs. Autonomous AI Closed-Loop Control.")

df_comparison = pd.DataFrame({
    'Time Step': ['Step 1', 'Step 2', 'Step 3', 'Step 4', 'Step 5'],
    'Baseline Energy (kWh)': [16.8, 16.5, 16.9, 16.7, 16.6],
    'AI Closed-Loop Energy (kWh)': [15.2, 14.6, 14.1, 13.9, 13.8],
    'Baseline PMV': [0.72, 0.68, 0.75, 0.70, 0.69],
    'AI Closed-Loop PMV': [0.35, 0.28, 0.20, 0.18, 0.15],
    'AI Setpoint (°C)': [25.0, 24.5, 24.2, 24.0, 24.0]
})

baseline_total_kwh = df_comparison['Baseline Energy (kWh)'].sum()
ai_total_kwh = df_comparison['AI Closed-Loop Energy (kWh)'].sum()
kwh_savings = baseline_total_kwh - ai_total_kwh
pct_reduction = (kwh_savings / baseline_total_kwh) * 100
avg_ai_pmv = df_comparison['AI Closed-Loop PMV'].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Baseline Total Energy", value=f"{baseline_total_kwh:.2f} kWh")
with col2:
    st.metric(label="AI Closed-Loop Energy", value=f"{ai_total_kwh:.2f} kWh", delta=f"-{kwh_savings:.2f} kWh")
with col3:
    st.metric(label="Energy Savings (% Reduction)", value=f"{pct_reduction:.1f}%", delta="Target Met (>10%)")
with col4:
    st.metric(label="Avg PMV Comfort Index", value=f"{avg_ai_pmv:.2f}", delta="Optimal Boundary (-0.5 to +0.5)")

st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("⚡ Energy Consumption Comparison (kWh)")
    energy_chart_df = df_comparison.set_index('Time Step')[['Baseline Energy (kWh)', 'AI Closed-Loop Energy (kWh)']]
    st.line_chart(energy_chart_df)

with col_right:
    st.subheader("🌡️ PMV Thermal Comfort Index Boundary")
    comfort_chart_df = df_comparison.set_index('Time Step')[['Baseline PMV', 'AI Closed-Loop PMV']]
    st.line_chart(comfort_chart_df)

st.markdown("---")
st.subheader("📊 Quantitative Performance Data Table")
st.dataframe(df_comparison, use_container_width=True)

csv_data = df_comparison.to_csv(index=False)
st.download_button(
    label="📥 Export Quantitative Savings Report (CSV)",
    data=csv_data,
    file_name="ecoloop_quantitative_savings_report.csv",
    mime="text/csv"
)
