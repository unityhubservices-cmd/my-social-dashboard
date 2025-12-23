import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# -----------------------------------------------------------------------------
# 1. PYTHON LOGIC (Backend - Yahan Data Process Hoga)
# -----------------------------------------------------------------------------
st.set_page_config(layout="wide", page_title="Control Centre")

# Yahan aap Python ka koi bhi jadoo kar sakte hain (API call, Database, AI)
current_time = datetime.now().strftime("%I:%M %p | %d %b")
total_earnings = 500
total_views = "14.6 K"
total_subs = "7.93 K"

# Python Logic for Charts
labels = ['YouTube', 'Pinterest', 'Facebook', 'Blogger']
values = [45, 25, 20, 10]
fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5, 
    marker_colors=['#FF4B4B', '#FFD700', '#00A8CC', '#1E90FF'])])
fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
    font=dict(color='white'), margin=dict(t=0, b=0, l=0, r=0), height=250, showlegend=False)

fig_bar = px.bar(x=[1,2,3,4,5], y=[10,15,8,22,18])
fig_bar.update_traces(marker_color='#00e5ff')
fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
    font=dict(color='white'), margin=dict(t=0, b=0, l=0, r=0), height=250, xaxis=dict(showgrid=False), yaxis=dict(gridcolor='#333'))


# -----------------------------------------------------------------------------
# 2. HTML & CSS DESIGN (Frontend - Full Control)
# -----------------------------------------------------------------------------
# Dekhein kaise maine Python variables ({current_time}, {total_earnings}) ko HTML mein ghusaya hai
html_code = f"""
<style>
    /* Aapka Custom CSS - Jahan marzi pixel set karein */
    .main-container {{
        background-color: #042f66;
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-family: sans-serif;
    }}
    .header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #021b3d;
        padding: 15px;
        border-radius: 10px;
        border-bottom: 3px solid #00a8cc;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}
    .title {{ font-size: 24px; font-weight: 900; letter-spacing: 1px; }}
    .pill {{ background: rgba(255,255,255,0.1); padding: 5px 15px; border-radius: 20px; font-size: 13px; }}
    
    /* KPI Cards Styling */
    .grid-container {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 20px;
        margin-bottom: 20px;
    }}
    .card {{
        background: linear-gradient(145deg, #004080, #003366);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #00a8cc;
        box-shadow: 0 4px 8px rgba(0,0,0,0.4);
    }}
    .card:hover {{ transform: translateY(-5px); transition: 0.3s; }}
    .card h3 {{ color: #b0c4de; font-size: 14px; text-transform: uppercase; margin: 0; }}
    .card h1 {{ color: white; font-size: 36px; font-weight: 800; margin: 10px 0; }}
    .arrow {{ color: #00ff00; font-weight: bold; font-size: 14px; }}

</style>

<div class="main-container">
    <div class="header">
        <div class="title">DIGITAL CONTROL CENTRE</div>
        <div style="display: flex; gap: 10px;">
            <div class="pill">💡 Hustle Hard</div>
            <div class="pill">🕒 {current_time}</div> </div>
    </div>

    <div class="grid-container">
        <div class="card">
            <h3>Total Earnings</h3>
            <h1>${total_earnings}</h1> <span class="arrow">⬆ $50 Today</span>
        </div>
        <div class="card">
            <h3>Total Views</h3>
            <h1>{total_views}</h1> <span class="arrow">⬆ +1.2K New</span>
        </div>
        <div class="card">
            <h3>Total Followers</h3>
            <h1>{total_subs}</h1> <span class="arrow">⬆ +120 Subs</span>
        </div>
    </div>
</div>
"""

# -----------------------------------------------------------------------------
# 3. RENDERING (Milaap)
# -----------------------------------------------------------------------------

# 1. Pehle Background set karein
st.markdown("""
    <style>
        .stApp { background-color: #042f66; } /* Background Color Fix */
        .block-container { padding-top: 1rem; padding-bottom: 0rem; } /* Padding remove */
        header { visibility: hidden; } /* Streamlit ka default header chupana */
    </style>
""", unsafe_allow_html=True)

# 2. Sidebar (Streamlit ka hi use karein kyunke wo functional hai)
with st.sidebar:
    st.title("Admin Panel")
    st.radio("Menu", ["Dashboard", "Analytics", "Settings"])

# 3. Apna HTML Design Render karein
st.markdown(html_code, unsafe_allow_html=True)

# 4. Charts (HTML mein Charts banana mushkil hai, isliye Charts hum Streamlit ke use karenge)
# Hum Columns bana kar charts ko HTML ke neeche adjust kar denge
c1, c2 = st.columns([1, 2])
with c1:
    st.markdown("<h3 style='color:white; text-align:center;'>Audience Split</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig_pie, use_container_width=True)
with c2:
    st.markdown("<h3 style='color:white; text-align:center;'>Growth Trend</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig_bar, use_container_width=True)
