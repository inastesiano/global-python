import os, clases

def inicializar_adn():
    """
    Solicita al usuario que ingrese una matriz de ADN válida.
    """
    ADN = []
    print("Ingrese la matriz de ADN fila por fila. Cada fila debe tener exactamente 6 caracteres (A, T, C, G).")
    
    for i in range(6):
        while True:
            fila = input(f"Fila {i + 1}: ").upper()
            if len(fila) == 6 and all(char in "ATCG" for char in fila):
                ADN.append(fila)
                break
            else:
                print("Entrada inválida. Intente de nuevo.")
    
    return ADN


def menu_principal():

    ADN = ['TGATCA', 'GTTTCA', 'CATCAT', 'GAGTTA', 'ATTGCG', 'CTGTTC']
    
    detector = clases.Detector(ADN)

    while True:
        print("1. Detectar mutaciones")
        print("2. Mutar ADN")
        print("3. Sanar ADN")
        print("4. Salir")
        
        opcion = input("Elija una opción: ")
        if opcion == "1":
            os.system("cls")
            # Detectar mutaciones
            if not ADN:
                print("Primero debe inicializar la matriz de ADN.")
                ADN = inicializar_adn()
            
            print(f"Matriz actual: {ADN}")
            # Aquí llamarías a la clase Detector y sus métodos
            detector.detectar_mutantes(ADN)

            rta = input(print("Desea realizar otra operación? (y/n): "))
            if rta.lower() == "y":
                menu_principal()
            else:
                break
            
        elif opcion == "2":
            # Mutar ADN
            if not ADN:
                print("Primero debe inicializar la matriz de ADN.")
                ADN = inicializar_adn()
            
            print("Función de mutar ADN aún no implementada.")
            
        elif opcion == "3":
            # Sanar ADN
            if not ADN:
                print("Primero debe inicializar la matriz de ADN.")
                ADN = inicializar_adn()
            
        else:
            print("Opción no válida. Intente de nuevo.")
