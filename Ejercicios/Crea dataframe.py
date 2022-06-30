import pandas as pd
import numpy as np
def reporte_contable(ran):
    meses = []
    for i in range (0,ran):
        meses.append(input('Introducir los meses a registrar: '+str(i) +': ')) 
    Ventas = []
    for i in range (0,ran):
        Ventas.append(input('Introducir los valores a registrar: '+str(i) +': '))
    Gastos = []
    for i in range (0,ran):
        Gastos.append(input('Introducir los valores a registrar: '+str(i) +': '))
    marks_array = np.array(["Meses","Ventas","Gastos"])
    print("")
    data_df = pd.DataFrame(list(zip(meses,Ventas,Gastos)),columns=marks_array)
    print("El Dataframe es:")
    print(data_df)
reporte_contable(int(input("Ingrese la cantidad de datos : ")))