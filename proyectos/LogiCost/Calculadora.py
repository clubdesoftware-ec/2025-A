import streamlit as st
import Request as rq  # Importa el módulo request que ya contiene la función
import calculadora_funciones as cf

st.set_page_config(layout="wide")

# Título de la aplicación
st.title("Calculadora de Costos de Transporte")
calculadora = st.selectbox("Seleccione el tipo de cálculo", ["Costo de transporte", "Rendimiento de combustible"])
if calculadora == "Costo de transporte":

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

    if st.button("Calcular"):
        st.write(cf.funciones_calculadora2(costo_combustible_año=gasto_combustible_anual, costo_neumatico_anual=gasto_neumaticos_anual,
                                           gastos_mantenimiento_preventivo_anual=gasto_mantenimiento_preventivo_anual, gastos_mantenimiento_correctivo_anual=gasto_mantenimiento_correctivo_anual,
                                           gasto_anual_mano_obra=gastos_anuales_mano_obra, gastos_legalizacion_anual=gastos_legalizacion_año, depreciacion_anual=depreciacion_anual,
                                           gastos_administrativos_anuales=gastos_administrativos_anuales, costo_inversion=costo_inversion).costo_fijo_total())

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
        st.write(cf.funciones_calculadora(kilometrosxdia=kilometros_dia, gdcombustible=gasto_diario, costo_neumatico=0, costo_preventivo=0, costo_correctivo=0).rendimiento_combustible())
        



