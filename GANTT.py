import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import calendar

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Planificador Operativo",
    layout="wide"
)

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
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Actualizar indicadores productividad PICKING CO",
        "Frecuencia": "Mensual (1-5)",
        "Prioridad": "Alta",
        "Duracion": 2,
        "Inicio": 1,
        "Fin": 5,
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Actualizar indicadores productividad ALMACEN CO",
        "Frecuencia": "Mensual (1-5)",
        "Prioridad": "Alta",
        "Duracion": 2,
        "Inicio": 1,
        "Fin": 5,
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Actualizar ajuste de inventario OBT",
        "Frecuencia": "Mensual (10-15)",
        "Prioridad": "Media",
        "Duracion": 1.5,
        "Inicio": 10,
        "Fin": 15,
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Actualizar ajuste de inventario ALMACEN CO",
        "Frecuencia": "Mensual (10-15)",
        "Prioridad": "Media",
        "Duracion": 1.5,
        "Inicio": 10,
        "Fin": 15,
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Indicador ajustes de PICKING CO",
        "Frecuencia": "Mensual (10-15)",
        "Prioridad": "Media",
        "Duracion": 1,
        "Inicio": 11,
        "Fin": 16,
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Indicador ajustes de DESGUASE",
        "Frecuencia": "Mensual (20-25)",
        "Prioridad": "Media",
        "Duracion": 1,
        "Inicio": 20,
        "Fin": 24,
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Documentos anulados",
        "Frecuencia": "Semanal",
        "Prioridad": "Alta",
        "Duracion": 1,
        "Inicio": 1,
        "Fin": 31,
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Ocupación sedes veta al paso",
        "Frecuencia": "Mensual (15-18)",
        "Prioridad": "Media",
        "Duracion": 1.5,
        "Inicio": 15,
        "Fin": 18,
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Documentos pendientes",
        "Frecuencia": "Semanal",
        "Prioridad": "Alta",
        "Duracion": 1.5,
        "Inicio": 1,
        "Fin": 31,
        "Tipo": "Operacion"
    },
    {
        "Actividad": "Desarrollo proyecto modelación",
        "Frecuencia": "Variable",
        "Prioridad": "Baja",
        "Duracion": 4,
        "Inicio": 1,
        "Fin": 31,
        "Tipo": "Proyecto"
    },
    {
        "Actividad": "Seguimiento RPA",
        "Frecuencia": "Diario",
        "Prioridad": "Alta",
        "Duracion": 0.5,
        "Inicio": 1,
        "Fin": 31,
        "Tipo": "Operacion"
    }
]

df = pd.DataFrame(tareas)

# =========================================================
# HEADER
# =========================================================
st.markdown("""
    <h1 style='color:#0B1F5E; margin-bottom:0;'>
    📅 PLANIFICADOR OPERATIVO
    </h1>
""", unsafe_allow_html=True)

st.markdown("### Agenda Inteligente")

# =========================================================
# KPIs
# =========================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("TAREAS TOTALES", len(df))

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
        "PROYECTOS",
        len(df[df["Tipo"] == "Proyecto"])
    )

st.divider()

# =========================================================
# LAYOUT
# =========================================================
left, right = st.columns([1.1, 1.9])

# =========================================================
# TABLA IZQUIERDA
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
        height=600,
        width=700
    )

# =========================================================
# GANTT
# =========================================================
with right:

    st.subheader("CRONOGRAMA - MAYO 2026")

    fig = go.Figure()

    colores = {
        "Alta": "#EF4444",
        "Media": "#F59E0B",
        "Baja": "#22C55E"
    }

    for idx, row in df.iterrows():

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
                Duración: {row['Duracion']} h
                """
            )
        )

    fig.update_layout(
        height=650,
        barmode='overlay',
        plot_bgcolor='white',
        paper_bgcolor='white',
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
# RESUMEN
# =========================================================
st.divider()

col5, col6 = st.columns([1.5, 1])

# =========================================================
# CARGA
# =========================================================
with col5:

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
        title="CARGA DE TRABAJO POR DÍA",
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=350
    )

    st.plotly_chart(
        fig2,
        width='stretch'
    )

# =========================================================
# ESTADO
# =========================================================
with col6:

    st.subheader("ESTADO")

    st.success("✅ En tiempo: 9")
    st.warning("⚠️ En proceso: 2")
    st.error("❌ Pendiente: 3")

    st.divider()

    st.subheader("RESUMEN")

    resumen = df.groupby("Tipo")["Duracion"].sum()

    st.dataframe(resumen)

# =========================================================
# EXPORTAR
# =========================================================
st.divider()

st.subheader("EXPORTAR")

st.download_button(
    label="📥 Descargar CSV",
    data=df.to_csv(index=False),
    file_name="planificador_operativo.csv",
    mime="text/csv"
)

# =========================================================
# FOOTER
# =========================================================
st.caption(
    "Las tareas se programan automáticamente según prioridad y frecuencia."
)
