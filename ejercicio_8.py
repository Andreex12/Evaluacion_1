def ejercicio_7():
    dinero=input("Precio=")
    IVA=raw_input("Tipo de IVA(general, reducido o superreducido):")
    general=(dinero*16)/100
    reducido=(dinero*7)/100
    superreducido=(dinero*4)/100
    if IVA=="general":
        print "Coste=",general+dinero
    if IVA=="reducido":
        print "Coste=",reducido+dinero
    if IVA=="superreducido":
        print "Coste=",superreducido+dinero

ejercicio_7()
    
