import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Dashboard Gantt",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

.stApp {
    background-color: #F5F7FB;
    font-family: 'Segoe UI';
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: white;
    border-right: 1px solid #ECEEF5;
    width: 260px !important;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
}

.sidebar-title {
    font-size: 30px;
    font-weight: 800;
    color: white;
    background: linear-gradient(135deg,#5B3DF5,#3B82F6);
    width: 95px;
    height: 95px;
    border-radius: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 30px;
}

.menu-item {
    padding: 16px 20px;
    border-radius: 16px;
    margin-bottom: 12px;
    font-size: 20px;
    color: #4B5563;
}

.active-menu {
    background: #EEF2FF;
    color: #4F46E5;
    font-weight: 700;
}

/* TITULOS */
.main-title {
    font-size: 54px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 24px;
    color: #6B7280;
    margin-top: -10px;
    margin-bottom: 30px;
}

/* CARDS */
.metric-card {
    background: white;
    padding: 30px;
    border-radius: 24px;
    border: 1px solid #ECEEF5;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.04);
}

.metric-title {
    color: #6B7280;
    font-size: 18px;
    margin-bottom: 15px;
}

.metric-value {
    color: #1D4ED8;
    font-size: 54px;
    font-weight: 800;
}

.metric-small {
    color: #111827;
    font-size: 42px;
    font-weight: 800;
}

.metric-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    margin-top: 15px;
}

/* GANTT */
.gantt-container {
    background: white;
    border-radius: 28px;
    padding: 25px;
    border: 1px solid #ECEEF5;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.04);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown(
        """
        <div class='sidebar-title'>1</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style='font-size:34px;font-weight:800;color:#111827;margin-bottom:35px;'>
        ProjectPlanner
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='menu-item'>🏠 Resumen</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item active-menu'>📋 Gantt</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>📁 Tareas</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>📅 Calendario</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>👥 Recursos</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>📈 Reportes</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>⚙️ Configuración</div>", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <div class='main-title'>Dashboard Gantt</div>
    <div class='subtitle'>Vista general del proyecto</div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DATA
# =========================================================
df = pd.DataFrame([
    {
        "Tarea": "Análisis del proyecto",
        "Inicio": "01 May",
        "Semana": 1,
        "Duracion": 1,
        "Color": "#1565FF"
    },
    {
        "Tarea": "Planificación",
        "Inicio": "03 May",
        "Semana": 1.4,
        "Duracion": 1,
        "Color": "#11B8E5"
    },
    {
        "Tarea": "Diseño de la solución",
        "Inicio": "05 May",
        "Semana": 1.8,
        "Duracion": 1,
        "Color": "#7C3AED"
    },
    {
        "Tarea": "Desarrollo",
        "Inicio": "08 May",
        "Semana": 2.4,
        "Duracion": 1,
        "Color": "#F032C2"
    },
    {
        "Tarea": "Pruebas",
        "Inicio": "18 May",
        "Semana": 3,
        "Duracion": 1,
        "Color": "#FFA412"
    },
    {
        "Tarea": "Implementación",
        "Inicio": "22 May",
        "Semana": 3.9,
        "Duracion": 0.8,
        "Color": "#69D340"
    },
    {
        "Tarea": "Cierre del proyecto",
        "Inicio": "28 May",
        "Semana": 4.4,
        "Duracion": 0.6,
        "Color": "#0EA5C6"
    }
])

# =========================================================
# GANTT
# =========================================================
st.markdown("<div class='gantt-container'>", unsafe_allow_html=True)

fig = go.Figure()

for _, row in df.iterrows():

    fig.add_trace(
        go.Bar(
            x=[row["Duracion"]],
            y=[row["Tarea"]],
            base=[row["Semana"]],
            orientation='h',
            marker=dict(
                color=row["Color"]
            ),
            width=0.42,
            hoverinfo='none'
        )
    )

fig.update_layout(
    height=620,
    bargap=0.45,
    showlegend=False,
    barmode='overlay',
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin=dict(l=40, r=40, t=80, b=30),

    font=dict(
        family='Segoe UI',
        size=16,
        color='#111827'
    ),

    xaxis=dict(
        range=[0.8, 5],
        tickvals=[1.5, 2.5, 3.5, 4.5],

        ticktext=[
            'Semana 1<br>01 May - 07 May',
            'Semana 2<br>08 May - 14 May',
            'Semana 3<br>15 May - 21 May',
            'Semana 4<br>22 May - 31 May'
        ],

        showgrid=True,
        gridcolor='#EEF2F7',
        zeroline=False,
        side='top'
    ),

    yaxis=dict(
        autorange='reversed',
        showgrid=True,
        gridcolor='#F3F4F6'
    ),

    annotations=[
        dict(
            text='Mayo 2026',
            x=2.9,
            y=1.16,
            xref='x',
            yref='paper',
            showarrow=False,

            font=dict(
                size=20,
                color='#111827',
                family='Segoe UI'
            )
        )
    ]
)

st.plotly_chart(
    fig,
    width='stretch'
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# KPI CARDS
# =========================================================
col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(
        """
        <div class='metric-card'>
            <div class='metric-title'>Progreso general</div>
            <div class='metric-value'>65%</div>

            <div style='margin-top:20px;height:12px;background:#EEF2F7;border-radius:20px;'>
                <div style='width:65%;height:12px;background:#1565FF;border-radius:20px;'></div>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class='metric-card'>
            <div class='metric-title'>Tareas completadas</div>
            <div class='metric-small'>13 / 20</div>
            <div class='metric-dot' style='background:#4ADE80;'></div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class='metric-card'>
            <div class='metric-title'>En progreso</div>
            <div class='metric-small'>4</div>
            <div class='metric-dot' style='background:#F59E0B;'></div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        """
        <div class='metric-card'>
            <div class='metric-title'>Pendientes</div>
            <div class='metric-small'>3</div>
            <div class='metric-dot' style='background:#FF4D4F;'></div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br><br>", unsafe_allow_html=True)

st.caption("Dashboard ejecutivo estilo Gantt moderno")
