import os
import numpy as np
import examen as ex
edificio=np.empty([10,4],type(int))
otra=np.empty([10,4],type(int))
ruts=[]
ex.llenar(edificio,otra)
op=0
ed=""
suma=0

while(op!=5):
    os.system("cls")
    print("     Inmobiliaria Casa Feliz     ")
    print("     **********************     ")
    print(" 1.  Comprar departamento ")
    print(" 2.  Mostrar departamentos disponibles ")
    print(" 3.  Ver listado de compradores ")
    print(" 4.  Mostrar ganancias totales ")
    print(" 5.  Salir ")
    op=ex.validaOp()
    if(op==1):
        dd=ex.edificio()
        ed=ex.validaedificio()
        cc=ex.disponible(edificio,ed)
        if(cc):
            print("edificio disponible!!")
            os.system("pause")
            pagar=ex.comprardepartamento(edificio,dd,otra,ruts)
            print("\t Usted deberá cancelar un total de: $", pagar,"UTM" )
            os.system("pause")
    if(op==2):
        ex.mostrarDisponibles(edificio)
        os.system("pause")
    if(op==3):
        ex.Listado(ruts)
        os.system("pause")
    if(op==4):
        suma=0
        suma=ex.totalVenta(otra)
        if(suma==0):
            print("\t No se han vendido pasajes aún")
        else:
            print("\t El total vendido hasta ahora es de : $", suma)
        os.system("pause")
    if(op==5):
        print("******Muchas gracias por comprar departamentos en nuestra inmobiliaria, vuelva pronto******")
        break
