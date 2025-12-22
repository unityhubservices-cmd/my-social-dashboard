import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config (Sabse pehle)
st.set_page_config(page_title="Analytics Pro", layout="wide", page_icon="⚡")

# 2. Custom CSS (Yeh hai wo makeup jo design badlega)
st.markdown("""
    <style>
    /* Pure page ka background dark grey/black */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Metrics wale dabbo ka design (Glassmorphism Effect) */
    div[data-testid="metric-container"] {
        background-color: #262730;
        border: 1px solid #3b3c45;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
        transition: transform 0.2s;
    }
    
    /* Hover karne par dabbe thode uth jayenge */
    div[data-testid="metric-container"]:hover {
        transform: scale(1.02);
        border: 1px solid #ff4b4b;
    }

    /* Text Colors */
    h1, h2, h3 {
        color: white !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Chart ka background transparent */
    div[data-testid="stChart"] {
        background-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section
st.title("⚡ Ultra-Stats Command Center")
st.markdown("<h4 style='color: #808495;'>Live Performance Overview</h4>", unsafe_allow_html=True)
st.write("---")

# 4. KPI Row (Top Stats)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="YouTube Subs", value="14.2K", delta="🔥 +120 Today")
with col2:
    st.metric(label="Instagram Reach", value="45.2K", delta="🚀 +15%")
with col3:
    st.metric(label="Facebook Engmt", value="8,900", delta="-2% (Low)")
with col4:
    st.metric(label="Total Revenue", value="$1,240", delta="💵 +$50")

st.write(" ") # Thora gap

# 5. Charts Section (Side by Side)
c1, c2 = st.columns((2, 1)) # Left wala chart bada, right wala chota

with c1:
    st.subheader("📈 Monthly Growth Trend")
    # Fake Data generate kar rahe hain graph ke liye
    chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['Views', 'Subscribers'])
    st.area_chart(chart_data, color=["#FF4B4B", "#00B4D8"]) # Red and Blue colors

with c2:
    st.subheader("🎯 Audience Split")
    # Pie chart data
    st.bar_chart({"Male": 60, "Female": 35, "Other": 5}, color="#FF4B4B")

# 6. Footer Styles
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>System Status: 🟢 Online | Updated: Just Now</div>", unsafe_allow_html=True)
