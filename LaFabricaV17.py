CP = 0
CPCadena = "  "
CC=0
CCCadena = " "
PrC = 0.0
PrT = 0
PrNum = False
PrCadena = ' '
contadorpiezas = 0
compporpieza = 0
comptotales=0
total = 0
cnumerico = True
unidades = 0
unumerico = False
unidadescadena = ' '
verificacion = False
print("Ingrese que pieza quiere procesar (entre 01 y 99) o 0 para terminar.")
CPCadena = input()
while CPCadena != "0": 
    if len(CPCadena) == 2: 
        cnumerico = CPCadena.isnumeric() 
        if cnumerico == True: 
            CP = int(CPCadena)
            if CP > 0:
                contadorpiezas = contadorpiezas + 1 
                print(f"Va a procesar la pieza {CPCadena}")
                print("Que componente quiere incluir en la pieza?(entre 01 y 99) o ingrese '0' para terminar de procesar la pieza")
                CCCadena= input()
                while CCCadena == "0" and compporpieza == 0:
                    print("La pieza debe incluir al menos un compónente")
                    CCCadena = input()
                while CCCadena != "0": 
                    cnumerico = CCCadena.isnumeric()
                    if cnumerico == True:                  
                        if CCCadena[-2:] == CPCadena: 
                            if len(CCCadena) == 4:
                                if int(CCCadena[:2]) > 0:
                                    print(f"Esta agregando el componente {CCCadena}")
                                    print("Cuantas unidades del componente desea agregar a la pieza?")
                                    unidadescadena=input()
                                    unumerico = unidadescadena.isnumeric()
                                    while unumerico == False:
                                        print("las unidades deben ser un numero")
                                        unidadescadena= input()
                                        unumerico = unidadescadena.isnumeric()
                                    unidades=int(unidadescadena)
                                    if unidades > 0: 
                                        print("Cual es el valor del componente?(entre 10.00 y 999.999)")
                                        compporpieza = compporpieza + unidades
                                        PrCadena = input()
                                        PrNum = PrCadena.replace('.', '1').isnumeric()
                                        while verificacion == False:
                                            while PrNum == False:
                                                print("El precio debe ser un nueroi entre 10.00 y 999.99")
                                                PrCadena = input()
                                                PrNum=PrCadena.replace('.', '1').isnumeric()
                                            PrC = float(PrCadena)
                                            if PrC >= 1000 or PrC <10: 
                                                PrNum =False
                                            
                                            else:
                                                verificacion= True
                                            
                                        PrT = PrT + (PrC * unidades)
                                        PrC = 0
                                        if compporpieza > 0:
                                            print("¿Qué otro componente quiere agregar(0 para terminar)")
                                            CCCadena = input()
                                        else:
                                            print("La pieza debe tener al menos un componente")
                                            print("Ingrese un numero de componente")
                                            CCCadena = input()
                                    else:
                                        print("Ingreso invalido, debe ser por lo menos 1 unidad")
                                        unidadescadena=input()
                                        unumerico = unidadescadena.isnumeric()
                                    verificacion = False
                                else:
                                    print("Ingreso invalido(el codigo de componente debe ser entre 01 y 99)")
                                    CCCadena= input()
                            else:
                                print("Ingreso invalido, el codigo de componente debe ser de 4 digitos")
                                CCCadena = input()
                        else:
                            print("Ingreso invalido(el codigo de componente no correspone a al codigo de pieza)")
                            CCCadena = input()   
                    else:
                        print("Codigo de componente invalido, debe ser numerico")
                        CCCadena = input()
                print(f"La pieza {CPCadena} contiene {compporpieza} componentes y el costo total es {PrT}")
                print("Qué otra pieza quiere procesar? ('0' para terminar)")
                total = total + PrT
                comptotales = comptotales + compporpieza
                compporpieza=0
                PrT = 0
                verificacion = False
                CPCadena = input()
            else:
                print("Ingreso invalido, el código de pieza debe ser entre 01 y 99")
                CPCadena = input()        
        else:
            print("Código de pieza invalido, tiene que ser un numerico")
            CPCadena= input()       
    else:
        print("Ingreso invalido(debe ser entre 01 y 99) o 0 para terminar")
        CPCadena = input()
print(f"usted proceso {contadorpiezas} piezas que contienen {comptotales} componentes y el valor total es {total}")





