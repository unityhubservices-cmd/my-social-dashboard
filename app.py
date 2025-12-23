import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# -----------------------------------------------------------------------------
# 1. PAGE SETUP (Must be the first command)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Digital Control Centre",
    page_icon="🎛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. DESIGN ENGINE (CSS for Navy Blue Theme)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* 1. Main Background - Deep Navy Blue */
    .stApp {
        background-color: #042f66;
        color: white;
    }

    /* 2. Sidebar Background */
    [data-testid="stSidebar"] {
        background-color: #021b3d;
        border-right: 2px solid #FFD700; /* Gold Line */
    }

    /* 3. Top Header Bar */
    .top-bar {
        background-color: #021b3d;
        padding: 15px 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        border-bottom: 2px solid #00a8cc; /* Cyan Line */
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .header-title {
        font-size: 22px;
        font-weight: 900;
        color: white;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    .header-pill {
        background-color: white;
        color: #042f66;
        padding: 6px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 13px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }

    /* 4. KPI Cards Styling */
    .kpi-card {
        background: linear-gradient(145deg, #004080, #003366);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #00a8cc;
        box-shadow: 0 4px 8px rgba(0,0,0,0.4);
        margin-bottom: 10px;
    }
    .kpi-label { font-size: 14px; color: #b0c4de; margin-bottom: 5px; text-transform: uppercase; }
    .kpi-val { font-size: 36px; font-weight: 800; color: white; margin: 0; }
    .kpi-arrow { color: #00ff00; font-size: 14px; font-weight: bold; }

    /* 5. General Text Fixes */
    h1, h2, h3, p, label { color: white !important; }
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #021b3d !important;
        color: white !important;
        border: 1px solid #00a8cc;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. TOP HEADER (Title + Time)
# -----------------------------------------------------------------------------
current_time = datetime.now().strftime("%I:%M %p | %d %b")

st.markdown(f"""
    <div class="top-bar">
        <div class="header-title">Digital Control Centre</div>
        <div style="display: flex; gap: 10px;">
            <div class="header-pill">💡 Hustle Hard</div>
            <div class="header-pill">🕒 {current_time}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. SIDEBAR MENU
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 👤 Admin Panel")
    selected = st.radio(
        "Navigate", 
        ["Home Dashboard", "Analytics", "Goals / Targets", "Settings"],
        label_visibility="collapsed"
    )
    st.write("---")
    st.info("System Status: 🟢 Online")

# -----------------------------------------------------------------------------
# 5. DASHBOARD CONTENT
# -----------------------------------------------------------------------------

# Filters Row
c1, c2, c3 = st.columns([3, 1, 1])
with c1:
    st.subheader("Monthly Stats Dashboard")
with c2:
    st.selectbox("Platform", ["All Platforms", "YouTube", "Instagram"], label_visibility="collapsed")
with c3:
    st.selectbox("Duration", ["This Month", "Last Month"], label_visibility="collapsed")

# KPI Cards Row
k1, k2, k3 = st.columns(3)

def kpi(title, val, growth):
    return f"""
    <div class="kpi-card">
        <div class="kpi-label">{title}</div>
        <div class="kpi-val">{val}</div>
        <div class="kpi-arrow">⬆ {growth}</div>
    </div>
    """

with k1:
    st.markdown(kpi("Total Earnings", "$500", "$50 Today"), unsafe_allow_html=True)
with k2:
    st.markdown(kpi("Total Views", "14.6 K", "+1.2K New"), unsafe_allow_html=True)
with k3:
    st.markdown(kpi("Total Followers", "7.93 K", "+120 Subs"), unsafe_allow_html=True)

st.write("---")

# Charts Row
col_pie, col_bar = st.columns([1, 2])

# Pie Chart (Left)
with col_pie:
    st.markdown("##### Audience Split")
    labels = ['YouTube', 'Pinterest', 'Facebook', 'Blogger']
    values = [45, 25, 20, 10]
    fig_pie = go.Figure(data=[go.Pie(
        labels=labels, values=values, hole=0,
        marker_colors=['#FF4B4B', '#FFD700', '#00A8CC', '#1E90FF']
    )])
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'), margin=dict(t=0, b=0, l=0, r=0), height=300,
        showlegend=True, legend=dict(orientation="h", y=-0.1)
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Bar Chart (Right)
with col_bar:
    st.markdown("##### Total Growth (Cyan Mode)")
    # Dummy Data
    bar_data = pd.DataFrame({'Day': [1,2,3,4,5,6,7], 'Growth': [10, 15, 8, 22, 18, 25, 30]})
    fig_bar = px.bar(bar_data, x='Day', y='Growth')
    fig_bar.update_traces(marker_color='#00e5ff') # Cyan Neon Color
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'), margin=dict(t=0, b=0, l=0, r=0), height=300,
        xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='#333')
    )
    st.plotly_chart(fig_bar, use_container_width=True)
