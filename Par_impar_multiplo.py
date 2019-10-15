def Par_impar_multiplo():
    numero=input("Dime un numero: ")
    if numero%2==0:
        print "Este numero es par"
        if numero%3==0:
            print "y tambien es multiplo de 3"
        else:
            print "Pero no es multiplo de 3"
    else:
        print "Este numero es impar"
        if numero%3==0:
            print "y tambien es multiplo de 3"
        else:
            print "Pero no es multiplo de tres"

Par_impar_multiplo()
        
       
