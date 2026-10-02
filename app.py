import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Page configuration
st.set_page_config(
    page_title="MBA 2nd Year 3rd Sem - Attendance Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Dark Theme CSS with Vibrant Attractive Accents
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Sleek Deep Dark Background */
    .stApp {
        background-color: #0A0E1A !important;
        color: #F8FAFC !important;
    }

    /* Hide Streamlit Header & Chrome */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        z-index: 1;
    }
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }

    .main .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
    }

    /* Dark Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    /* Glowing Gradient Navigation Radio Buttons */
    div[data-testid="stRadio"] > div {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    div[data-testid="stRadio"] label {
        background: rgba(255, 255, 255, 0.03) !important;
        border-radius: 12px !important;
        padding: 10px 16px !important;
        cursor: pointer !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        color: #94A3B8 !important;
        font-weight: 500 !important;
        font-size: 14px !important;
    }
    div[data-testid="stRadio"] label:hover {
        background: rgba(99, 102, 241, 0.12) !important;
        color: #F8FAFC !important;
        border-color: rgba(99, 102, 241, 0.3) !important;
        transform: translateX(3px);
    }
    div[data-testid="stRadio"] input[type="radio"] {
        display: none !important;
    }
    div[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p {
        font-size: 14px !important;
        font-weight: 600 !important;
        color: inherit !important;
    }
    /* Active Radio Item with Vibrant Violet-Indigo Glow */
    div[data-testid="stRadio"] label:has(input[type="radio"]:checked) {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border-color: #818CF8 !important;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.45) !important;
    }
    div[data-testid="stRadio"] label:has(input[type="radio"]:checked) p {
        color: #FFFFFF !important;
    }

    /* Top Navigation Header */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
        background: rgba(15, 23, 42, 0.6);
        padding: 14px 20px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(12px);
    }
    .top-bar-title-wrap {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .top-bar-title {
        font-size: 22px;
        font-weight: 800;
        background: linear-gradient(135deg, #60A5FA 0%, #C084FC 50%, #F472B6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.3px;
    }
    .top-bar-badge {
        background: rgba(99, 102, 241, 0.18);
        color: #A5B4FC;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 20px;
        border: 1px solid rgba(99, 102, 241, 0.35);
    }
    .top-bar-actions {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .action-icon {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background: #1E293B;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #94A3B8;
        cursor: pointer;
        font-size: 15px;
        transition: all 0.2s ease;
    }
    .action-icon:hover {
        background: #334155;
        color: #F8FAFC;
    }
    .avatar-img {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #6366F1;
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.5);
    }

    /* Luxury Dark Card with Soft Glassmorphic Glow */
    .dark-card {
        background: #131B2E;
        border-radius: 20px;
        padding: 22px 24px;
        border: 1px solid rgba(255, 255, 255, 0.07);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
        margin-bottom: 20px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .dark-card:hover {
        border-color: rgba(99, 102, 241, 0.25);
    }
    .card-title {
        font-size: 15px;
        font-weight: 700;
        color: #F1F5F9;
        margin-bottom: 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* 6 Horizontal Mini Cards with Glowing Colors */
    .stat-row-grid {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 12px;
        width: 100%;
    }
    .mini-stat-card {
        background: #0E1626;
        border-radius: 16px;
        padding: 16px 12px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: 10px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .mini-stat-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    .mini-icon-box {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }
    .mini-label {
        font-size: 11px;
        font-weight: 600;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .mini-val {
        font-size: 24px;
        font-weight: 800;
        line-height: 1;
    }

    /* 2x2 Metric Sub-card Grid */
    .grid-2x2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
    }
    .box-metric {
        background: #0E1626;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 16px 18px;
        transition: border-color 0.2s ease;
    }
    .box-metric:hover {
        border-color: rgba(99, 102, 241, 0.3);
    }
    .box-metric-lbl {
        font-size: 11px;
        font-weight: 600;
        color: #94A3B8;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }
    .box-metric-num {
        font-size: 22px;
        font-weight: 800;
    }

    /* Form Inputs in Dark Theme */
    div[data-testid="stSelectbox"] > div {
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        background-color: #131B2E !important;
        color: #F8FAFC !important;
    }
    div[data-testid="stTextInput"] input {
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        background-color: #131B2E !important;
        color: #F8FAFC !important;
    }
    div[data-testid="stNumberInput"] input {
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        background-color: #131B2E !important;
        color: #F8FAFC !important;
    }
</style>
""", unsafe_allow_html=True)

# Load data safely
@st.cache_data
def load_data():
    csv_path = "attendance.csv"
    if not os.path.exists(csv_path):
        return None
    df = pd.read_csv(csv_path)
    df['Attendance_Percentage'] = pd.to_numeric(df['Attendance_Percentage'], errors='coerce')
    total_classes_map = {
        'MBG24301T': 16,
        'MBG24302T': 16,
        'MBG24303L': 24,
    }
    df['Total_Classes'] = df['Course_Code'].map(lambda c: total_classes_map.get(c, 17))
    df['Attended_Classes'] = (df['Attendance_Percentage'] / 100.0 * df['Total_Classes']).round().astype(int)
    return df

df = load_data()

if df is None:
    st.error("⚠️ 'attendance.csv' not found. Please ensure the CSV file is generated.")
    st.stop()

# Key metrics
total_students = df['Register_No'].nunique()
total_registrations = len(df)
overall_avg = df['Attendance_Percentage'].mean()
eligible_regs = int((df['Status'] == 'Eligible').sum())
shortage_regs = int((df['Status'] == 'Shortage').sum())
total_courses = df['Course_Code'].nunique()

shortage_records = df[df['Attendance_Percentage'] < 75.0]
defaulter_ids = shortage_records['Register_No'].unique()
total_defaulters = len(defaulter_ids)
fully_eligible = total_students - total_defaulters

severe_shortage_count = int((df['Attendance_Percentage'] < 50.0).sum())
borderline_shortage_count = int(((df['Attendance_Percentage'] >= 50.0) & (df['Attendance_Percentage'] < 75.0)).sum())

core_courses = ['MBG24301T', 'MBG24302T', 'MBG24303L']
core_regs = int(df['Course_Code'].isin(core_courses).sum())
elective_regs = total_registrations - core_regs

# SIDEBAR (Dark Luxury Theme)
with st.sidebar:
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 6px 4px 22px 4px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 24px;">🎓</span>
                <div>
                    <div style="font-size: 16px; font-weight: 800; color: #F8FAFC; line-height: 1.1;">MBA 2nd Year</div>
                    <div style="font-size: 12px; font-weight: 600; color: #818CF8;">3rd Semester</div>
                </div>
            </div>
            <span style="color: #64748B; font-size: 16px; cursor: pointer;">☰</span>
        </div>
    """, unsafe_allow_html=True)

    nav_options = [
        "Dashboard",
        "Attendance",
        "Defaulters List",
        "Attendance Calculator",
        "Student Report Card",
        "Subject Rankings",
        "Master Records"
    ]
    selected_nav = st.radio(
        "Navigation",
        nav_options,
        index=0,
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border:none;border-top:1px solid rgba(255,255,255,0.08);margin:20px 0;'>", unsafe_allow_html=True)
    st.caption("🔍 FILTER ATTENDANCE")

    filter_course = st.selectbox("Course", ["All Courses"] + sorted(df['Course_Title'].unique().tolist()))
    filter_status = st.selectbox("Status", ["All Statuses", "Eligible (≥75%)", "Shortage (<75%)"])
    search_keyword = st.text_input("Search Student", placeholder="Name or Reg No...")

    st.markdown("""
        <div style="margin-top: 35px; color: #64748B; font-size: 13px; display: flex; flex-direction: column; gap: 14px;">
            <div style="display: flex; align-items: center; gap: 10px; cursor: pointer; color: #94A3B8;">⚙️ System Settings</div>
            <div style="display: flex; align-items: center; gap: 10px; cursor: pointer; color: #94A3B8;">❓ Help & Guidelines</div>
        </div>
    """, unsafe_allow_html=True)

# Apply filters
filtered_df = df.copy()
if filter_course != "All Courses":
    filtered_df = filtered_df[filtered_df['Course_Title'] == filter_course]
if filter_status == "Eligible (≥75%)":
    filtered_df = filtered_df[filtered_df['Status'] == 'Eligible']
elif filter_status == "Shortage (<75%)":
    filtered_df = filtered_df[filtered_df['Status'] == 'Shortage']
if search_keyword.strip():
    kw = search_keyword.strip().lower()
    filtered_df = filtered_df[
        filtered_df['Student_Name'].str.lower().str.contains(kw) |
        filtered_df['Register_No'].str.lower().str.contains(kw)
    ]

# TOP BAR with "MBA 2nd Year 3rd Sem" Heading
st.markdown(f"""
    <div class="top-bar">
        <div class="top-bar-title-wrap">
            <span style="font-size: 24px;">📊</span>
            <div class="top-bar-title">MBA 2nd Year 3rd Sem - {selected_nav}</div>
            <span class="top-bar-badge">Fall 2026</span>
        </div>
        <div class="top-bar-actions">
            <div class="action-icon">🔍</div>
            <div class="action-icon" style="position: relative;">
                🔔
                <span style="position: absolute; top: 6px; right: 7px; width: 6px; height: 6px; background: #F43F5E; border-radius: 50%; box-shadow: 0 0 8px #F43F5E;"></span>
            </div>
            <img class="avatar-img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" alt="Profile"/>
        </div>
    </div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# 1. DASHBOARD VIEW (Vibrant Dark Theme)
# -------------------------------------------------------------
if selected_nav in ["Dashboard", "Attendance"]:
    # ================= ROW 1 =================
    r1_col1, r1_col2 = st.columns([1.1, 2.9], gap="medium")

    with r1_col1:
        # Statistics Donut Card with Glowing Colors
        pct_eligible_num = round((eligible_regs / total_registrations) * 100)
        st.markdown("""
            <div class="dark-card">
                <div class="card-title">
                    <span>Attendance Statistics</span>
                    <span style="color: #64748B; font-size: 14px; cursor: pointer;">•••</span>
                </div>
        """, unsafe_allow_html=True)

        fig_donut = go.Figure(data=[go.Pie(
            values=[eligible_regs, shortage_regs],
            labels=['Eligible (≥75%)', 'Shortage (<75%)'],
            hole=0.68,
            marker=dict(colors=['#10B981', '#F43F5E'], line=dict(color='#0A0E1A', width=3)),
            textinfo='none',
            hoverinfo='label+value+percent'
        )])
        fig_donut.update_layout(
            showlegend=False,
            margin=dict(t=0, b=0, l=0, r=0),
            height=190,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            annotations=[
                dict(
                    text=f"<span style='font-size:11px;color:#94A3B8;letter-spacing:0.5px;'>TOTAL STUDENTS</span><br><b style='font-size:26px;color:#F8FAFC;'>{total_students}</b>",
                    x=0.5, y=0.5,
                    font_size=14,
                    showarrow=False
                )
            ]
        )
        st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})

        st.markdown(f"""
                <div style="display: flex; justify-content: center; margin-top: 10px;">
                    <span style="background: rgba(16, 185, 129, 0.15); color: #34D399; font-weight: 700; font-size: 12px; padding: 5px 16px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.35);">
                        ✨ {pct_eligible_num}% Eligible Registrations
                    </span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with r1_col2:
        # 6 Horizontal Metric Cards with Attractive Glowing Badges
        st.markdown(f"""
            <div class="dark-card">
                <div class="card-title">
                    <span>Semester Attendance Metrics</span>
                    <span style="color: #64748B; font-size: 14px; cursor: pointer;">•••</span>
                </div>
                <div class="stat-row-grid">
                    <div class="mini-stat-card">
                        <div class="mini-icon-box" style="background: rgba(16, 185, 129, 0.16); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.3);">✓</div>
                        <div class="mini-label">Eligible</div>
                        <div class="mini-val" style="color: #34D399;">{eligible_regs}</div>
                    </div>
                    <div class="mini-stat-card">
                        <div class="mini-icon-box" style="background: rgba(244, 63, 94, 0.16); color: #FB7185; border: 1px solid rgba(244, 63, 94, 0.3);">⚠️</div>
                        <div class="mini-label">Shortage</div>
                        <div class="mini-val" style="color: #FB7185;">{shortage_regs}</div>
                    </div>
                    <div class="mini-stat-card">
                        <div class="mini-icon-box" style="background: rgba(245, 158, 11, 0.16); color: #FBBF24; border: 1px solid rgba(245, 158, 11, 0.3);">☂️</div>
                        <div class="mini-label">Defaulters</div>
                        <div class="mini-val" style="color: #FBBF24;">{total_defaulters}</div>
                    </div>
                    <div class="mini-stat-card">
                        <div class="mini-icon-box" style="background: rgba(6, 182, 212, 0.16); color: #22D3EE; border: 1px solid rgba(6, 182, 212, 0.3);">👨‍🎓</div>
                        <div class="mini-label">Students</div>
                        <div class="mini-val" style="color: #22D3EE;">{total_students}</div>
                    </div>
                    <div class="mini-stat-card">
                        <div class="mini-icon-box" style="background: rgba(168, 85, 247, 0.16); color: #C084FC; border: 1px solid rgba(168, 85, 247, 0.3);">📚</div>
                        <div class="mini-label">Courses</div>
                        <div class="mini-val" style="color: #C084FC;">{total_courses}</div>
                    </div>
                    <div class="mini-stat-card">
                        <div class="mini-icon-box" style="background: rgba(59, 130, 246, 0.16); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.3);">📈</div>
                        <div class="mini-label">Class Avg</div>
                        <div class="mini-val" style="color: #60A5FA;">{overall_avg:.1f}%</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # ================= ROW 2 =================
    r2_col1, r2_col2, r2_col3 = st.columns([1.3, 1.4, 1.3], gap="medium")

    with r2_col1:
        # Variance vs 75% Target Chart
        st.markdown("""
            <div class="dark-card">
                <div class="card-title">
                    <span>Attendance Variance vs 75% Target</span>
                    <span style="color: #818CF8; font-size: 12px; font-weight: 600;">Threshold</span>
                </div>
        """, unsafe_allow_html=True)

        subj_diff = df.groupby('Course_Code')['Attendance_Percentage'].mean().reset_index()
        subj_diff['Diff'] = subj_diff['Attendance_Percentage'] - 75.0
        subj_diff = subj_diff.head(6)

        fig_diff = go.Figure()
        # Vibrant colors: green for positive variance, bright neon pink/red for negative variance
        bar_colors = ['#10B981' if v >= 0 else '#F43F5E' for v in subj_diff['Diff']]
        fig_diff.add_trace(go.Bar(
            x=subj_diff['Course_Code'],
            y=subj_diff['Diff'],
            marker_color=bar_colors,
            width=0.42
        ))
        fig_diff.add_hline(y=0, line_width=1.5, line_color="#475569")
        fig_diff.update_layout(
            margin=dict(t=5, b=5, l=5, r=5),
            height=210,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#94A3B8'),
            yaxis=dict(title="Variance (%)", showgrid=True, gridcolor="rgba(255,255,255,0.06)", zeroline=False),
            xaxis=dict(showgrid=False)
        )
        st.plotly_chart(fig_diff, use_container_width=True, config={'displayModeBar': False})
        st.markdown("</div>", unsafe_allow_html=True)

    with r2_col2:
        # Subject Benchmarks (Overtime style)
        st.markdown("""
            <div class="dark-card">
                <div class="card-title">
                    <span>Subject Performance Benchmarks</span>
                    <span style="background: linear-gradient(135deg, #4F46E5, #7C3AED); color: white; border-radius: 12px; padding: 3px 12px; font-size: 11px; font-weight: 700;">Average %</span>
                </div>
        """, unsafe_allow_html=True)

        top_courses = df.groupby('Course_Code')['Attendance_Percentage'].mean().reset_index()
        top_courses = top_courses.sort_values('Attendance_Percentage', ascending=False).head(7)

        # Gradient bar coloring with highlighted champion course in bright neon cyan
        bar_c2 = ['#38BDF8' if i == 0 else ('#818CF8' if i < 3 else '#6366F1') for i in range(len(top_courses))]
        fig_bench = go.Figure(go.Bar(
            x=top_courses['Course_Code'],
            y=top_courses['Attendance_Percentage'],
            marker_color=bar_c2,
            width=0.42
        ))
        fig_bench.update_layout(
            margin=dict(t=5, b=5, l=5, r=5),
            height=210,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#94A3B8'),
            yaxis=dict(range=[0, 100], showgrid=True, gridcolor="rgba(255,255,255,0.06)", zeroline=False),
            xaxis=dict(showgrid=False)
        )
        st.plotly_chart(fig_bench, use_container_width=True, config={'displayModeBar': False})
        st.markdown("</div>", unsafe_allow_html=True)

    with r2_col3:
        # Attendance Source 2x2 grid with glowing numbers
        st.markdown(f"""
            <div class="dark-card">
                <div class="card-title">
                    <span>Attendance Distribution</span>
                    <span style="color: #64748B; font-size: 14px; cursor: pointer;">•••</span>
                </div>
                <div class="grid-2x2">
                    <div class="box-metric">
                        <div class="box-metric-lbl">Core Courses</div>
                        <div class="box-metric-num" style="color: #60A5FA;">{core_regs}</div>
                    </div>
                    <div class="box-metric">
                        <div class="box-metric-lbl">Electives</div>
                        <div class="box-metric-num" style="color: #C084FC;">{elective_regs}</div>
                    </div>
                    <div class="box-metric">
                        <div class="box-metric-lbl">100% Eligible</div>
                        <div class="box-metric-num" style="color: #34D399;">{fully_eligible}</div>
                    </div>
                    <div class="box-metric">
                        <div class="box-metric-lbl">Total Subjects</div>
                        <div class="box-metric-num" style="color: #FBBF24;">{total_courses}</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # ================= ROW 3 =================
    r3_col1, r3_col2 = st.columns([1, 1], gap="medium")

    with r3_col1:
        # Exceptions
        st.markdown(f"""
            <div class="dark-card">
                <div class="card-title">
                    <span>Attendance Exceptions</span>
                    <span style="color: #64748B; font-size: 14px; cursor: pointer;">•••</span>
                </div>
                <div class="grid-2x2">
                    <div class="box-metric">
                        <div class="box-metric-lbl">Severe Shortage (&lt;50%)</div>
                        <div class="box-metric-num" style="color: #FB7185;">{severe_shortage_count} cases</div>
                    </div>
                    <div class="box-metric">
                        <div class="box-metric-lbl">Borderline Shortage (50-74%)</div>
                        <div class="box-metric-num" style="color: #FBBF24;">{borderline_shortage_count} cases</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with r3_col2:
        # Action Items
        st.markdown(f"""
            <div class="dark-card">
                <div class="card-title">
                    <span>Pending Actions & Undertakings</span>
                    <span style="color: #64748B; font-size: 14px; cursor: pointer;">•••</span>
                </div>
                <div class="grid-2x2">
                    <div class="box-metric">
                        <div class="box-metric-lbl">Defaulter Interventions Required</div>
                        <div class="box-metric-num" style="color: #F87171;">{total_defaulters} students</div>
                    </div>
                    <div class="box-metric">
                        <div class="box-metric-lbl">Eligible Without Undertakings</div>
                        <div class="box-metric-num" style="color: #34D399;">{fully_eligible} students</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# 2. DEFAULTERS LIST VIEW
# -------------------------------------------------------------
elif selected_nav == "Defaulters List":
    st.markdown("""
        <div class="dark-card">
            <div class="card-title">
                <span>⚠️ Defaulters Directory (Students with Attendance &lt; 75%)</span>
                <span style="background: rgba(244, 63, 94, 0.2); color: #FB7185; font-size: 12px; font-weight: 700; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(244, 63, 94, 0.35);">
                    20 Defaulters Found
                </span>
            </div>
    """, unsafe_allow_html=True)

    defaulters_data = []
    for reg_no in defaulter_ids:
        s_df = df[df['Register_No'] == reg_no]
        student_name = s_df['Student_Name'].iloc[0]
        s_shortages = s_df[s_df['Attendance_Percentage'] < 75.0]
        shortage_details = "; ".join([f"{r['Course_Code']} ({r['Attendance_Percentage']}%)" for _, r in s_shortages.iterrows()])
        defaulters_data.append({
            "Register No": reg_no,
            "Student Name": student_name,
            "Shortage Count": len(s_shortages),
            "Shortage Subjects": shortage_details,
            "Avg Attendance": round(s_df['Attendance_Percentage'].mean(), 2)
        })

    defaulters_df = pd.DataFrame(defaulters_data).sort_values(by=["Shortage Count", "Avg Attendance"], ascending=[False, True]).reset_index(drop=True)
    defaulters_df.index += 1
    defaulters_df.index.name = "Rank"

    st.dataframe(
        defaulters_df,
        column_config={
            "Shortage Count": st.column_config.NumberColumn(
                "Shortage Count",
                format="%d ⚠️"
            ),
            "Avg Attendance": st.column_config.ProgressColumn(
                "Avg Attendance",
                format="%.2f%%",
                min_value=0,
                max_value=100
            )
        },
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# 3. ATTENDANCE CALCULATOR VIEW
# -------------------------------------------------------------
elif selected_nav == "Attendance Calculator":
    st.markdown("""
        <div class="dark-card">
            <div class="card-title">
                <span>🧮 75% Attendance Eligibility Calculator</span>
                <span style="color: #818CF8; font-size: 13px; font-weight: 600;">Consecutive Classes Recovery Tool</span>
            </div>
    """, unsafe_allow_html=True)

    calc_mode = st.radio(
        "Choose Mode:",
        ["Select by Student & Registered Course", "Custom / Manual Input"],
        horizontal=True
    )

    if calc_mode == "Select by Student & Registered Course":
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            stud_opts = df[['Register_No', 'Student_Name']].drop_duplicates().sort_values('Student_Name')
            stud_list = [f"{row['Student_Name']} ({row['Register_No']})" for _, row in stud_opts.iterrows()]
            calc_stud = st.selectbox("Select Student", stud_list, key="calc_tab_student")
            calc_reg = calc_stud.split('(')[-1].replace(')', '').strip()

        courses_for_stud = df[df['Register_No'] == calc_reg].copy()
        course_display_opts = [
            f"{r['Course_Code']} - {r['Course_Title']} (Current: {r['Attendance_Percentage']:.2f}% | {r['Status']})"
            for _, r in courses_for_stud.iterrows()
        ]

        with col_c2:
            calc_course_choice = st.selectbox("Select Subject", course_display_opts, key="calc_tab_course")
            sel_code = calc_course_choice.split(' - ')[0].strip()

        row_sel = courses_for_stud[courses_for_stud['Course_Code'] == sel_code].iloc[0]
        attended = int(row_sel['Attended_Classes'])
        total_held = int(row_sel['Total_Classes'])
        curr_pct = float(row_sel['Attendance_Percentage'])
        course_name = f"{row_sel['Course_Code']} - {row_sel['Course_Title']}"
        student_display = row_sel['Student_Name']

    else:
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            total_held = st.number_input("Total Classes Held So Far", min_value=1, max_value=200, value=16, step=1)
        with col_m2:
            attended = st.number_input("Classes Attended So Far", min_value=0, max_value=int(total_held), value=min(7, int(total_held)), step=1)
        curr_pct = round((attended / total_held) * 100, 2)
        course_name = "Custom Subject"
        student_display = "Student"

    target_pct = st.slider("Target Attendance Requirement (%)", min_value=50, max_value=100, value=75, step=1)
    target_dec = target_pct / 100.0

    met1, met2, met3, met4 = st.columns(4)
    met1.metric("Classes Held", f"{total_held}")
    met2.metric("Classes Attended", f"{attended}")
    met3.metric("Current Attendance", f"{curr_pct:.2f}%")
    is_eligible = curr_pct >= target_pct
    met4.metric(
        "Current Status",
        "Eligible" if is_eligible else "Shortage",
        delta=f"{curr_pct - target_pct:+.2f}%",
        delta_color="normal" if is_eligible else "inverse"
    )

    st.markdown("<hr style='border:none;border-top:1px solid rgba(255,255,255,0.08);margin:20px 0;'>", unsafe_allow_html=True)

    if curr_pct >= target_pct:
        st.success(
            f"🎉 **Eligible!** Attendance in **{course_name}** is already **{curr_pct:.2f}%**, exceeding the required **{target_pct}%** mark.\n\n"
            f"👉 **Upcoming consecutive classes needed to attend: 0 classes.**"
        )
        if target_dec > 0:
            missable = int((attended - target_dec * total_held) // target_dec)
            if missable > 0:
                st.info(f"💡 **Safety Margin**: You can afford to miss up to **{missable} upcoming class{'es' if missable > 1 else ''}** and still maintain $\ge {target_pct}\%$ attendance.")
            else:
                st.info(f"⚠️ **Borderline**: You are right at {target_pct}%. Missing even 1 class will cause shortage.")
    else:
        numerator = target_dec * total_held - attended
        denom = 1.0 - target_dec
        required_classes = int(-(-numerator // denom))
        required_classes = max(0, required_classes)

        proj_att = attended + required_classes
        proj_tot = total_held + required_classes
        proj_pct = round((proj_att / proj_tot) * 100, 2)

        st.error(
            f"🚨 **Shortage Detected for {student_display}!**\n\n"
            f"To reach **{target_pct}% eligibility** in **{course_name}**, you must attend:\n\n"
            f"### 👉 **`{required_classes}` upcoming consecutive classes** (without missing any)\n\n"
            f"Reaching this target will bring your attendance record to **{proj_att}/{proj_tot} ({proj_pct:.2f}%)**."
        )

        # Simulation
        sim_rows = []
        max_steps = max(required_classes + 3, 6)
        for step in range(1, max_steps + 1):
            s_att = attended + step
            s_tot = total_held + step
            s_pct = round((s_att / s_tot) * 100, 2)
            sim_rows.append({
                "Classes Attended (+N)": f"+{step} class" if step == 1 else f"+{step} classes",
                "New Record": f"{s_att}/{s_tot}",
                "Projected Attendance (%)": s_pct,
                "Status": "✅ Eligible" if s_pct >= target_pct else "❌ Shortage"
            })
        sim_df = pd.DataFrame(sim_rows)

        fig_sim = px.line(
            sim_df,
            x="Classes Attended (+N)",
            y="Projected Attendance (%)",
            markers=True,
            title="Attendance Recovery Trajectory"
        )
        fig_sim.add_hline(y=target_pct, line_width=2, line_dash="dash", line_color="#34D399", annotation_text=f"Target {target_pct}%")
        fig_sim.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#94A3B8'),
            yaxis=dict(range=[max(0, curr_pct - 5), 100], gridcolor="rgba(255,255,255,0.06)"),
            xaxis=dict(gridcolor="rgba(255,255,255,0.06)")
        )
        st.plotly_chart(fig_sim, use_container_width=True)

        with st.expander("📊 View Detailed Step-by-Step Simulation Table"):
            st.dataframe(sim_df, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# 4. STUDENT REPORT CARD VIEW
# -------------------------------------------------------------
elif selected_nav == "Student Report Card":
    st.markdown("""
        <div class="dark-card">
            <div class="card-title">
                <span>👤 Individual Student Attendance Card</span>
            </div>
    """, unsafe_allow_html=True)

    student_options = df[['Register_No', 'Student_Name']].drop_duplicates().sort_values('Student_Name')
    student_labels = [f"{row['Student_Name']} ({row['Register_No']})" for _, row in student_options.iterrows()]

    selected_student_label = st.selectbox("Select Student", student_labels)
    if selected_student_label:
        selected_reg = selected_student_label.split('(')[-1].replace(')', '').strip()
        student_df = df[df['Register_No'] == selected_reg].copy()
        student_name = student_df['Student_Name'].iloc[0]
        avg_student_att = student_df['Attendance_Percentage'].mean()
        shortages_count = (student_df['Attendance_Percentage'] < 75.0).sum()

        st.markdown(f"### **{student_name}** (`{selected_reg}`)")
        c1, c2, c3 = st.columns(3)
        c1.metric("Overall Average", f"{avg_student_att:.2f}%")
        c2.metric("Total Courses", f"{len(student_df)}")
        c3.metric(
            "Shortage Subjects",
            f"{shortages_count}",
            delta=f"{shortages_count} shortage(s)" if shortages_count > 0 else "All Clear",
            delta_color="inverse" if shortages_count > 0 else "normal"
        )

        display_student_df = student_df[['Course_Code', 'Course_Title', 'Attendance_Percentage', 'Status']].reset_index(drop=True)
        display_student_df.index += 1

        st.dataframe(
            display_student_df,
            column_config={
                "Attendance_Percentage": st.column_config.ProgressColumn(
                    "Attendance %",
                    format="%.2f%%",
                    min_value=0,
                    max_value=100
                )
            },
            use_container_width=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# 5. SUBJECT RANKINGS VIEW
# -------------------------------------------------------------
elif selected_nav == "Subject Rankings":
    st.markdown("""
        <div class="dark-card">
            <div class="card-title">
                <span>📚 Subject-Wise Attendance Benchmarks</span>
            </div>
    """, unsafe_allow_html=True)

    subject_stats = df.groupby(['Course_Code', 'Course_Title'])['Attendance_Percentage'].agg(
        Count='count',
        Average='mean',
        Shortages=lambda x: (x < 75.0).sum()
    ).reset_index()
    subject_stats['Average'] = subject_stats['Average'].round(2)
    subject_stats = subject_stats.sort_values(by='Average', ascending=True).reset_index(drop=True)
    subject_stats.index += 1

    colors = ['#F43F5E' if avg < 75 else '#10B981' for avg in subject_stats['Average']]

    fig_bar = go.Figure(go.Bar(
        x=subject_stats['Average'],
        y=subject_stats['Course_Code'] + " - " + subject_stats['Course_Title'],
        orientation='h',
        marker=dict(color=colors),
        text=[f"{v:.2f}%" for v in subject_stats['Average']],
        textposition='outside'
    ))
    fig_bar.add_vline(x=75, line_width=2, line_dash="dash", line_color="#FBBF24", annotation_text="75% Threshold")
    fig_bar.update_layout(
        xaxis=dict(range=[0, 105], title="Average Attendance %", gridcolor="rgba(255,255,255,0.06)"),
        yaxis=dict(title="", autorange="reversed"),
        margin=dict(t=20, b=20, l=20, r=40),
        height=500,
        font=dict(color='#94A3B8'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    st.dataframe(
        subject_stats,
        column_config={
            "Average": st.column_config.ProgressColumn(
                "Average Attendance",
                format="%.2f%%",
                min_value=0,
                max_value=100
            ),
            "Shortages": st.column_config.NumberColumn(
                "Students in Shortage",
                format="%d 🚨"
            )
        },
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# 6. MASTER RECORDS VIEW
# -------------------------------------------------------------
elif selected_nav == "Master Records":
    st.markdown(f"""
        <div class="dark-card">
            <div class="card-title">
                <span>📋 Filtered Attendance Records</span>
                <span style="color: #94A3B8; font-size: 13px;">Showing {len(filtered_df)} of {len(df)} records</span>
            </div>
    """, unsafe_allow_html=True)

    st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

    csv_bytes = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_bytes,
        file_name="MBA_3rd_Sem_attendance.csv",
        mime="text/csv"
    )
    st.markdown("</div>", unsafe_allow_html=True)
