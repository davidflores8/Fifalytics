class Parser:

    def atributos(cadena):
        #aqui estan todas las lineas
        cadena=cadena.split("\n")
        #split por cada linea, ya se sabe que son 3 lineas
        #linea 1 (ritmo y regate)
        ritmo=cadena[0].replace("PAC)", " ")
        ritmo=ritmo.replace("PAC|", " ")
        ritmo=ritmo.replace(")", "")
        ritmo=ritmo.replace(".", "")
        ritmo=ritmo.replace("PAC|", " ")
        ritmo=ritmo.replace("PAC=", " ")
        ritmo=ritmo.replace("PAC", " ")
        ritmo=ritmo.replace("0R1", " ")
        ritmo=ritmo.replace("ORI", " ")
        ritmo=ritmo.replace("OR1", " ")
        ritmo=ritmo.replace("DRI", " ")
        ritmo=ritmo.replace("DRL", " ")
        #correccion de caracteres comunes
        ritmo=ritmo.replace("g", "8")
        ritmo=ritmo.replace("A", "4")
        ritmo=ritmo.replace("B", "8")
        ritmo=ritmo.replace("I", "1")
        ritmo=ritmo.replace("T", "7")
        ritmo=ritmo.replace("a", "8")
        ritmo=ritmo.replace("Q", "8")
        ritmo=ritmo.replace("O", "0")
        atribut=ritmo.split(" ")
        #linea 2
        print("segunda linea")
        print (cadena[1])
        linea2=cadena[1].replace("SHO|","")
        linea2=linea2.replace("SHO)","")
        linea2=linea2.replace("SHO","")
        list(atribut).append(linea2.split(" "))
        return atribut