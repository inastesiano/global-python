import os, time

# -------------------------------------------- MENU PRINCIPAL --------------------------------------------

os.system("cls")
ADN = input("Ingrese las filas del ADN separadas por espacios: ")

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
        for base in range(1, len(ADN)-2):
            if ADN[base] == ADN[base-1] == ADN[base+1] == ADN [base+2]:
                infectado = 1
            if ADN[base][base] == ADN[base-1][base] == ADN[base+1][base] == ADN [base+2][base]:
                infectado = 2

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








  