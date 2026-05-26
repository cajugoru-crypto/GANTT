import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ======================================================
# CONFIG
# ======================================================
st.set_page_config(
    page_title="Dashboard Gantt",
    layout="wide"
)

# ======================================================
# CSS
# ======================================================
st.markdown("""
<style>

.stApp {
    background-color: #F5F7FB;
}

/* Cards */
[data-testid="metric-container"] {

    background: white;

    border-radius: 20px;

    padding: 20px;

    border: 1px solid #ECEEF5;

    box-shadow:
        0px 4px 12px rgba(0,0,0,0.04);
}

/* Data editor */
[data-testid="stDataEditor"] {

    border-radius: 20px;

    overflow: hidden;

    border: 1px solid #ECEEF5;
}

/* Plotly */
.element-container:has(.js-plotly-plot) {

    background: white;

    padding: 20px;

    border-radius: 24px;

    border: 1px solid #ECEEF5;

    box-shadow:
        0px 4px 12px rgba(0,0,0,0.04);
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================
with st.sidebar:

    st.title("📋 ProjectPlanner")

    menu = st.radio(

        "Navegación",

        [
            "Dashboard",
            "Calendario",
            "Reportes",
            "Configuración"
        ]
    )

# ======================================================
# DATA
# ======================================================
if "tasks" not in st.session_state:

    st.session_state.tasks = pd.DataFrame([

        {
            "Tarea": "Indicadores productividad OBT",
            "Semana": 1,
            "Duracion": 1,
            "Estado": "En progreso",
            "Prioridad": "Alta",
            "Color": "#1565FF"
        },

        {
            "Tarea": "Indicadores PICKING CO",
            "Semana": 1.5,
            "Duracion": 1,
            "Estado": "Pendiente",
            "Prioridad": "Alta",
            "Color": "#7C3AED"
        },

        {
            "Tarea": "Seguimiento RPA",
            "Semana": 2,
            "Duracion": 1,
            "Estado": "En progreso",
            "Prioridad": "Media",
            "Color": "#F032C2"
        },

        {
            "Tarea": "Proyecto modelación",
            "Semana": 3,
            "Duracion": 1.5,
            "Estado": "Pendiente",
            "Prioridad": "Media",
            "Color": "#FFA412"
        },

        {
            "Tarea": "Documentos pendientes",
            "Semana": 4,
            "Duracion": 1,
            "Estado": "Pendiente",
            "Prioridad": "Alta",
            "Color": "#34A853"
        }

    ])

df = st.session_state.tasks

# ======================================================
# HEADER
# ======================================================
st.title("📆 Dashboard Gantt")
st.caption("Gestión inteligente de carga operativa")

# ======================================================
# KPIs
# ======================================================
k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Total tareas",
        len(df)
    )

with k2:
    st.metric(
        "Alta prioridad",
        len(df[df["Prioridad"] == "Alta"])
    )

with k3:
    st.metric(
        "En progreso",
        len(df[df["Estado"] == "En progreso"])
    )

with k4:
    st.metric(
        "Horas planificadas",
        round(df["Duracion"].sum(), 1)
    )

st.markdown("##")

# ======================================================
# LAYOUT
# ======================================================
left, right = st.columns([1, 1.8])

# ======================================================
# TABLA
# ======================================================
with left:

    st.subheader("📋 Gestión de tareas")

    edited_df = st.data_editor(

        df,

        use_container_width=True,

        num_rows="dynamic",

        height=600,

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
                max_value=5.0,
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

# ======================================================
# GANTT
# ======================================================
with right:

    st.subheader("📆 Roadmap operativo")

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
                Duración: {row['Duracion']}h
                <extra></extra>
                """
            )
        )

    fig.update_layout(

        height=700,

        barmode='overlay',

        showlegend=False,

        plot_bgcolor='white',

        paper_bgcolor='white',

        font=dict(
            family="Segoe UI",
            size=14,
            color="#111827"
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        xaxis=dict(

            range=[0.8, 5],

            tickvals=[1.5, 2.5, 3.5, 4.5],

            ticktext=[

                "Semana 1",
                "Semana 2",
                "Semana 3",
                "Semana 4"
            ],

            side='top',

            showgrid=True,

            gridcolor='#EEF2F7',

            zeroline=False
        ),

        yaxis=dict(

            autorange='reversed',

            showgrid=True,

            gridcolor='#F3F4F6'
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# EXPORT
# ======================================================
st.markdown("##")

csv = edited_df.to_csv(index=False)

st.download_button(

    label="📥 Descargar CSV",

    data=csv,

    file_name="dashboard_gantt.csv",

    mime="text/csv"
)
