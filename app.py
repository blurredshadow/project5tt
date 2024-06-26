import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Anuncios de Vehiculos")
st.write("Selecciona el gráfico deseado")
        
car_data = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

import streamlit as st

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

scatter_button = st.button('Construir diagrama de dispersion') # crear un botón
        
if scatter_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el precio')
            
          
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)