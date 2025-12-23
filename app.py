import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# -----------------------------------------------------------------------------
# 1. PAGE SETUP
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Digital Control Centre",
    page_icon="🎛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. THEME LOGIC (Light vs Dark)
# -----------------------------------------------------------------------------
# Check current theme in session state
if 'theme' not in st.session_state:
    st.session_state.theme = 'Light' # Default is Light as per your request

# Sidebar Toggle Logic
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/906/906343.png", width=40)
    st.markdown("### ⚙️ View Settings")
    
    # Toggle Button
    theme_selection = st.radio(
        "Theme Mode:", 
        ["Light", "Dark"], 
        index=0 if st.session_state.theme == 'Light' else 1,
        horizontal=True
    )
    
    # Update state if changed
    if theme_selection != st.session_state.theme:
        st.session_state.theme = theme_selection
        st.rerun() # Force reload to apply CSS

# Define Colors based on Theme
if st.session_state.theme == 'Light':
    main_bg_color = "#F5F7FA" # Soft White/Grey
    text_color = "#021b3d"    # Dark Blue Text
    card_bg = "white"
    card_shadow = "0 4px 6px rgba(0,0,0,0.1)"
    card_border = "#E0E0E0"
    chart_text_color = "black"
else:
    main_bg_color = "#042f66" # Deep Blue
    text_color = "white"
    card_bg = "linear-gradient(145deg, #004080, #003366)"
    card_shadow = "0 4px 8px rgba(0,0,0,0.4)"
    card_border = "#00a8cc"
    chart_text_color = "white"

# -----------------------------------------------------------------------------
# 3. DYNAMIC CSS (Injecting Colors)
# -----------------------------------------------------------------------------
st.markdown(f"""
    <style>
    /* 1. Main Background (Changes based on toggle) */
    .stApp {{
        background-color: {main_bg_color};
        color: {text_color};
    }}

    /* 2. Sidebar Background (ALWAYS BLUE) */
    [data-testid="stSidebar"] {{
        background-color: #021b3d;
        border-right: 2px solid #FFD700;
    }}
    /* Sidebar text always white */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label {{
        color: white !important;
    }}

    /* 3. Top Header Bar (ALWAYS BLUE) */
    .top-bar {{
        background-color: #021b3d;
        padding: 15px 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        border-bottom: 3px solid #00a8cc;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
    .header-title {{
        font-size: 24px;
        font-weight: 900;
        color: white;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }}
    
    /* Pills inside header */
    .header-pill {{
        background-color: rgba(255,255,255,0.1);
        color: white;
        border: 1px solid rgba(255,255,255,0.2);
        padding: 6px 15px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 13px;
    }}

    /* 4. KPI Cards Styling (Dynamic) */
    .kpi-card {{
        background: {card_bg};
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid {card_border};
        box-shadow: {card_shadow};
        margin-bottom: 10px;
        transition: transform 0.2s;
    }}
    .kpi-card:hover {{ transform: translateY(-5px); }}
    
    .kpi-label {{ 
        font-size: 14px; 
        color: {'#666' if st.session_state.theme == 'Light' else '#b0c4de'}; 
        margin-bottom: 5px; 
        text-transform: uppercase; 
        font-weight: bold;
    }}
    .kpi-val {{ 
        font-size: 36px; 
        font-weight: 800; 
        color: {'#021b3d' if st.session_state.theme == 'Light' else 'white'}; 
        margin: 0; 
    }}
    .kpi-arrow {{ color: #00C851; font-size: 14px; font-weight: bold; }}

    /* 5. Headings & Text Colors */
    h1, h2, h3, h4, p {{ color: {text_color} !important; }}
    
    /* Selectbox Styling */
    .stSelectbox div[data-baseweb="select"] > div {{
        background-color: {'white' if st.session_state.theme == 'Light' else '#021b3d'} !important;
        color: {text_color} !important;
        border: 1px solid #ccc;
    }}
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. HEADER SECTION
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
# 5. SIDEBAR MENU (Remaining items)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("---")
    selected = st.radio(
        "Navigate", 
        ["Home Dashboard", "Analytics", "Goals / Targets", "Settings"],
        label_visibility="collapsed"
    )
    st.write("---")
    st.info("System Status: 🟢 Online")

# -----------------------------------------------------------------------------
# 6. DASHBOARD CONTENT
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
        labels=labels, values=values, hole=0.5,
        marker_colors=['#FF4B4B', '#FFD700', '#00A8CC', '#1E90FF']
    )])
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=chart_text_color), # Dynamic Color
        margin=dict(t=20, b=20, l=0, r=0), 
        height=300,
        showlegend=True, 
        legend=dict(orientation="h", y=-0.2)
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Bar Chart (Right)
with col_bar:
    st.markdown("##### Total Growth")
    # Dummy Data
    bar_data = pd.DataFrame({'Day': [1,2,3,4,5,6,7], 'Growth': [10, 15, 8, 22, 18, 25, 30]})
    
    fig_bar = px.bar(bar_data, x='Day', y='Growth')
    # Light Mode mein Blue bars, Dark mode mein Cyan neon bars
    bar_color = '#021b3d' if st.session_state.theme == 'Light' else '#00e5ff'
    
    fig_bar.update_traces(marker_color=bar_color, borderradius=5)
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color=chart_text_color), # Dynamic Color
        margin=dict(t=20, b=20, l=0, r=0), 
        height=300,
        xaxis=dict(showgrid=False), 
        yaxis=dict(showgrid=True, gridcolor='#eee' if st.session_state.theme == 'Light' else '#333')
    )
    st.plotly_chart(fig_bar, use_container_width=True)
