import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# =========================================================
# CONFIGURACION
# =========================================================
st.set_page_config(
    page_title="Planificador Operativo",
    layout="wide"
)

# =========================================================
# ESTILOS PRO
# =========================================================
st.markdown("""
<style>

/* Fondo principal */
.stApp {
    background-color: #F5F7FB;
}

/* Títulos */
h1 {
    color: #0F172A !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #1E293B !important;
    font-weight: 700 !important;
}

/* KPI Cards */
[data-testid="metric-container"] {
    background: white;
    border-radius: 18px;
    padding: 20px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background: white;
    border-radius: 18px;
    border: 1px solid #E2E8F0;
    padding: 10px;
}

/* Botones */
.stButton > button {
    background: linear-gradient(
        135deg,
        #2563EB,
        #1D4ED8
    );

    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 20px;
    font-weight: 600;
}

/* Download Button */
.stDownloadButton > button {
    background: linear-gradient(
        135deg,
        #2563EB,
        #1D4ED8
    );

    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 20px;
    font-weight: 600;
}

/* Charts */
.js-plotly-plot {
    background: white !important;
    border-radius: 18px;
    padding: 10px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

/* Alertas */
.stAlert {
    border-radius: 14px;
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
        "Fin": 5,
    },
    {
        "Actividad": "Actualizar indicadores productividad PICKING CO",
        "Frecuencia": "Mensual (1-5)",
        "Prioridad": "Alta",
        "Duracion": 2,
        "Inicio": 1,
        "Fin": 5,
    },
    {
        "Actividad": "Actualizar indicadores productividad ALMACEN CO",
        "Frecuencia": "Mensual (1-5)",
        "Prioridad": "Alta",
        "Duracion": 2,
        "Inicio": 1,
        "Fin": 5,
    },
    {
        "Actividad": "Actualizar ajuste de inventario OBT",
        "Frecuencia": "Mensual (10-15)",
        "Prioridad": "Media",
        "Duracion": 1.5,
        "Inicio": 10,
        "Fin": 15,
    },
    {
        "Actividad": "Actualizar ajuste de inventario ALMACEN CO",
        "Frecuencia": "Mensual (10-15)",
        "Prioridad": "Media",
        "Duracion": 1.5,
        "Inicio": 10,
        "Fin": 15,
    },
    {
        "Actividad": "Indicador ajustes de PICKING CO",
        "Frecuencia": "Mensual (10-15)",
        "Prioridad": "Media",
        "Duracion": 1,
        "Inicio": 11,
        "Fin": 16,
    },
    {
        "Actividad": "Indicador ajustes de DESGUASE",
        "Frecuencia": "Mensual (20-25)",
        "Prioridad": "Media",
        "Duracion": 1,
        "Inicio": 20,
        "Fin": 24,
    },
    {
        "Actividad": "Documentos anulados",
        "Frecuencia": "Semanal",
        "Prioridad": "Alta",
        "Duracion": 1,
        "Inicio": 1,
        "Fin": 31,
    },
    {
        "Actividad": "Ocupación sedes veta al paso",
        "Frecuencia": "Mensual (15-18)",
        "Prioridad": "Media",
        "Duracion": 1.5,
        "Inicio": 15,
        "Fin": 18,
    },
    {
        "Actividad": "Documentos pendientes",
        "Frecuencia": "Semanal",
        "Prioridad": "Alta",
        "Duracion": 1.5,
        "Inicio": 1,
        "Fin": 31,
    },
    {
        "Actividad": "Desarrollo proyecto modelación",
        "Frecuencia": "Variable",
        "Prioridad": "Baja",
        "Duracion": 4,
        "Inicio": 1,
        "Fin": 31,
    },
    {
        "Actividad": "Seguimiento RPA",
        "Frecuencia": "Diario",
        "Prioridad": "Alta",
        "Duracion": 0.5,
        "Inicio": 1,
        "Fin": 31,
    }
]

df = pd.DataFrame(tareas)

# =========================================================
# TITULO
# =========================================================
st.title("📅 PLANIFICADOR OPERATIVO")
st.caption("Agenda inteligente de trabajo")

# =========================================================
# KPIs
# =========================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "TAREAS TOTALES",
        len(df)
    )

with col2:
    st.metric(
        "ALTA PRIORIDAD",
        len(df[df["Prioridad"] == "Alta"])
    )

with col3:
    st.metric(
        "HORAS PROGRAMADAS",
        f"{round(df['Duracion'].sum(),1)} h"
    )

with col4:
    st.metric(
        "ACTIVIDADES MENSUALES",
        len(df[df["Frecuencia"].str.contains("Mensual")])
    )

st.divider()

# =========================================================
# LAYOUT PRINCIPAL
# =========================================================
left, right = st.columns([1.1, 1.9])

# =========================================================
# TABLA
# =========================================================
with left:

    st.subheader("ACTIVIDADES")

    st.dataframe(
        df[
            [
                "Actividad",
                "Frecuencia",
                "Prioridad",
                "Duracion"
            ]
        ],
        height=650,
        width=700
    )

# =========================================================
# GANTT
# =========================================================
with right:

    st.subheader("CRONOGRAMA OPERATIVO")

    fig = go.Figure()

    colores = {
        "Alta": "#EF4444",
        "Media": "#F59E0B",
        "Baja": "#22C55E"
    }

    for _, row in df.iterrows():

        fig.add_trace(
            go.Bar(
                x=[row["Fin"] - row["Inicio"] + 1],
                y=[row["Actividad"]],
                base=[row["Inicio"]],
                orientation='h',

                marker=dict(
                    color=colores[row["Prioridad"]]
                ),

                hovertemplate=
                f"""
                <b>{row['Actividad']}</b><br>
                Prioridad: {row['Prioridad']}<br>
                Frecuencia: {row['Frecuencia']}<br>
                Duración: {row['Duracion']} horas
                """
            )
        )

    fig.update_layout(

        height=700,

        barmode='overlay',

        plot_bgcolor='#FFFFFF',

        paper_bgcolor='#F5F7FB',

        font=dict(
            family="Arial",
            size=13,
            color="#1E293B"
        ),

        xaxis=dict(
            title='Días del mes',
            tickmode='linear',
            dtick=1,
            range=[0, 32]
        ),

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )

# =========================================================
# CARGA DIARIA
# =========================================================
st.divider()

st.subheader("📊 CARGA DE TRABAJO")

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
    go.Bar(
        x=carga_df["Dia"],
        y=carga_df["Horas"]
    )
)

fig2.add_hline(
    y=8,
    line_dash="dash",
    line_color="red"
)

fig2.update_layout(

    height=350,

    plot_bgcolor='#FFFFFF',

    paper_bgcolor='#F5F7FB',

    font=dict(
        family="Arial",
        size=13,
        color="#1E293B"
    ),

    title="Carga de trabajo por día"
)

st.plotly_chart(
    fig2,
    width='stretch'
)

# =========================================================
# ALERTAS
# =========================================================
st.divider()

st.subheader("🚨 ALERTAS")

dias_saturados = carga_df[carga_df["Horas"] > 8]

if len(dias_saturados) > 0:

    st.warning(
        f"⚠️ Hay {len(dias_saturados)} días con sobrecarga."
    )

    st.dataframe(dias_saturados)

else:

    st.success("✅ No hay sobrecarga.")

# =========================================================
# DESCARGA
# =========================================================
st.divider()

st.subheader("📥 EXPORTAR")

csv = df.to_csv(index=False)

st.download_button(
    label="Descargar CSV",
    data=csv,
    file_name="planificador_operativo.csv",
    mime="text/csv"
)

# =========================================================
# FOOTER
# =========================================================
st.caption(
    "Las tareas se organizan automáticamente según prioridad y frecuencia."
)
