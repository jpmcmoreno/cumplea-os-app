import streamlit as st
import math

def calcular_probabiliadad(cant_personas):
    numerador = math.perm(365, cant_personas)
    denominador = math.pow(365, cant_personas)
    return 1 - numerador / denominador


st.title('Probabilidad de coincidencia de cumpleaños')
cant_personas = st.number_input('Cantidad de personas', min_value=2, max_value=365, value=2)

probabilidad = calcular_probabiliadad(cant_personas)

st.write(f'La probabilidad de que al menos dos personas de un grupo de {cant_personas} personas cumplan años el mismo día es de {probabilidad:.1%}')