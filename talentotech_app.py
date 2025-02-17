import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mtl
import seaborn as sb
import plotly as sns
import datetime as dt
#configuración inicial de la aplicación
st.set_page_config(
  page_title="Dashboard Interactivo",
  page_icon="📊"
  layout="wide"
)
st.title("Dashboard nteractivo con Streamlit")
st.sidebar.title("🔍 Opciones de navegación")
