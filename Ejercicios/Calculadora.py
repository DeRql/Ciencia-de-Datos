import time
def suma():
    c = a+b
    print("\n\n Resultado : \n")
    print(c)
def resta():
    c= a-b
    print("\n\n Resultado : \n")
    print(c)
def multiplicacion():
    c= a*b
    print("\n\n Resultado : \n")
    print(c)
def division():
    if b == 0:
        print("\n\n El numero debe ser diferente a cero\n ")
        time.sleep(3)
        ingresar()
        c= a/b
    else:
        c= a/b 
    print("\n\n Resultado : \n")
    print(c)
def programa():
    while True:
        print("\n\n ***      PROGRAMA         *** \n\n")
        print("Ingresar que hacer \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- Division \n 5.- Fin")
        x = int(input("")) 
        
        if x==1:
            ingresar()
            suma()
        elif x==2:
            ingresar()
            resta()
        elif x==3:
            ingresar()
            multiplicacion()
        elif x==4:
            ingresar()
            division()
        elif x==5:
            print(" FIN DE PROGRAMA ")
            break
        else:
            print("\n\nNO EXISTE ESA OPCION !! ")
            time.sleep(3)
            programa()
def ingresar():
    global a
    global b
    a = complex(input("Valor 1 : ")) 
    b = complex(input("Valor 2 : "))     
try:     
    programa()
except:
    print(" ERROR, INTENTA DE NUEVO  \n\n\n")
    time.sleep(3)
    programa()

