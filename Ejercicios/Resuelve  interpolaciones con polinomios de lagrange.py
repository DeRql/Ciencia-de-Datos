from scipy.interpolate import lagrange
import matplotlib.pyplot as plt 
from scipy import *
import numpy as np

val1 = np.arange(12,18)
val2 = np.arange(-3,3,)
val_1 = []
val_2 = []
print("  -- PROGRAMA QUE RESUELVE UNA INTERPOLACION CON POLINOMIOS DE LAGRANGE --")
def programa():
    x = int(input("Ingresar la cantidad de datos que ingresara : "))
    for i in range(0,x):
        val_1.append(int(input("Ingresa el valor #"+str(i+1)+" de la función X --> ")))
    for i in range(0,x):
        val_2.append(int(input("Ingresa el valor #"+str(i+1)+" de la función Y --> ")))

    plt.plot(val_1,val_2,".")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    funcion_l = lagrange(val_1,val_2)
    print("El polinomio de lagrange es :\n " + str(funcion_l))
    evaluar = int(input("Si queremos evaluar un valor, ingresa aqui : "))
    print("\n\n --> Reemplazando "+str(evaluar)+" en la funcion nos da " + str(funcion_l(evaluar)))
programa()