def ejercicio_7():
    print "Dime dos numeros:"
    a=input("a= ")
    b=input("b= ")
    print "Que queres hacer:suma(S), resta(R),multiplcacion(M) o division(D)?"
    operacion=raw_input("letra= ")

    if operacion=="S":
        print "Suma=",a+b
    if operacion=="R":
        print "Resta=",a-b
    if operacion=="M":
        print "Multiplicacion=",a*b
    if operacion=="D":
        if b==0:
            print "Error.No se puede dividir por 0"
        else:
            print "Division=",a/b

ejercicio_7()
    
    
    
