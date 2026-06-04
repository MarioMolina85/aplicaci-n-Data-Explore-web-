import streamlit as st
import pandas as pd
import sweetviz as sv
import os

# Configuración
st.set_page_config(
    page_title="Análisis Exploratorio de Datos",
    layout="wide"
)

# Encabezado
st.title("📊 Aplicación de Exploracion de Datos y Visualizacion   ")

st.markdown("""
### Informacion personal del Alumno

**Nombre:** Mario Freddy Molina Estrella  
**Asignatura:** Minería de Datos 
**Paralelo:** M2A

---

### Instrucciones de Uso

1. Cargue un archivo CSV o Excel.
""")

# Carga de archivo
archivo = st.file_uploader(
    "Seleccione un archivo CSV o Excel",
    type=["csv", "xlsx"]
)

if archivo is not None:

    # Leer archivo
    if archivo.name.endswith(".csv"):
        df = pd.read_csv(archivo, sep=",", encoding="latin1")
    else:
        df = pd.read_excel(archivo, archivo, sep=",", encoding="latin1")

    st.subheader("Vista Previa del Dataset")
    st.dataframe(df)

    # Información de tipos
    st.subheader("Tipos de Datos")

    tipos = pd.DataFrame({
        "Variable": df.columns,
        "Tipo de Dato": df.dtypes.astype(str)
    })
    st.dataframe(tipos)

    # Estadísticas
    st.subheader("Resumen Estadístico")
    st.dataframe(df.describe())

    # Botón para generar EDA
    with st.spinner("Generando análisis..."):

            reporte = sv.analyze(df)

            reporte.show_html(
                "reporte.html",
                open_browser=False
            )

    st.success("Reporte generado correctamente")

    with open(
            "reporte.html",
            "r",
            encoding="utf-8"
        ) as f:

            html = f.read()

    st.components.v1.html(
            html,
            height=900,
            scrolling=True
        )

       