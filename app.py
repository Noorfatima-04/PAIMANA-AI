import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration

st.set_page_config(
    page_title="PAIMANA AI",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f4f6f9;
}

[data-testid="stSidebar"] {
    background: #102a43;
    min-width: 270px;
}

[data-testid="stSidebar"] > div:first-child {
    background: #102a43;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

.sidebar-brand {
    padding: 8px 4px 25px 4px;
    border-bottom: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 20px;
}

.sidebar-brand-title {
    font-size: 24px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.sidebar-brand-subtitle {
    font-size: 12px;
    color: #b9c9d8 !important;
    margin-top: 4px;
}

.sidebar-section {
    font-size: 11px;
    font-weight: 600;
    color: #9fb3c8 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 22px;
    margin-bottom: 8px;
}

.main-header {
    background: #ffffff;
    border-radius: 14px;
    padding: 28px 32px;
    margin-bottom: 22px;
    border: 1px solid #e3e8ee;
    box-shadow: 0 2px 8px rgba(16, 42, 67, 0.05);
}

.header-label {
    color: #486581;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 8px;
}

.header-title {
    color: #102a43;
    font-size: 32px;
    font-weight: 700;
    margin: 0;
}

.header-subtitle {
    color: #627d98;
    font-size: 15px;
    margin-top: 8px;
}

.snapshot-badge {
    display: inline-block;
    background: #e9f2fb;
    color: #1565a8;
    padding: 7px 13px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    margin-top: 15px;
}

.kpi-card {
    background: #ffffff;
    border: 1px solid #e1e8ef;
    border-radius: 12px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 2px 7px rgba(16, 42, 67, 0.04);
}

.kpi-label {
    color: #627d98;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.6px;
}

.kpi-value {
    color: #102a43;
    font-size: 29px;
    font-weight: 700;
    margin-top: 10px;
}

.kpi-description {
    color: #829ab1;
    font-size: 11px;
    margin-top: 4px;
}

.section-title {
    color: #102a43;
    font-size: 20px;
    font-weight: 700;
    margin-top: 8px;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #627d98;
    font-size: 13px;
    margin-bottom: 16px;
}

.panel {
    background: #ffffff;
    border: 1px solid #e1e8ef;
    border-radius: 12px;
    padding: 22px;
    color: #102a43;
    box-shadow: 0 2px 7px rgba(16, 42, 67, 0.04);
}

.panel * {
    color: #102a43 !important;
}

.project-header {
    background: #102a43;
    color: white;
    border-radius: 12px;
    padding: 24px;
    margin-top: 15px;
    margin-bottom: 18px;
}

.project-name {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 7px;
}

.project-meta {
    color: #c9d7e5;
    font-size: 13px;
}

.risk-card {
    background: #ffffff;
    border: 1px solid #e1e8ef;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
    min-height: 110px;
}

.risk-card-label {
    color: #627d98;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
}

.risk-card-value {
    color: #102a43;
    font-size: 25px;
    font-weight: 700;
    margin-top: 8px;
}

.warning-box {
    border-radius: 10px;
    padding: 15px 18px;
    margin: 8px 0;
    font-size: 13px;
}

.warning-critical {
    background: #fff1f0;
    border-left: 5px solid #d64545;
    color: #8a2020;
}

.warning-high {
    background: #fff7e6;
    border-left: 5px solid #e09b24;
    color: #805c10;
}

.warning-medium {
    background: #fffbea;
    border-left: 5px solid #d7b11e;
    color: #6d5c0a;
}

.warning-low {
    background: #eef9f1;
    border-left: 5px solid #3b9b5f;
    color: #25633b;
}

.footer {
    text-align: center;
    color: #829ab1;
    font-size: 11px;
    padding: 30px 0 10px 0;
}

div[data-testid="stMetric"] {
    background: transparent;
}

div[data-testid="stMetricLabel"] {
    color: #627d98 !important;
}

div[data-testid="stMetricValue"] {
    color: #102a43 !important;
}

.stSelectbox label {
    color: #486581 !important;
    font-weight: 600 !important;
    font-size: 12px !important;
}

button[data-baseweb="tab"] {
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# Load data

DATA_PATH = "data/paimana_projects_april_2026.csv"

df = pd.read_csv(DATA_PATH)

# Data preparation

numeric_columns = [
    "original_cost_crore",
    "revised_cost_crore",
    "expenditure_crore",
    "physical_progress_pct"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df["physical_progress_pct"] = df["physical_progress_pct"].fillna(0)

# Convert completion dates

df["original_completion_date"] = pd.to_datetime(
    df["original_completion"],
    format="%m/%Y",
    errors="coerce"
)

df["revised_completion_date"] = pd.to_datetime(
    df["revised_completion"],
    format="%m/%Y",
    errors="coerce"
)

# Cost escalation

df["cost_escalation_pct"] = np.where(
    df["original_cost_crore"] > 0,
    (
        (df["revised_cost_crore"] - df["original_cost_crore"])
        / df["original_cost_crore"]
    ) * 100,
    0
)

# Schedule delay

df["schedule_delay_months"] = np.where(
    df["original_completion_date"].notna()
    & df["revised_completion_date"].notna(),
    (
        (df["revised_completion_date"].dt.year
         - df["original_completion_date"].dt.year) * 12
        +
        (df["revised_completion_date"].dt.month
         - df["original_completion_date"].dt.month)
    ),
    0
)

df["schedule_delay_months"] = df["schedule_delay_months"].clip(lower=0)

# Prototype risk scores

df["cost_risk_score"] = (
    df["cost_escalation_pct"].clip(lower=0) * 2
).clip(upper=100)

df["delay_risk_score"] = (
    df["schedule_delay_months"] * 5
).clip(upper=100)

# Overall screening score

df["risk_score"] = (
    df["cost_risk_score"] * 0.4
    + df["delay_risk_score"] * 0.4
    + (100 - df["physical_progress_pct"].clip(0, 100)) * 0.2
).clip(0, 100)

# Risk level

def classify_risk(score):
    if score >= 70:
        return "Critical"
    elif score >= 50:
        return "High"
    elif score >= 30:
        return "Medium"
    else:
        return "Low"


df["risk_level"] = df["risk_score"].apply(classify_risk)

# Sidebar

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-title">🏗️ PAIMANA AI</div>
        <div class="sidebar-brand-subtitle">
            Infrastructure Risk Intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-section">Navigation</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        ["Dashboard", "Project Intelligence", "All Projects"],
        label_visibility="collapsed"
    )

    st.markdown(
        '<div class="sidebar-section">Project Filters</div>',
        unsafe_allow_html=True
    )

    state_options = ["All States"] + sorted(
        df["state"].dropna().astype(str).unique().tolist()
    )

    selected_state = st.selectbox(
        "State",
        state_options
    )

    agency_options = ["All Agencies"] + sorted(
        df["agency"].dropna().astype(str).unique().tolist()
    )

    selected_agency = st.selectbox(
        "Agency",
        agency_options
    )

    risk_options = [
        "All Risk Levels",
        "Critical",
        "High",
        "Medium",
        "Low"
    ]

    selected_risk = st.selectbox(
        "Risk Level",
        risk_options
    )

    st.markdown(
        '<div class="sidebar-section">Data Source</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "PAIMANA / MoSPI\n\nApril 2026 Flash Report"
    )

# Apply filters

filtered_df = df.copy()

if selected_state != "All States":
    filtered_df = filtered_df[
        filtered_df["state"] == selected_state
    ]

if selected_agency != "All Agencies":
    filtered_df = filtered_df[
        filtered_df["agency"] == selected_agency
    ]

if selected_risk != "All Risk Levels":
    filtered_df = filtered_df[
        filtered_df["risk_level"] == selected_risk
    ]

# Dashboard header

# Dashboard

if page == "Dashboard":

    st.markdown("""
<div class="main-header">

<div class="header-label">
PAIMANA • PROJECT MONITORING INTELLIGENCE
</div>

<div class="header-title">
Predictive Infrastructure Risk & Early Warning
</div>

<div class="header-subtitle">
An explainable decision-support layer for identifying infrastructure
projects that require priority monitoring attention.
</div>

<div class="snapshot-badge">
● APRIL 2026 DATA SNAPSHOT
</div>

</div>
""", unsafe_allow_html=True)

    # Dashboard metrics

    total_projects = len(filtered_df)

    high_risk_projects = len(
        filtered_df[
            filtered_df["risk_level"].isin(["High", "Critical"])
        ]
    )

    cost_risk_projects = len(
        filtered_df[
            filtered_df["cost_risk_score"] >= 50
        ]
    )

    delay_risk_projects = len(
        filtered_df[
            filtered_df["delay_risk_score"] >= 50
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Total Projects</div>
                <div class="kpi-value">{total_projects:,}</div>
                <div class="kpi-description">Projects in current view</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">High / Critical Risk</div>
                <div class="kpi-value">{high_risk_projects:,}</div>
                <div class="kpi-description">Priority monitoring candidates</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Cost Risk</div>
                <div class="kpi-value">{cost_risk_projects:,}</div>
                <div class="kpi-description">Elevated cost indicators</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Schedule Risk</div>
                <div class="kpi-value">{delay_risk_projects:,}</div>
                <div class="kpi-description">Schedule delay indicators</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.caption(
        f"Showing {len(filtered_df):,} of {len(df):,} projects"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Risk distribution

    left_col, right_col = st.columns([1.35, 1])

    with left_col:

        st.markdown(
            '<div class="section-title">Risk Distribution</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">Current project risk screening across the selected portfolio.</div>',
            unsafe_allow_html=True
        )

        risk_distribution = (
            filtered_df["risk_level"]
            .value_counts()
            .reindex(
                ["Critical", "High", "Medium", "Low"],
                fill_value=0
            )
            .reset_index()
        )

        risk_distribution.columns = ["Risk Level", "Projects"]

        fig = px.bar(
            risk_distribution,
            x="Risk Level",
            y="Projects",
            text="Projects",
            color="Risk Level",
            color_discrete_map={
                "Critical": "#c62828",
                "High": "#e67e22",
                "Medium": "#d4a017",
                "Low": "#4f8a5b"
            }
        )

        fig.update_traces(
            textposition="outside",
            marker_line_width=0
        )

        fig.update_layout(
            height=350,
            margin=dict(l=10, r=10, t=15, b=10),
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis_title=None,
            yaxis_title=None,
            showlegend=False,
            font=dict(
                family="Inter",
                color="#486581"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with right_col:

        st.markdown(
            '<div class="section-title">Portfolio Status</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">Risk-level composition of the current project view.</div>',
            unsafe_allow_html=True
        )

        risk_counts = (
            filtered_df["risk_level"]
            .value_counts()
            .reindex(
                ["Critical", "High", "Medium", "Low"],
                fill_value=0
            )
        )

        fig_pie = px.pie(
            values=risk_counts.values,
            names=risk_counts.index,
            hole=0.62,
            color=risk_counts.index,
            color_discrete_map={
                "Critical": "#c62828",
                "High": "#e67e22",
                "Medium": "#d4a017",
                "Low": "#4f8a5b"
            }
        )

        fig_pie.update_layout(
            height=350,
            margin=dict(l=10, r=10, t=15, b=10),
            paper_bgcolor="white",
            showlegend=True,
            legend=dict(
                orientation="h",
                y=-0.05
            ),
            font=dict(
                family="Inter",
                color="#486581"
            )
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    # Priority projects

    st.markdown(
        '<div class="section-title">Priority Projects</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Projects with the highest current screening scores.</div>',
        unsafe_allow_html=True
    )

    priority_projects = (
        filtered_df[
            [
                "project_name",
                "agency",
                "state",
                "risk_score",
                "risk_level",
                "cost_escalation_pct",
                "schedule_delay_months",
                "physical_progress_pct"
            ]
        ]
        .sort_values("risk_score", ascending=False)
        .head(10)
        .copy()
    )

    priority_projects["risk_score"] = (
        priority_projects["risk_score"].round(1)
    )

    priority_projects["cost_escalation_pct"] = (
        priority_projects["cost_escalation_pct"].round(1)
    )

    priority_projects["schedule_delay_months"] = (
        priority_projects["schedule_delay_months"].astype(int)
    )

    priority_projects["physical_progress_pct"] = (
        priority_projects["physical_progress_pct"].round(1)
    )

    priority_projects.columns = [
        "Project",
        "Agency",
        "State",
        "Risk Score",
        "Risk Level",
        "Cost Escalation %",
        "Delay (Months)",
        "Physical Progress %"
    ]

    st.dataframe(
        priority_projects,
        use_container_width=True,
        hide_index=True,
        height=390
    )

# Project intelligence

if page == "Project Intelligence":

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Project Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Detailed project-level risk indicators, drivers and early-warning signals.</div>',
        unsafe_allow_html=True
    )

    if filtered_df.empty:

        st.warning(
            "No projects match the selected filters."
        )

    else:

        project_options = filtered_df.index.tolist()

        selected_project_index = st.selectbox(
            "Select Project",
            project_options,
            format_func=lambda idx: (
                f"{filtered_df.loc[idx, 'project_name']} "
                f"| Code: {filtered_df.loc[idx, 'project_code']}"
            )
        )

        project = filtered_df.loc[selected_project_index]

        # Project header

        st.markdown(
            f"""
            <div class="project-header">
                <div class="project-name">
                    {project['project_name']}
                </div>
                <div class="project-meta">
                    {project['agency']} &nbsp; • &nbsp;
                    {project['state']} &nbsp; • &nbsp;
                    Project Code: {project['project_code']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Project risk summary

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                f"""
                <div class="risk-card">
                    <div class="risk-card-label">Risk Score</div>
                    <div class="risk-card-value">
                        {project['risk_score']:.1f}/100
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="risk-card">
                    <div class="risk-card-label">Risk Level</div>
                    <div class="risk-card-value">
                        {project['risk_level']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""
                <div class="risk-card">
                    <div class="risk-card-label">Cost Escalation</div>
                    <div class="risk-card-value">
                        {project['cost_escalation_pct']:.1f}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                f"""
                <div class="risk-card">
                    <div class="risk-card-label">Schedule Delay</div>
                    <div class="risk-card-value">
                        {int(project['schedule_delay_months'])} months
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Project details

        detail_col1, detail_col2, detail_col3 = st.columns(3)

        with detail_col1:
            st.markdown(
                f"""
                <div class="panel">
                    <div style="font-size:16px; font-weight:700; color:#102a43; margin-bottom:18px;">
                        Financial Details
                    </div>
                    <div style="font-size:13px; color:#486581; margin-bottom:12px;">
                        <strong>Original Cost:</strong> ₹{project['original_cost_crore']:,.2f} Cr
                    </div>
                    <div style="font-size:13px; color:#486581; margin-bottom:12px;">
                        <strong>Revised Cost:</strong> ₹{project['revised_cost_crore']:,.2f} Cr
                    </div>
                    <div style="font-size:13px; color:#486581;">
                        <strong>Expenditure:</strong> ₹{project['expenditure_crore']:,.2f} Cr
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with detail_col2:
            st.markdown(
                f"""
                <div class="panel">
                    <div style="font-size:16px; font-weight:700; color:#102a43; margin-bottom:18px;">
                        Schedule Details
                    </div>
                    <div style="font-size:13px; color:#486581; margin-bottom:12px;">
                        <strong>Original Completion:</strong> {project['original_completion']}
                    </div>
                    <div style="font-size:13px; color:#486581; margin-bottom:12px;">
                        <strong>Revised Completion:</strong> {project['revised_completion']}
                    </div>
                    <div style="font-size:13px; color:#486581;">
                        <strong>Delay:</strong> {int(project['schedule_delay_months'])} months
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with detail_col3:
            st.markdown(
                f"""
                <div class="panel">
                    <div style="font-size:16px; font-weight:700; color:#102a43; margin-bottom:18px;">
                        Physical Progress
                    </div>
                    <div style="font-size:13px; color:#486581; margin-bottom:12px;">
                        <strong>Current Progress:</strong> {project['physical_progress_pct']:.1f}%
                    </div>
                    <div style="font-size:13px; color:#486581; margin-bottom:12px;">
                        <strong>Progress Gap:</strong> {max(0, 100 - project['physical_progress_pct']):.1f}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(
                min(max(float(project['physical_progress_pct']) / 100, 0), 1)
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Risk drivers

        st.markdown(
            '<div class="section-title">Why is this project risky?</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">Key factors contributing to the current screening score.</div>',
            unsafe_allow_html=True
        )

        risk_drivers = []

        cost_contribution = (
            project["cost_risk_score"] * 0.4
        )

        if project["cost_escalation_pct"] > 0:

            risk_drivers.append(
                f"Cost escalation of "
                f"{project['cost_escalation_pct']:.1f}% "
                f"contributes approximately "
                f"{cost_contribution:.1f} risk points."
            )

        delay_contribution = (
            project["delay_risk_score"] * 0.4
        )

        if project["schedule_delay_months"] > 0:

            risk_drivers.append(
                f"Schedule deviation of "
                f"{int(project['schedule_delay_months'])} months "
                f"contributes approximately "
                f"{delay_contribution:.1f} risk points."
            )

        progress_gap = (
            100 - project["physical_progress_pct"]
        )

        progress_contribution = (
            progress_gap * 0.2
        )

        if project["physical_progress_pct"] < 50:

            risk_drivers.append(
                f"Physical progress is "
                f"{project['physical_progress_pct']:.1f}%, "
                f"creating approximately "
                f"{progress_contribution:.1f} risk points "
                f"from the progress-gap component."
            )

        if not risk_drivers:

            risk_drivers.append(
                "No major risk driver identified by "
                "the current screening rules."
            )

        for driver in risk_drivers:

            st.markdown(
                f"""
                <div class="warning-box warning-high">
                    ⚠ &nbsp; {driver}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Early warning

        st.markdown(
            '<div class="section-title">Early Warning</div>',
            unsafe_allow_html=True
        )

        risk_level = project["risk_level"]

        if risk_level == "Critical":

            warning_class = "warning-critical"

            warning_text = (
                "CRITICAL EARLY WARNING: This project shows multiple "
                "significant risk indicators and should receive "
                "priority monitoring attention."
            )

        elif risk_level == "High":

            warning_class = "warning-high"

            warning_text = (
                "HIGH-RISK EARLY WARNING: This project shows significant "
                "cost, schedule or progress-related risk indicators."
            )

        elif risk_level == "Medium":

            warning_class = "warning-medium"

            warning_text = (
                "MEDIUM-RISK EARLY WARNING: The project shows indicators "
                "that should continue to be monitored."
            )

        else:

            warning_class = "warning-low"

            warning_text = (
                "LOW-RISK STATUS: No major risk signal is identified "
                "by the current screening rules."
            )

        st.markdown(
            f"""
            <div class="warning-box {warning_class}">
                <strong>{warning_text}</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Monitoring focus

        monitoring_focus = []

        if project["cost_escalation_pct"] >= 20:
            monitoring_focus.append("Cost")

        if project["schedule_delay_months"] >= 6:
            monitoring_focus.append("Schedule")

        if project["physical_progress_pct"] < 50:
            monitoring_focus.append("Physical Progress")

        if monitoring_focus:

            st.info(
                "**Recommended monitoring focus:** "
                + " + ".join(monitoring_focus)
            )

        else:

            st.success(
                "**Recommended monitoring focus:** "
                "Routine monitoring"
            )

# All projects

if page == "All Projects":

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">All PAIMANA Projects</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Complete project-level monitoring dataset for the current April 2026 snapshot.</div>',
        unsafe_allow_html=True
    )

    display_columns = [
        "project_name",
        "agency",
        "state",
        "project_code",
        "original_cost_crore",
        "revised_cost_crore",
        "expenditure_crore",
        "physical_progress_pct",
        "cost_escalation_pct",
        "schedule_delay_months",
        "risk_score",
        "risk_level"
    ]

    all_projects = filtered_df[display_columns].copy()

    all_projects.columns = [
        "Project",
        "Agency",
        "State",
        "Project Code",
        "Original Cost (Cr)",
        "Revised Cost (Cr)",
        "Expenditure (Cr)",
        "Physical Progress %",
        "Cost Escalation %",
        "Delay (Months)",
        "Risk Score",
        "Risk Level"
    ]

    st.dataframe(
        all_projects,
        use_container_width=True,
        hide_index=True,
        height=600
    )

# Footer

st.markdown(
    """
    <div class="footer">
        PAIMANA AI • Infrastructure Risk Intelligence
        <br>
        Prototype for SIH 2026 • Based on PAIMANA April 2026 project data
    </div>
    """,
    unsafe_allow_html=True
)
