import streamlit as st
import numpy as np
st.title("Proyecto módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

st.image("Python_logo.png")
st.sidebar.image("DMC.png")

modulo =st.sidebar.selectbox("Elija un módulo",["Módulo Listas","Módulo Array","Módulo Funciones"])

if modulo == "Módulo Listas":  

  valor_inicial =st.number_input("Ingrese el valor inicial", value =0)
  valor_final =st.number_input("Ingrese el valor final", value=1 )
  lista_numerica= list(range(valor_inicial, valor_final))
  st.write(lista_numerica)

elif modulo == "Módulo Array":  
  st.write("Estas en el módulo de arreglos")
   
  limite_inferior =st.number_input("Ingrese el limite inferior", value =1200)
  limite_superior =st.number_input("Ingrese el limite superior", value=1250)
  cantidad_datos =st.number_input("Ingrese totalidad de datos a crear", value=31)
   
  datos_produccion = np.random.randint(limite_inferior,limite_superior, cantidad_datos)
  st.write(datos_produccion) 
  st.write("La producción total es:" ,  np.sum(datos_produccion))
  st.write("La producción promedio es:" , np.mean(datos_produccion)) 
  
else:
  st.write("Estas en el módulo de funciones")
  principal =st.number_input("Ingrese el monto del préstamo", value =0)
  tasa_anual =st.number_input("Ingrese la Tasa anual en decimalr", value =0.10)
  anios=st.number_input("Ingrese el Número de años del préstamo", value =1)
  pagos_por_anio=st.number_input("Ingrese la Cantidad de pagos por año", value =12)
  
  cuota = lf.cuota_prestamo(principal,tasa_anual,anios, pagos_por_anio )
  st.write("La cuota mensual de pago será", cuota)
