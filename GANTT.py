import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Dashboard Gantt",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================
if "tasks" not in st.session_state:

    st.session_state.tasks = pd.DataFrame([

        {
            "Tarea": "Actualizar indicadores productividad OBT",
            "Semana": 1,
            "Duracion": 1,
            "Estado": "En progreso",
            "Prioridad": "Alta",
            "Color": "#1565FF"
        },

        {
            "Tarea": "Actualizar indicadores productividad PICKING CO",
            "Semana": 1.5,
            "Duracion": 1,
            "Estado": "Pendiente",
            "Prioridad": "Alta",
            "Color": "#11B8E5"
        },

        {
            "Tarea": "Seguimiento RPA",
            "Semana": 2,
            "Duracion": 1,
            "Estado": "En progreso",
            "Prioridad": "Media",
            "Color": "#7C3AED"
        },

        {
            "Tarea": "Desarrollo proyecto modelación",
            "Semana": 3,
            "Duracion": 1.3,
            "Estado": "Pendiente",
            "Prioridad": "Media",
            "Color": "#F032C2"
        },

        {
            "Tarea": "Documentos pendientes",
            "Semana": 4,
            "Duracion": 0.8,
            "Estado": "Pendiente",
            "Prioridad": "Alta",
            "Color": "#FFA412"
        }

    ])

# =========================================================
# CSS PRO
# =========================================================
st.markdown("""
<style>

.stApp {
    background-color: #F5F7FB;
    font-family: 'Segoe UI';
}

/* HEADER */
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
}

.sidebar-logo {

    width: 90px;
    height: 90px;

    border-radius: 22px;

    background: linear-gradient(
        135deg,
        #5B3DF5,
        #3B82F6
    );

    display: flex;

    align-items: center;

    justify-content: center;

    color: white;

    font-size: 34px;

    font-weight: 800;

    margin-bottom: 25px;
}

.menu-item {

    padding: 16px 18px;

    border-radius: 16px;

    margin-bottom: 10px;

    font-size: 18px;

    color: #6B7280;
}

.active-menu {

    background: #EEF2FF;

    color: #4F46E5;

    font-weight: 700;
}

/* TITLES */
.main-title {

    font-size: 52px;

    font-weight: 800;

    color: #111827;

    margin-bottom: 0px;
}

.sub-title {

    font-size: 22px;

    color: #6B7280;

    margin-top: -8px;

    margin-bottom: 35px;
}

/* KPI */
.kpi-card {

    background: white;

    border-radius: 24px;

    padding: 25px;

    border: 1px solid #ECEEF5;

    box-shadow:
        0px 8px 20px rgba(0,0,0,0.04);
}

.kpi-title {

    color: #6B7280;

    font-size: 16px;
}

.kpi-value {

    color: #111827;

    font-size: 42px;

    font-weight: 800;
}

/* CONTAINERS */
.block-container {
    padding-top: 2rem;
}

/* DATA EDITOR */
[data-testid="stDataEditor"] {

    border-radius: 22px;

    overflow: hidden;

    border: 1px solid #ECEEF5;
}

/* CHART */
.chart-container {

    background: white;

    border-radius: 28px;

    padding: 20px;

    border: 1px solid #ECEEF5;

    box-shadow:
        0px 8px 20px rgba(0,0,0,0.04);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown(
        """
        <div class='sidebar-logo'>
        1
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style='font-size:34px;
                    font-weight:800;
                    color:#111827;
                    margin-bottom:35px;'>

        ProjectPlanner

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='menu-item active-menu'>📋 Dashboard</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='menu-item'>📅 Calendario</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='menu-item'>📈 Reportes</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='menu-item'>⚙️ Configuración</div>",
        unsafe_allow_html=True
    )

# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <div class='main-title'>
    Dashboard Gantt
    </div>

    <div class='sub-title'>
    Gestión inteligente de carga operativa
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# KPIs
# =========================================================
df = st.session_state.tasks

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(
        f"""
        <div class='kpi-card'>
            <div class='kpi-title'>
            Total tareas
            </div>

            <div class='kpi-value'>
            {len(df)}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        f"""
        <div class='kpi-card'>
            <div class='kpi-title'>
            Alta prioridad
            </div>

            <div class='kpi-value'>
            {len(df[df['Prioridad']=='Alta'])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        f"""
        <div class='kpi-card'>
            <div class='kpi-title'>
            En progreso
            </div>

            <div class='kpi-value'>
            {len(df[df['Estado']=='En progreso'])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        f"""
        <div class='kpi-card'>
            <div class='kpi-title'>
            Horas planificadas
            </div>

            <div class='kpi-value'>
            {round(df['Duracion'].sum(),1)}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# LAYOUT
# =========================================================
left, right = st.columns([1, 1.8])

# =========================================================
# TABLA INTERACTIVA
# =========================================================
with left:

    st.subheader("📋 Gestión de tareas")

    edited_df = st.data_editor(

        df,

        num_rows="dynamic",

        use_container_width=True,

        height=620,

        column_config={

            "Tarea": st.column_config.TextColumn(
                "Tarea"
            ),

            "Semana": st.column_config.NumberColumn(
                "Semana",
                min_value=1.0,
                max_value=4.5,
                step=0.1
            ),

            "Duracion": st.column_config.NumberColumn(
                "Duración",
                min_value=0.1,
                max_value=4.0,
                step=0.1
            ),

            "Estado": st.column_config.SelectboxColumn(
                "Estado",
                options=[
                    "Pendiente",
                    "En progreso",
                    "Terminado"
                ]
            ),

            "Prioridad": st.column_config.SelectboxColumn(
                "Prioridad",
                options=[
                    "Alta",
                    "Media",
                    "Baja"
                ]
            ),

            "Color": st.column_config.TextColumn(
                "Color HEX"
            )
        }
    )

    st.session_state.tasks = edited_df

# =========================================================
# GANTT
# =========================================================
with right:

    st.subheader("📆 Roadmap operativo")

    st.markdown(
        "<div class='chart-container'>",
        unsafe_allow_html=True
    )

    fig = go.Figure()

    for _, row in edited_df.iterrows():

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

                hovertemplate=
                f"""
                <b>{row['Tarea']}</b><br>
                Estado: {row['Estado']}<br>
                Prioridad: {row['Prioridad']}<br>
                Duración: {row['Duracion']}<extra></extra>
                """
            )
        )

    fig.update_layout(

        height=700,

        bargap=0.45,

        showlegend=False,

        barmode='overlay',

        plot_bgcolor='white',

        paper_bgcolor='white',

        margin=dict(
            l=40,
            r=40,
            t=80,
            b=30
        ),

        font=dict(
            family='Segoe UI',
            size=15,
            color='#111827'
        ),

        xaxis=dict(

            range=[0.8, 5],

            tickvals=[1.5, 2.5, 3.5, 4.5],

            ticktext=[

                'Semana 1<br>01 - 07',

                'Semana 2<br>08 - 14',

                'Semana 3<br>15 - 21',

                'Semana 4<br>22 - 31'
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

                text='MAYO 2026',

                x=2.9,

                y=1.15,

                xref='x',

                yref='paper',

                showarrow=False,

                font=dict(

                    size=22,

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

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# =========================================================
# EXPORT
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

csv = edited_df.to_csv(index=False)

st.download_button(

    label="📥 Descargar CSV",

    data=csv,

    file_name="dashboard_gantt.csv",

    mime="text/csv"
)

# =========================================================
# FOOTER
# =========================================================
st.caption(
    "Dashboard operativo interactivo estilo SaaS"
)
