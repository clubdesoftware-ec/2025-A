import streamlit as st
import Request as rq  # Importa el módulo request que ya contiene la función
import calculadora_funciones as cf
st.set_page_config(layout="wide")

# Título de la aplicación
st.title("Calculadora de Costos de Transporte")
calculadora = st.selectbox("Seleccione el tipo de cálculo", ["Costo de transporte", "Rendimiento de combustible"])
if calculadora == "Costo de transporte":

    # Sección: Datos generales
    st.header("Datos Generales")
    viajes_diarios = st.number_input("Número de viajes diarios", min_value=0, step=1)
    toneladas_por_viaje = st.number_input("Toneladas transportadas por viaje", min_value=0.0, step=0.1)
    km_por_viaje = st.number_input("Kilómetros recorridos por viaje", min_value=0.0, step=0.1)
    tarifa_por_tonelada = st.number_input("Tarifa actual por tonelada", min_value=0.0, step=0.1)

    # Sección: Costos Variables
    st.header("Costos Variables")
    gasto_combustible_anual = st.number_input("Gasto de combustible anual", min_value=0.0, step=0.1)
    gasto_neumaticos_anual = st.number_input("Gasto en neumáticos anual", min_value=0.0, step=0.1)
    gasto_mantenimiento_preventivo_anual = st.number_input("Gasto en mantenimiento preventivo anual", min_value=0.0, step=0.1)
    gasto_mantenimiento_correctivo_anual = st.number_input("Gasto en mantenimiento correctivo anual", min_value=0.0, step=0.1)

    # Sección: Costos Fijos
    st.header("Costos Fijos")
    gastos_anuales_mano_obra = st.number_input("Gastos anuales en mano de obra", min_value=0.0, step=0.01)
    gastos_legalizacion_año = st.number_input("Gastos en legalización al año", min_value=0.0, step=0.01)
    depreciacion_anual = st.number_input("Depreciación anual", min_value=0.0, step=0.1)
    gastos_administrativos_anuales = st.number_input("Gastos administrativos anuales", min_value=0.0, step=0.1)
    costo_inversion = st.number_input("Costos de inversión", min_value=0.0, step=0.1)

elif calculadora == "Rendimiento de combustible":

    # Sección: Rendimiento del combustible por galón
    st.header("Rendimiento del combustible por galón")
    col1, col2 = st.columns([2, 1])
 
    with col1:
        kilometros_dia = st.number_input("Kilómetros recorridos por día (KRdía)",
                                        min_value=0.1, value=100.0, step=0.1)
        
        gasto_diario = st.number_input("Gasto diario en combustible ($) (GCDía)",
                                        min_value=0.1, value=20.0, step=1.0)

    with col2:
        precio_promedio_galon = rq.get_fuel_price()
        with st.container():
            st.write("### Precio Actual del Diesel")
            st.write(f"{precio_promedio_galon}/galón")

    # Sección: Costo de Combustible por Km recorrido
    st.header("Costo de Combustible por Km recorrido")
    col1, col2 = st.columns([2, 1])

    with col1:
        precio_promedio_galon = rq.get_fuel_price()
        with st.container():
                st.write("### Precio Actual del Diesel")
                st.write(f"{precio_promedio_galon}/galón")
    with col2:
        rendimiento_galon = st.number_input("Rendimiento del galón (Km/galón)",
                                                min_value=0.1, value=5.0, step=0.1)

    # Sección: Costo del combustible mensual        
    st.header("Costo del combustible mensual")
    col1, col2 = st.columns([2, 1])

    with col1:
        costo_kilometro_recorrido = st.number_input("Costo por kilómetro recorrido ($)",
                                                    min_value=0.1, value=0.1, step=0.1)
        
    with col2:
        kilometro_recorrido_mes = st.number_input("Kilómetros recorridos al mes",
                                                    min_value=0.1, value=1000.0, step=0.1)
        
    # Sección: Costo del combustible anual
    st.header("Costo del combustible anual")
    col1, col2 = st.columns([2, 1])
        
    with col1:
        kilometro_recorrido_anual = st.number_input("Kilómetros recorridos al año",
                                                    min_value=0.1, value=12000.0, step=0.1)
        
        
        
    




# Botón para calcular
if st.button("Calcular"):   
    st.write("Aquí se mostrarán los resultados del cálculo.")
