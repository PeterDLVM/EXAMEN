
import os
import numpy as np 
def llenar(aa,otra): 
    p=1
    for i in range(10):
        for j in range(4):
            aa[i,j]=p
            otra[i,j]=p
            p+=1 
def validaOp():
    pp=0
    while(True):
        try:
            pp=int(input("   Elija opción: "))
            if(pp>=1 and pp<=5):
                break
            else:
                print("Debe ingresar una opción entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero")
    return pp 
def mostrarDisponibles(aa):
    os.system("cls")
    for i in range(10):
        print("\n") 
        for j in range(4):
            if(j=="A1" or j=="D10"):
                print("\t",aa[i,j], end="  ")
            else:
                print("\t",aa[i,j], end="   ")
    print("\n\n")
def edificio():
    os.system("cls")
    des=""
    while(len(des)<=0):
        print("******Edificio******")
        print("A1","B1","C1","D1",sep="  ")
        print("A2","B2","C2","D2",sep="  ")
        print("A3","B3","C3","D3",sep="  ")
        print("A4","B4","C4","D4",sep="  ")
        print("A5","B5","C5","D5",sep="  ")
        print("A6","B6","C6","D6",sep="  ")
        print("A7","B7","C7","D7",sep="  ")
        print("A8","B8","C8","D8",sep="  ")
        print("A9","B9","C9","D9",sep="  ")
        print("A10","B10","C10","D10",sep="  ")
        des=input("   Elija un departamento con columna A,B,C,D y su respectivo numero. ejemplo (A10) ").lower()
        if(des=="A1" and des=="B1" and des=="C1" and des=="D1"):
            print("Debe ingresar una opcion correcta")
            des=""
        if(des=="A2" and des=="B2" and des=="C2" and des=="D2"):
            print("Debe ingresar una opcion correcta")
            des=""
        if(des=="A3" and des=="B3" and des=="C3" and des=="D3"):
            print("Debe ingresar una opcion correcta")
            des=""
        if(des=="A4" and des=="B4" and des=="C4" and des=="D4"):
            print("Debe ingresar una opcion correcta")
            des=""
        if(des=="A5" and des=="B5" and des=="C5" and des=="D5"):
            print("Debe ingresar una opcion correcta")
            des=""
        if(des=="A6" and des=="B6" and des=="C6" and des=="D6"):
            print("Debe ingresar una opcion correcta")
            des=""
        if(des=="A7" and des=="B7" and des=="C7" and des=="D7"):
            print("Debe ingresar una opcion correcta")
            des=""
        if(des=="A8" and des=="B8" and des=="C8" and des=="D8"):
            print("Debe ingresar una opcion correcta")
            des=""
        if(des=="A9" and des=="B9" and des=="C9" and des=="D9"):
            print("Debe ingresar una opcion correcta")
            des=""
        if(des=="A10" and des=="B10" and des=="C10" and des=="D10"):
            print("Debe ingresar una opcion correcta")
            des=""
    return des
def validaedificio():
    edificio=0
    while(True):
        try:
            edificio=input(" Ingrese letra y número de departamento entre (A1) hasta (D10) ")
            if(edificio=="A1" and edificio=="B1" and edificio=="C1" and edificio=="D1" and edificio=="A2" and edificio=="B2" 
            and edificio=="C2" and edificio=="D2" and edificio=="A3" and edificio=="B3" and edificio=="C3" and edificio=="D3" 
            and edificio=="A4" and edificio=="B4" and edificio=="C4" and edificio=="D4" and edificio=="A5" and edificio=="B5" 
            and edificio=="C5" and edificio=="D5" and edificio=="A6" and edificio=="B6" and edificio=="C6" and edificio=="D6"
            and edificio=="A7" and edificio=="B7" and edificio=="C7" and edificio=="D7" and edificio=="A8" and edificio=="B8" 
            and edificio=="C8" and edificio=="D8" and edificio=="A9" and edificio=="B9" and edificio=="C9" and edificio=="D9"
            and edificio=="A10" and edificio=="B10" and edificio=="C10" and edificio=="D10"):
                break
            else:
                print("Error debe ingresar un asiento entre A1 a D10")
        except ValueError:
            print("Error dato ingresado no es valido")
    return edificio 
def disponible(edificio):
    for i in range(10):
        for j in range(4):
            if(edificio[i,j]):
                return True
    return False
def comprardepartamento(aa,edificio,dd,otra,ruts):
    if(dd=="A1"):
        pago=3800
    if(dd=="A2"):
        pago=3800
    if(dd=="A3"):
        pago=3800
    if(dd=="A4"):
        pago=3800
    if(dd=="A5"):
        pago=3800
    if(dd=="A6"):
        pago=3800
    if(dd=="A7"):
        pago=3800
    if(dd=="A8"):
        pago=3800
    if(dd=="A9"):
        pago=3800
    if(dd=="A10"):
        pago=3800
    if(dd=="B1"):
        pago=3000
    if(dd=="B2"):
        pago=3000
    if(dd=="B3"):
        pago=3000
    if(dd=="B4"):
        pago=3000
    if(dd=="B5"):
        pago=3000
    if(dd=="B6"):
        pago=3000
    if(dd=="B7"):
        pago=3000
    if(dd=="B8"):
        pago=3000
    if(dd=="B9"):
        pago=3000
    if(dd=="B10"):
        pago=3000
    if(dd=="C1"):
        pago=2800
    if(dd=="C2"):
        pago=2800
    if(dd=="C3"):
        pago=2800
    if(dd=="C4"):
        pago=2800
    if(dd=="C5"):
        pago=2800
    if(dd=="C6"):
        pago=2800
    if(dd=="C7"):
        pago=2800
    if(dd=="C8"):
        pago=2800
    if(dd=="C9"):
        pago=2800
    if(dd=="C10"):
        pago=2800
    if(dd=="D1"):
        pago=3500
    if(dd=="D2"):
        pago=3500
    if(dd=="D3"):
        pago=3500
    if(dd=="D4"):
        pago=3500
    if(dd=="D5"):
        pago=3500
    if(dd=="D6"):
        pago=3500
    if(dd=="D7"):
        pago=3500
    if(dd=="D8"):
        pago=3500
    if(dd=="D9"):
        pago=3500
    if(dd=="D10"):
        pago=3500
    for i in range(10):
        for j in range(4):
            if(edificio==aa[i,j]):
                while(True):
                    while(True):
                        try:
                            rut=int(input("Rut debe tener 8 digitos minimo "))
                            if(rut<9999999):
                                print("Error, debe tener 8 dígitos mínimo")
                            else:
                                break
                        except ValueError:
                            print("Debe ser número entero")
                    if(len(rut)>0): 
                        sw=0
                        for y in range(len(rut)):
                            if(rut==rut[y]):
                                sw=1
                        if(sw==1):
                            print("El rut ya existe y no se puede agregar el pasajero")
                        else:
                            ruts.append(rut)
                            break
                    else:
                        ruts.append(rut)
                        break
                aa[i,j]="X"
                otra[i,j]=pago
def totalVenta(aa):
    suma=0
    for i in range(10):
        for j in range(4):
            if(aa[i,j]!=0 and aa[i,j]>34):
                suma+=aa[i,j]
