def ejercicio_6():
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
        print "Division=",a/b
    
   
ejercicio_6()
        
