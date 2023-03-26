import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sklearn
from fs import FeatureSelection

with open('mejor_modelo_tp4.pkl', 'rb') as f:
    modelo = pickle.load(f)



def predecir(features):
    
    predicciones = modelo.predict(features)
    return predicciones


# Crea la aplicación Streamlit
def app():
    
    st.title('Es o no es una caída?')

    st.write('Ingresá usando los sliders los valores del giroscopio y del acelerómetro del smartphone:')

    col1, col2, col3 = st.columns(3)

    with col1:
            feature1 = st.text_input('Índice', value = 61, help = "En este campo podés poner cualquier cosa")

    with col2:
            feature2 = st.slider('Acelerómetro (4to segundo)', min_value=9.0, max_value=33.0, value=26.0, step=0.1, format="%f", help="Aceleración máxima del 4to segundo")

    with col3:
            feature3 = st.slider('Giroscopio (4to segundo)', min_value=0.0, max_value=18.0, value=5.0, step=0.1, format="%f", help="dato máximo del giroscopio en el 4to segundo")

    col4, col5, col6 = st.columns(3)

    with col4:
            feature4 = st.slider('Acelerómetro (kurtosis)', min_value=-2.0, max_value=232.0, value=17.0, step=0.1, format="%f", help="kurtosis de la aceleración durante los 6 segundos")

    with col5:
            feature5 = st.slider('Giroscopio (kurtosis)', min_value=-2.0, max_value=35.0, value=9.0, step=0.1, format="%f", help="kurtosis del giroscopio durante los 6 segundos")

    with col6:
            feature6 = st.text_input('Tipo de movimiento', value = 'FOL', help = "En este campo podés poner cualquier cosa")
    
    col7, col8, col9 = st.columns(3)

    with col7:
            feature7 = st.slider('Acelerómetro (lineal, 4to segundo)', min_value=0.0, max_value=26.0, value=11.0, step=0.1, format="%f", help="aceleración lineal máxima (excluyendo la gravedad) del 4to segundo")

    with col8:
            feature8 = st.slider('Acelerómetro (simetría)', min_value=-15.0, max_value=7.0, value=3.0, step=0.1, format="%f", help="simetría de la aceleración durante los 6 segundos")

    with col9:
            feature9 = st.slider('Giroscopio (simetría)', min_value=-1.0, max_value=6.0, value=2.0, step=0.1, format="%f", help="simetría del giroscopio durante los 6 segundos")

    col10, col11, col12 = st.columns(3)

    with col10:
            feature10 = st.slider('Giroscopio (6to segundo)', min_value=-5.0, max_value=17.0, value=4.0, step=0.1, format="%f", help="dato máximo del giroscopio en el 6to segundo")

    with col11:
            feature11 = st.slider('Acelerómetro (6to segundo)', min_value=-6.0, max_value=24.0, value=10.0, step=0.1, format="%f", help="aceleración lineal máxima en el 6to segundo")
    
    with col12:
            
            if st.button('¿Es una caída?'):
        
                features = pd.DataFrame({
                'Unnamed: 0': [feature1],
                'acc_max': [feature2],
                'gyro_max': [feature3],
                'acc_kurtosis': [feature4],
                'gyro_kurtosis': [feature5],
                'label': [feature6],
                'lin_max': [feature7],
                'acc_skewness': [feature8],
                'gyro_skewness': [feature9],
                'post_gyro_max': [feature10],
                'post_lin_max': [feature11],          
                })
        
        # if predecir(features) == 0:
        #     predicciones = 'NO '
        # else:
        #     predicciones = ''
                if predecir(features) == [0]:
                       respuesta = ' NO  '
                else:
                       respuesta = ' SI  '
                st.write(f'Estos datos {respuesta}son compatibles con una caída')
 
    if st.button('Pasos del modelo:'):
               
        st.write(modelo.named_steps)
        
    st.markdown("[Link al dataset original](https://www.kaggle.com/datasets/saadmansakib/smartphone-human-fall-dataset)")

# Ejecuta la aplicación Streamlit
if __name__ == '__main__':
    app()
