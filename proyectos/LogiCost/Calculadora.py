import streamlit as st

# Título de la aplicación
st.title("Calculadora de Costos de Transporte")

# Sección: Datos generales
st.header("Datos Generales")
viajes_diarios = st.number_input("Número de viajes diarios", min_value=0, step=1)
toneladas_por_viaje = st.number_input("Toneladas transportadas por viaje", min_value=0.0, step=0.1)
km_por_viaje = st.number_input("Kilómetros recorridos por viaje", min_value=0.0, step=0.1)
tarifa_por_tonelada = st.number_input("Tarifa actual por tonelada", min_value=0.0, step=0.1)

# Sección: Costos Fijos
st.header("Costos Fijos")
salario_conductor = st.number_input("Salario del conductor", min_value=0.0, step=0.1)
costo_seguros = st.number_input("Costo de seguros", min_value=0.0, step=0.1)
depreciacion_vehiculo = st.number_input("Depreciación del vehículo", min_value=0.0, step=0.1)
costo_matricula = st.number_input("Costo de matrícula", min_value=0.0, step=0.1)
costo_inversion = st.number_input("Costo de inversión", min_value=0.0, step=0.1)

# Sección: Costos Variables
st.header("Costos Variables")
consumo_combustible = st.number_input("Consumo de combustible (litros/km o galones/km)", min_value=0.0, step=0.01)
precio_combustible = st.number_input("Precio del combustible por litro o galón", min_value=0.0, step=0.01)
costo_llantas = st.number_input("Costo de llantas", min_value=0.0, step=0.1)
vida_util_llantas = st.number_input("Vida útil de las llantas (en kilómetros)", min_value=0.0, step=0.1)
costo_mantenimiento = st.number_input("Costos de mantenimiento preventivo y correctivo", min_value=0.0, step=0.1)

# Sección: Rendimiento del combustible por galón
st.header("Rendimiento del combustible por galón")
col1, col2 = st. columns([2, 1])

with col1:
    kilometros_dia = st.number_input("Kilómetros recorridos por día (KRdía)",
                                      min_value=0.1, value=100.0, step=0.1)
    
    gasto_diario = st.number_input("Gasto diario en combustible ($) (GCDía)",
                                    min_value=0.1, value=20.0, step=1.0)
    

    

# Botón para calcular
if st.button("Calcular"):
    st.write("Aquí se mostrarán los resultados del cálculo.")