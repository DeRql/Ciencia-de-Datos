f = 1
def programaa():   
    try:
        def v_1():
            print("Ingresa aqui \n↓↓↓↓↓↓↓↓↓↓")
            val1= complex(input())
            return val1
        def v_2():
            print("Ingresa aqui \n↓↓↓↓↓↓↓↓↓↓")
            val2= complex(input())
            print("\nResultado")
            return val2
        def sumar(n1,n2):
            respuesta = n1 + n2
            return respuesta
        def restar(n1,n2):
            respuesta = n1 - n2
            return respuesta
        def multiplicar(n1,n2):
            respuesta = n1 * n2
            return respuesta
        def dividir(n1,n2):
            if n2 != 0:
                respuesta = n1 / n2
                return respuesta
            else:
                print("\n\nDebe ser diferente a 0 \n Intenta de nuevo.\n")
                dividir(v_1(),v_2())
        print("                -----------  MENU  ----------- \n\n\n1.- SUMAR\n2.- RESTAR\n3.- MULTIPLICAR\n4.- DIVIDIR\n0.- Terminar el programa\n\n--> Con ayuda del teclado numero ingresar la opción deseada : \n ")
        opc = int(input("-  "))
        if opc<6 and opc>=0:       
            if opc == 1:                
                print(sumar(v_1(),v_2()))
            elif opc == 2:
                print(restar(v_1(),v_2()))
            elif opc == 3:
                print(multiplicar(v_1(),v_2()))
            elif opc == 4:
                print(dividir(v_1(),v_2()))      
            elif opc == 0:
                global f
                f = 0
                print(" ---- >>>> FIN DEL PROGRAMA ")                         
        else:
            print("\n\n OPCIÓN INCORRECTA !")
    except:
        print(" ERROR, INTENTA DE NUEVO  \n\n\n")
while f != 0:
    programaa()