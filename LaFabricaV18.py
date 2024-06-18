CP = 0
CPCadena = " "
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
while CPCadena != "0": #una vez que sea 0 se termina el proceso
    if len(CPCadena) == 2: #verifica que el codigo ingresado sea de la longitud correcta
        cnumerico = CPCadena.isnumeric() 
        if cnumerico == True: # verifica que el codigo ingresado sean solo numeros
            CP = int(CPCadena)
            if CP > 0: # verifica que el codigo ingresado no sea 00
                contadorpiezas = contadorpiezas + 1 
                print(f"Va a procesar la pieza {CPCadena}.")
                print("Qué componente quiere incluir en la pieza?(entre 01 y 99) o ingrese '0' para terminar de procesar la pieza.")
                CCCadena= input()
                while CCCadena == "0" and compporpieza == 0: # verifica que la pieza procesada contenga al menos un componente
                    print("La pieza debe incluir al menos un componente.")
                    CCCadena = input()
                while CCCadena != "0": #cuando el codigo de componente sea 0 se termina de procesar la pieza
                    cnumerico = CCCadena.isnumeric()
                    if cnumerico == True:#verifica que el codigo ingresado sean numeros
                        if CCCadena[-2:] == CPCadena: #verifica que el codigo de componente conucuerde con la pieza que se esta procesando
                            if len(CCCadena) == 4: #verifica la longitud correcta del codigo de componente 
                                if int(CCCadena[:2]) > 0: #verifica que el codigo no empiece por 00
                                    print(f"Está agregando el componente {CCCadena}.")
                                    print("Cuantas unidades del componente desea agregar a la pieza?")
                                    unidadescadena=input()
                                    unumerico = unidadescadena.isnumeric()
                                    while unumerico == False:#verifica que se ingresen un numero de unidades
                                        print("Las unidades deben ser un número.")
                                        unidadescadena= input()
                                        unumerico = unidadescadena.isnumeric()
                                    unidades=int(unidadescadena)
                                    if unidades > 0: #verifica que el numero de unidades sea disntinto de 0
                                        print("Cuál es el valor del componente?(entre 10.00 y 999.999)")
                                        compporpieza = compporpieza + unidades
                                        PrCadena = input()
                                        PrNum = PrCadena.replace('.', '1').isnumeric()#reemplazo los puntos por un 1 para poder verificar que sea un ingreso numerico que pueda convertir a float
                                        while verificacion == False:#verifica que el precio este en numeros y dentro del rango valido
                                            while PrNum == False:#mientras el valor no haya sido numerico pide que se ingrese uno distinto
                                                print("El precio debe ser un numero entre 10.00 y 999.99.")
                                                PrCadena = input()
                                                PrNum=PrCadena.replace('.', '1').isnumeric()
                                            PrC = float(PrCadena)#transforma el valor a su variable numerica
                                            if PrC >= 1000 or PrC <10:#si el valor no esta dentro del rango valido vuelve a pedir el ingreso de la cadena de precio
                                                PrNum =False                                            
                                            else:#si el valor es numerico y dentro del rango la verificacion es verdadera
                                                verificacion= True                                            
                                        PrT = PrT + (PrC * unidades)
                                        PrC = 0
                                        if compporpieza > 0: #verifica que la pieza tenga al menos un componente
                                            print("¿Qué otro componente quiere agregar?(0 para terminar)")
                                            CCCadena = input()
                                        else:
                                            print("La pieza debe tener al menos un componente.")
                                            print("Ingrese un numero de componente.")
                                            CCCadena = input()
                                    else:
                                        print("Ingreso inválido, debe ser por lo menos 1 unidad.")
                                        unidadescadena=input()
                                        unumerico = unidadescadena.isnumeric()
                                    verificacion = False
                                else:
                                    print("Ingreso inválido.(el codigo de componente debe ser entre 01 y 99)")
                                    CCCadena= input()
                            else:
                                print("Ingreso inválido, el codigo de componente debe ser de 4 digitos.")
                                CCCadena = input()
                        else:
                            print("Ingreso inválido. (el codigo de componente no correspone a al codigo de pieza)")
                            CCCadena = input()   
                    else:
                        print("Código de componente invalido, debe ser numerico.")
                        CCCadena = input()
                print(f"La pieza {CPCadena} contiene {compporpieza} componentes y el costo total es ${PrT}.") #se imprimen los datos de la pieza procesada y se reinician variables
                print("Qué otra pieza quiere procesar? ('0' para terminar)")
                total = total + PrT
                comptotales = comptotales + compporpieza
                compporpieza=0
                PrT = 0
                verificacion = False
                CPCadena = input()
            else:
                print("Ingreso inválido, el código de pieza debe ser entre 01 y 99")
                CPCadena = input()        
        else:
            print("Código de pieza inválido, tiene que ser un numérico")
            CPCadena= input()       
    else:
        print("Ingreso inválido(debe ser entre 01 y 99) o 0 para terminar.")
        CPCadena = input()
print(f"Usted procesó {contadorpiezas} piezas que contienen {comptotales} componentes y el valor total es ${total}")#si imprime los datos totales del procesamiento de piezas





