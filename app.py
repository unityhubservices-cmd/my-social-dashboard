import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. Page Config ---
st.set_page_config(page_title="Pro Social Dashboard", layout="wide", page_icon="📊")

# --- 2. Custom CSS (Styling & Colors from Reference) ---
st.markdown("""
    <style>
    /* Main Background (Dark) */
    .stApp {
        background-color: #0E1117; /* Dark background for pro feel */
        color: white;
    }
    
    /* Top Navigation Bar (Inspired by Ref Image) */
    .top-nav {
        background-color: #001F5B; /* Dark Blue header */
        padding: 15px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 3px solid #FFD700; /* Gold line separator */
        margin-bottom: 25px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .top-nav .title {
        font-size: 26px;
        font-weight: 800;
        color: white;
        letter-spacing: 1px;
    }
    .top-nav .slogan {
        font-size: 14px;
        color: #E0E0E0;
        text-align: right;
        line-height: 1.4;
    }

    /* Custom Metric Cards Styling */
    .metric-card {
        border-radius: 12px;
        padding: 20px;
        color: white;
        box-shadow: 0 6px 10px -2px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    .metric-card:hover {
        transform: translateY(-7px) scale(1.02);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
    }
    
    /* Card Colors (From Reference Image) */
    .card-blue { background: linear-gradient(145deg, #001F5B, #0044cc); }
    .card-red { background: linear-gradient(145deg, #C0392B, #E74C3C); }
    .card-green { background: linear-gradient(145deg, #27AE60, #2ECC71); }
    .card-yellow { background: linear-gradient(145deg, #F39C12, #F1C40F); color: #fff; }

    .metric-title { font-size: 16px; opacity: 0.9; font-weight: 500; }
    .metric-value { font-size: 32px; font-weight: 900; margin: 10px 0 5px 0; }
    .metric-delta { font-size: 13px; font-weight: 600; }
    .metric-icon { position: absolute; top: 15px; right: 15px; font-size: 24px; opacity: 0.7; }
    
    /* Progress Bar inside Card */
    .progress-container {
        margin-top: 15px;
        background-color: rgba(0,0,0,0.2);
        height: 6px;
        border-radius: 10px;
    }
    .progress-bar {
        height: 6px;
        border-radius: 10px;
        background-color: rgba(255,255,255,0.9);
    }
    .goal-text { font-size: 11px; text-align: right; margin-top: 4px; opacity: 0.8; }

    /* Hide default Streamlit elements */
    div[data-testid="stMetric"] { display: none; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* General Text Styling */
    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: white !important; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    
    /* Form & Table Styling */
    div[data-testid="stForm"] { background-color: #1E2130; padding: 20px; border-radius: 10px; border: 1px solid #3b3c45; }
    .stDataFrame { border: 1px solid #3b3c45; border-radius: 10px; overflow: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header Section (Reference Style) ---
st.markdown("""
    <div class="top-nav">
        <div class="title">📊 SOCIAL PRO DASHBOARD</div>
        <div class="slogan">
            خَيْرُ النَّاسِ مَنْ يَنْفَعُ النَّاسَ<br>
            Logon mein behtareen woh hai jo logon ko faida pohanchaye
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Helper Function to Create Custom Cards ---
def custom_metric(title, value, delta, color_class, icon, progress, goal_txt):
    st.markdown(f"""
        <div class="metric-card {color_class}">
            <div class="metric-icon">{icon}</div>
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-delta">{delta}</div>
            <div class="progress-container">
                <div class="progress-bar" style="width: {progress}%;"></div>
            </div>
             <div class="goal-text">{goal_txt} ({progress}%)</div>
        </div>
        """, unsafe_allow_html=True)

# --- 4. The 4 Pro Cards (With Goals & Progress) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    # Blue Card - YouTube
    custom_metric("YouTube Subscribers", "14,250", "🔥 +120 Today", "card-blue", "▶️", 95, "Goal: 15k")
with col2:
    # Red Card - Instagram
    custom_metric("Instagram Followers", "45,200", "🚀 +300 Today", "card-red", "📸", 90, "Goal: 50k")
with col3:
    # Green Card - Total Views
    custom_metric("Total Views (All Time)", "1.8M", "📈 +50k This Week", "card-green", "👁️", 90, "Goal: 2M")
with col4:
    # Yellow Card - Recent Performance
    custom_metric("Recent Video Views", "8,500", "⭐ Uploaded Yesterday", "card-yellow", "🎬", 85, "Goal: 10k")

st.write("---") # Separator line

# --- 5. New Charts Section ---
c1, c2 = st.columns((2, 1)) # Left column is wider

with c1:
    st.subheader("📈 30-Day Views Trend (YouTube vs Insta)")
    # Generating Fake Data for the Area Chart
    chart_data = pd.DataFrame(
        np.random.randint(1000, 6000, size=(30, 2)),
        columns=['YouTube Views', 'Instagram Reach'],
        index=pd.date_range(start=datetime.today() - pd.Timedelta(days=30), periods=30)
    )
    # Using Blue and Red colors for the chart
    st.area_chart(chart_data, color=["#0044cc", "#E74C3C"], height=350)

with c2:
    st.subheader("🎯 Audience Demographics")
    # Fake Data for the Bar Chart
    demo_data = pd.DataFrame({
        'Platform': ['YouTube', 'Instagram', 'Facebook', 'Pinterest'],
        'Male': [65, 40, 55, 25],
        'Female': [30, 55, 40, 70],
        'Other': [5, 5, 5, 5]
    })
    # Using Blue, Red, Green colors
    st.bar_chart(demo_data.set_index('Platform'), color=["#0044cc", "#E74C3C", "#2ECC71"], height=350)

st.write("---")

# --- 6. Data Entry Form (Ref: Add New Expense) ---
st.subheader("➕ Add New Post Data (Manual Entry)")
with st.expander("📝 Open Data Entry Form", expanded=False): # Collapsible form
    with st.form("data_entry_form"):
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            platform = st.selectbox("Platform *", ["YouTube", "Instagram", "Facebook", "Pinterest"])
            post_date = st.date_input("Post Date *", datetime.today())
        with f_col2:
            views = st.number_input("Views/Reach *", min_value=0, step=1, value=1000)
            likes = st.number_input("Likes/Engagement *", min_value=0, step=1, value=100)
        
        title = st.text_input("Post Title/Caption *", placeholder="E.g., 'My Dubai Vlog' or 'New Product Photo'")
        status = st.selectbox("Status", ["Published", "Scheduled", "Draft"])
        
        submitted = st.form_submit_button("💾 Save Post Data")
        if submitted:
            st.success(f"✅ Data for '{title}' on {platform} has been saved successfully!")

# --- 7. Data Records Table (Ref: Expense Records) ---
st.subheader("📋 Recent Post Records")
# Generating Fake Table Data
table_data = pd.DataFrame({
    'Date': pd.date_range(start=datetime.today() - pd.Timedelta(days=5), periods=5).strftime('%Y-%m-%d')[::-1],
    'Platform': ['Pinterest', 'Facebook', 'YouTube', 'Instagram', 'YouTube'],
    'Title': ['Design Inspiration Board', 'Page Update Post', 'Python Tutorial Part 2', 'Weekend Photo Dump', 'My New Vlog'],
    'Views': [15200, 850, 3200, 4500, 1200],
    'Likes': [1200, 45, 250, 680, 150],
    'Status': ['Published'] * 5
})
# Displaying the table
st.dataframe(table_data, use_container_width=True, hide_index=True)

# --- 8. Sidebar (Settings) ---
st.sidebar.header("🛠️ Dashboard Settings")
st.sidebar.markdown("---")
st.sidebar.write("**Version:** 3.0 (Pro Max)")
st.sidebar.write("**Last Sync:** Just Now")
st.sidebar.button("🔄 Force Refresh Data")
st.sidebar.markdown("---")
st.sidebar.info("ℹ️ **Note:** This dashboard is currently showing simulated data for design demonstration.")
