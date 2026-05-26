import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Operational Planner",
    layout="wide"
)

# =========================================================
# CSS PREMIUM UI
# =========================================================
st.markdown("""
<style>

/* Fondo principal */
.stApp {
    background-color: #F4F7FB;
}

/* Header */
h1 {
    color: #111827 !important;
    font-size: 42px !important;
    font-weight: 800 !important;
    margin-bottom: 0px;
}

h2, h3 {
    color: #1F2937 !important;
    font-weight: 700 !important;
}

/* KPI CARDS */
[data-testid="metric-container"] {

    background: white;

    border-radius: 22px;

    padding: 22px;

    border: 1px solid #E5E7EB;

    box-shadow:
        0px 10px 25px rgba(0,0,0,0.04);

    transition: 0.3s;
}

[data-testid="metric-container"]:hover {

    transform: translateY(-4px);
}

/* Dataframes */
[data-testid="stDataFrame"] {

    background: white;

    border-radius: 22px;

    border: 1px solid #E5E7EB;

    padding: 12px;

    box-shadow:
        0px 10px 25px rgba(0,0,0,0.04);
}

/* Plotly charts */
.element-container:has(.js-plotly-plot) {

    background: white;

    border-radius: 24px;

    padding: 20px;

    border: 1px solid #E5E7EB;

    box-shadow:
        0px 10px 30px rgba(0,0,0,0.04);

    margin-bottom: 20px;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {

    background: linear-gradient(
        135deg,
        #2563EB,
        #1D4ED8
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 12px 22px;

    font-weight: 600;

    transition: 0.3s;
}

.stButton > button:hover,
.stDownloadButton > button:hover {

    transform: scale(1.02);

    box-shadow:
        0px 8px 18px rgba(37,99,235,0.25);
}

/* Alerts */
.stAlert {

    border-radius: 16px;
}

/* Sidebar */
section[data-testid="stSidebar"] {

    background: white;

    border-right: 1px solid #E5E7EB;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA
# =========================================================
tareas = [

    {
        "Actividad": "Actualizar indicadores productividad OBT",
        "Frecuencia": "Mensual (1-5)",
        "Prioridad": "Alta",
        "Duracion": 2,
        "Inicio": 1,
        "Fin": 5
    },

    {
        "Actividad": "Actualizar indicadores productividad PICKING CO",
        "Frecuencia": "Mensual (1-5)",
        "Prioridad": "Alta",
        "Duracion": 2,
        "Inicio": 1,
        "Fin": 5
    },

    {
        "Actividad": "Actualizar indicadores productividad ALMACEN CO",
        "Frecuencia": "Mensual (1-5)",
        "Prioridad": "Alta",
        "Duracion": 2,
        "Inicio": 1,
        "Fin": 5
    },

    {
        "Actividad": "Actualizar ajuste de inventario OBT",
        "Frecuencia": "Mensual (10-15)",
        "Prioridad": "Media",
        "Duracion": 1.5,
        "Inicio": 10,
        "Fin": 15
    },

    {
        "Actividad": "Actualizar ajuste de inventario ALMACEN CO",
        "Frecuencia": "Mensual (10-15)",
        "Prioridad": "Media",
        "Duracion": 1.5,
        "Inicio": 10,
        "Fin": 15
    },

    {
        "Actividad": "Indicador ajustes de PICKING CO",
        "Frecuencia": "Mensual (10-15)",
        "Prioridad": "Media",
        "Duracion": 1,
        "Inicio": 11,
        "Fin": 16
    },

    {
        "Actividad": "Indicador ajustes de DESGUASE",
        "Frecuencia": "Mensual (20-25)",
        "Prioridad": "Media",
        "Duracion": 1,
        "Inicio": 20,
        "Fin": 24
    },

    {
        "Actividad": "Documentos anulados",
        "Frecuencia": "Semanal",
        "Prioridad": "Alta",
        "Duracion": 1,
        "Inicio": 1,
        "Fin": 31
    },

    {
        "Actividad": "Ocupación sedes veta al paso",
        "Frecuencia": "Mensual (15-18)",
        "Prioridad": "Media",
        "Duracion": 1.5,
        "Inicio": 15,
        "Fin": 18
    },

    {
        "Actividad": "Documentos pendientes",
        "Frecuencia": "Semanal",
        "Prioridad": "Alta",
        "Duracion": 1.5,
        "Inicio": 1,
        "Fin": 31
    },

    {
        "Actividad": "Desarrollo proyecto modelación",
        "Frecuencia": "Variable",
        "Prioridad": "Baja",
        "Duracion": 4,
        "Inicio": 1,
        "Fin": 31
    },

    {
        "Actividad": "Seguimiento RPA",
        "Frecuencia": "Diario",
        "Prioridad": "Alta",
        "Duracion": 0.5,
        "Inicio": 1,
        "Fin": 31
    }
]

df = pd.DataFrame(tareas)

# =========================================================
# HEADER
# =========================================================
st.title("📅 Operational Planner")

st.caption(
    "Executive workload management dashboard"
)

st.divider()

# =========================================================
# KPI CARDS
# =========================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "TASKS",
        len(df)
    )

with col2:
    st.metric(
        "HIGH PRIORITY",
        len(df[df["Prioridad"] == "Alta"])
    )

with col3:
    st.metric(
        "SCHEDULED HOURS",
        f"{round(df['Duracion'].sum(),1)} h"
    )

with col4:
    st.metric(
        "MONTHLY TASKS",
        len(df[df["Frecuencia"].str.contains("Mensual")])
    )

# =========================================================
# MAIN LAYOUT
# =========================================================
left, right = st.columns([1, 2])

# =========================================================
# TASK TABLE
# =========================================================
with left:

    st.subheader("📋 Tasks")

    st.dataframe(

        df[
            [
                "Actividad",
                "Frecuencia",
                "Prioridad",
                "Duracion"
            ]
        ],

        height=750,

        width=700
    )

# =========================================================
# EXECUTIVE ROADMAP
# =========================================================
with right:

    st.subheader("📆 Executive Roadmap")

    fig = go.Figure()

    colores = {

        "Alta": "#FF5A5F",

        "Media": "#F4B400",

        "Baja": "#34A853"
    }

    for _, row in df.iterrows():

        fig.add_trace(

            go.Bar(

                x=[row["Fin"] - row["Inicio"] + 1],

                y=[row["Actividad"]],

                base=[row["Inicio"]],

                orientation='h',

                marker=dict(

                    color=colores[row["Prioridad"]],

                    line=dict(
                        color="rgba(255,255,255,0.9)",
                        width=1.5
                    )
                ),

                hovertemplate=
                f"""
                <b>{row['Actividad']}</b><br>
                Priority: {row['Prioridad']}<br>
                Frequency: {row['Frecuencia']}<br>
                Duration: {row['Duracion']} h
                """
            )
        )

    fig.update_layout(

        height=820,

        barmode='overlay',

        plot_bgcolor='#FFFFFF',

        paper_bgcolor='#FFFFFF',

        font=dict(
            family="Segoe UI",
            size=13,
            color="#111827"
        ),

        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10
        ),

        xaxis=dict(

            title='MAY 2026',

            tickmode='linear',

            dtick=1,

            showgrid=True,

            gridcolor='rgba(0,0,0,0.05)',

            zeroline=False,

            range=[0.5, 31.5]
        ),

        yaxis=dict(

            showgrid=False,

            automargin=True,

            categoryorder='total ascending'
        ),

        showlegend=False
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

# =========================================================
# WORKLOAD ANALYSIS
# =========================================================
st.divider()

st.subheader("📊 Workload Analysis")

carga = []

for dia in range(1, 32):

    total = 0

    for _, row in df.iterrows():

        if row["Inicio"] <= dia <= row["Fin"]:

            total += row["Duracion"]

    carga.append(total)

carga_df = pd.DataFrame({

    "Dia": list(range(1, 32)),

    "Horas": carga
})

fig2 = go.Figure()

fig2.add_trace(

    go.Scatter(

        x=carga_df["Dia"],

        y=carga_df["Horas"],

        mode='lines+markers',

        line=dict(
            width=4,
            color='#2563EB'
        ),

        marker=dict(
            size=8
        ),

        fill='tozeroy'
    )
)

fig2.add_hline(

    y=8,

    line_dash="dash",

    line_color="red"
)

fig2.update_layout(

    height=380,

    plot_bgcolor='#FFFFFF',

    paper_bgcolor='#FFFFFF',

    title="Daily Workload Capacity",

    font=dict(
        family="Segoe UI",
        size=13,
        color="#111827"
    )
)

st.plotly_chart(
    fig2,
    width='stretch'
)

# =========================================================
# ALERTS
# =========================================================
st.divider()

st.subheader("🚨 Capacity Alerts")

dias_saturados = carga_df[carga_df["Horas"] > 8]

if len(dias_saturados) > 0:

    st.warning(
        f"⚠️ {len(dias_saturados)} overloaded days detected."
    )

    st.dataframe(dias_saturados)

else:

    st.success("✅ Workload balanced.")

# =========================================================
# EXPORT
# =========================================================
st.divider()

st.subheader("📥 Export")

csv = df.to_csv(index=False)

st.download_button(

    label="Download CSV",

    data=csv,

    file_name="operational_planner.csv",

    mime="text/csv"
)

# =========================================================
# FOOTER
# =========================================================
st.caption(
    "Tasks are dynamically distributed based on workload and operational frequency."
)
