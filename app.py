import streamlit as st
import pandas as pd
import numpy as np

# Page ka Setup (Tab ka naam aur layout)
st.set_page_config(page_title="Social Media Empire", layout="wide", page_icon="🚀")

# Title aur Header
st.title("🔥 My Social Media Command Center")
st.markdown("### Real-time Growth Tracker")

# 3 Dabbay (Metrics) - Yeh woh Shashka hai
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="YouTube Subs", value="12,450", delta="50 Today")
with col2:
    st.metric(label="Instagram Followers", value="5,230", delta="-12")
with col3:
    st.metric(label="FB Page Likes", value="8,900", delta="120 Today")
with col4:
    st.metric(label="Pinterest Views", value="1.2M", delta="5% Up")

# Chart ka Shashka (Abhi fake data hai)
st.write("---")
st.subheader("📈 Audience Growth Trend")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['YouTube', 'Instagram', 'Facebook'])
st.line_chart(chart_data)

# Sidebar (Side wala menu)
st.sidebar.header("Settings")
st.sidebar.write("Last updated: Just Now")
st.sidebar.button("Refresh Data 🔄")
