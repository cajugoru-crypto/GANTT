import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# =========================================================
# CONFIGURACION PAGINA
# =========================================================
st.set_page_config(
    page_title="Planificador Operativo",
    layout="wide"
)

# =========================================================
# TITULO
# =========================================================
st.title("📅 PLANIFICADOR OPERATIVO")
st.caption("Agenda Inteligente de Trabajo")

# =========================================================
# TAREAS
# =========================================================
tareas = [

    # =============================
    # PRIMEROS 5 DIAS
    # =============================
    {
        "Actividad": "Actualizar indicadores productividad OBT",
        "Frecuencia": "Mensual (1-5)",
        "Inicio": "2026-05-01 08:00",
        "Fin": "2026-05-01 10:00",
        "Prioridad": "Alta",
        "Tipo": "Operación"
    },

    {
        "Actividad": "Actualizar indicadores productividad PICKING CO",
        "Frecuencia": "Mensual (1-5)",
        "Inicio": "2026-05-02 08:00",
        "Fin": "2026-05-02 10:00",
        "Prioridad": "Alta",
        "Tipo": "Operación"
    },

    {
        "Actividad": "Actualizar indicadores productividad ALMACEN CO",
        "Frecuencia": "Mensual (1-5)",
        "Inicio": "2026-05-03 08:00",
        "Fin": "2026-05-03 10:00",
        "Prioridad": "Alta",
        "Tipo": "Operación"
    },

    # =============================
    # MITAD DE MES
    # =============================
    {
        "Actividad": "Actualizar ajuste de inventario OBT",
        "Frecuencia": "Mensual (10-15)",
        "Inicio": "2026-05-10 09:00",
        "Fin": "2026-05-10 11:00",
        "Prioridad": "Media",
        "Tipo": "Operación"
    },

    {
        "Actividad": "Actualizar ajuste de inventario ALMACEN CO",
        "Frecuencia": "Mensual (10-15)",
        "Inicio": "2026-05-12 09:00",
        "Fin": "2026-05-12 11:00",
        "Prioridad": "Media",
        "Tipo": "Operación"
    },

    {
        "Actividad": "Indicador ajustes de PICKING CO",
        "Frecuencia": "Mensual (10-15)",
        "Inicio": "2026-05-14 08:00",
        "Fin": "2026-05-14 09:00",
        "Prioridad": "Media",
        "Tipo": "Operación"
    },

    # =============================
    # FINAL DE MES
    # =============================
    {
        "Actividad": "Indicador ajustes de DESGUASE",
        "Frecuencia": "Mensual (20-25)",
        "Inicio": "2026-05-22 08:00",
        "Fin": "2026-05-22 09:00",
        "Prioridad": "Media",
        "Tipo": "Operación"
    },

    # =============================
    # SEMANALES
    # =============================
    {
        "Actividad": "Documentos anulados",
        "Frecuencia": "Semanal",
        "Inicio": "2026-05-05 08:00",
        "Fin": "2026-05-05 09:00",
        "Prioridad": "Alta",
        "Tipo": "Reportes"
    },

    {
        "Actividad": "Documentos pendientes",
        "Frecuencia": "Semanal",
        "Inicio": "2026-05-06 08:00",
        "Fin": "2026-05-06 10:00",
        "Prioridad": "Alta",
        "Tipo": "Reportes"
    },

    # =============================
    # OPERACION
    # =============================
    {
        "Actividad": "Seguimiento RPA",
        "Frecuencia": "Diario",
        "Inicio": "2026-05-01 07:30",
        "Fin": "2026-05-01 08:00",
        "Prioridad": "Alta",
        "Tipo": "Operación"
    },

    {
        "Actividad": "Ocupación sedes veta al paso",
        "Frecuencia": "Mensual",
        "Inicio": "2026-05-16 10:00",
        "Fin": "2026-05-16 11:00",
        "Prioridad": "Media",
        "Tipo": "Reportes"
    },

    # =============================
    # PROYECTO
    # =============================
    {
        "Actividad": "Desarrollo proyecto modelación",
        "Frecuencia": "Variable",
        "Inicio": "2026-05-20 14:00",
        "Fin": "2026-05-20 18:00",
        "Prioridad": "Baja",
        "Tipo": "Proyecto"
    }
]

# =========================================================
# DATAFRAME
# =========================================================
df = pd.DataFrame(tareas)

df["Inicio"] = pd.to_datetime(df["Inicio"])
df["Fin"] = pd.to_datetime(df["Fin"])

# =========================================================
# KPI
# =========================================================
st.markdown("## 📊 Resumen Ejecutivo")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📋 Tareas Totales",
        len(df)
    )

with col2:
    st.metric(
        "🚨 Alta Prioridad",
        len(df[df["Prioridad"] == "Alta"])
    )

with col3:

    horas = (
        (df["Fin"] - df["Inicio"])
        .dt.total_seconds()
        .sum()
        / 3600
    )

    st.metric(
        "⏰ Horas Programadas",
        round(horas, 1)
    )

with col4:
    st.metric(
        "📁 Proyectos",
        len(df[df["Tipo"] == "Proyecto"])
    )

# =========================================================
# DETECCION DE CHOQUES
# =========================================================
choques = []

for i in range(len(df)):
    for j in range(i + 1, len(df)):

        inicio1 = df.loc[i, "Inicio"]
        fin1 = df.loc[i, "Fin"]

        inicio2 = df.loc[j, "Inicio"]
        fin2 = df.loc[j, "Fin"]

        # MISMO DIA + HORAS CRUZADAS
        if (
            inicio1.date() == inicio2.date()
            and inicio1 < fin2
            and inicio2 < fin1
        ):

            choques.append(
                f"⚠️ {df.loc[i, 'Actividad']} "
                f"se cruza con "
                f"{df.loc[j, 'Actividad']}"
            )

# =========================================================
# ALERTAS
# =========================================================
st.markdown("## 🚦 Validación de Agenda")

if choques:

    st.error(
        "Existen actividades cruzadas"
    )

    for c in choques:
        st.write(c)

else:
    st.success(
        "✅ Agenda sin conflictos"
    )

# =========================================================
# GANTT
# =========================================================
st.markdown("## 📅 Cronograma Operativo")

fig = px.timeline(
    df,
    x_start="Inicio",
    x_end="Fin",
    y="Actividad",
    color="Prioridad",
    hover_data=[
        "Frecuencia",
        "Tipo"
    ]
)

fig.update_yaxes(
    autorange="reversed"
)

fig.update_layout(
    height=700,
    title="Cronograma Mensual Operativo",
    xaxis_title="Fecha",
    yaxis_title="Actividad"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# =========================================================
# EXPORTAR HTML
# =========================================================
html_string = fig.to_html()

st.download_button(
    label="📥 Descargar Cronograma HTML",
    data=html_string,
    file_name="cronograma_operativo.html",
    mime="text/html"
)

# =========================================================
# TABLA EDITABLE
# =========================================================
st.markdown("## ✏️ Gestión de Actividades")

editable_df = st.data_editor(
    df,
    num_rows="dynamic",
    width="stretch"
)

# =========================================================
# RESUMEN
# =========================================================
st.markdown("## 📌 Distribución")

resumen = (
    editable_df
    .groupby("Tipo")
    .size()
    .reset_index(name="Cantidad")
)

st.dataframe(
    resumen,
    width="stretch"
)

# =========================================================
# PIE
# =========================================================
st.caption(
    "Planificador operativo dinámico para seguimiento de actividades y carga laboral."
)