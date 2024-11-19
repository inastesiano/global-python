import os, time

# -------------------------------------------- MENU PRINCIPAL --------------------------------------------

os.system("cls")
ADN = ["CTGTTC", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "TTTTCA"]
#for i in range(6):
#    cadena = ""
#    while len(cadena)!=6:
#        cadena = input(f"Ingrese la cadena n° {i+1} del ADN: ")
#    ADN.append(cadena)

salir = False
while not salir:
    os.system("cls")

    print("ADN ingreasado: ", ADN)

    print("------------------------- MENU PRINCIPAL -------------------------")
    print("1. Detectar mutaciones")
    print("2. Mutar ADN ")
    print("3. Sanar ADN")
    print("4. Salir del programa")
    print("------------------------------------------------------------------")

    opcion = int(input("OPCION: "))
    
    if opcion == 1 :
        
        os.system("cls")
        infectado = 0
        for palabra in range(len(ADN)):
            for base in range(1, len(ADN)-2):
                if ADN[palabra][base] == ADN[palabra-1][base] == ADN[palabra-2][base] == ADN [palabra-3][base]:
                    infectado = 2
                if ADN[palabra][base] == ADN[palabra][base-1] == ADN[palabra][base+1] == ADN [palabra][base+2]:
                    infectado = 1
                

        if infectado == 1:
            print("El ADN ingresado está MUTADO HORIZONTALMENTE")
        if infectado == 2:
            print("El ADN ingresado está MUTADO VERTICALMENTE")
        else:
            print("El ADN ingresado está SANO")

        rta = input("Desea realizar otra operación? (y/n): ").lower()

        if rta == "y" :
            pass
        else:
            break

    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    else:
        salir = True
        os.system("cls")

print("--------------------------------------")
print("Saliendo del programa...")








  