def cantidad():
    a=input("Numero:")
    b=raw_input("Palabra:")
    letras=0
    for i in b:
        letras=letras+1
    if letras==a:
        print "Tiene el mismo numero de letras que el numero que has dicho"
    else:
        print "No tiene el mismo numero de letras que el numero que has dicho"

cantidad()
        
