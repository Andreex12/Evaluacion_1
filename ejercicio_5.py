def calendario():
    print "Dime una fecha:"
    a=input("dia= ")
    b=input("mes= ")
    c=input("año= ")
    if b==1:
        b="Enero"
    if b==2:
        b="Febrero"
    if b==3:
        b="Marzo"
    if b==4:
        b="Abril"
    if b==5:
        b="Mayo"
    if b==6:
        b="Junio"
    if b==7:
        b="Julio"
    if b==8:
        b="Agosto"
    if b==9:
        b="Septiembre"
    if b==10:
        b="Octubre"
    if b==11:
        b="Noviembre"
    if b==12:
        b="Diciembre"
    print a,"de",b,"de",c
    
calendario()

