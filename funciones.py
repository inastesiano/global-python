import os
import clases  

def inicializar_adn():
    
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
    
    ADN = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"]
    
    detector = clases.Detector(ADN)

    while True:
        print("\n1. Detectar mutaciones")
        print("2. Mutar ADN")
        print("3. Sanar ADN")
        print("4. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            os.system("cls")  
            
            if not ADN:
                print("Primero debe inicializar la matriz de ADN.")
                ADN = inicializar_adn()
            
            print(f"Matriz actual: {ADN}")
          
            detector.detectar_mutantes(ADN)

            rta = input("¿Desea realizar otra operación? (y/n): ")
            if rta.lower() != "y":
                break

        elif opcion == "2":
            if not ADN:
                print("Primero debe inicializar la matriz de ADN.")
                ADN = inicializar_adn()
            
        
            print("Elija el tipo de mutación:")
            print("1. Radiación")
            print("2. Virus")
            tipo_mutacion = input("Elija una opción (1/2): ")
            
            base_nitrogenada = input("Ingrese la base nitrogenada (A, T, C, G): ").upper()
            intensidad = input("Ingrese la intensidad de la mutación: ")

            if tipo_mutacion == "1":
                mutador = clases.Radiacion(base_nitrogenada, "Radiación", intensidad)
            elif tipo_mutacion == "2":
                tipo_virus = input("Ingrese el tipo de virus: ")
                nivel_contagio = input("Ingrese el nivel de contagio: ")
                mutador = clases.Virus(base_nitrogenada, tipo_virus, nivel_contagio)
            else:
                print("Opción inválida. Regresando al menú principal.")
                continue

            fila = int(input("Ingrese la fila para la mutación (0-5): "))
            columna = int(input("Ingrese la columna para la mutación (0-5): "))
            orientacion = input("Ingrese la orientación de la mutación (H para horizontal, V para vertical): ").upper()

            ADN = mutador.crear_mutante(ADN, (fila, columna))
            print(f"ADN después de la mutación: {ADN}")
            
            rta = input("¿Desea realizar otra operación? (y/n): ")
            if rta.lower() != "y":
                break
            
        elif opcion == "3":
            if not ADN:
                print("Primero debe inicializar la matriz de ADN.")
                ADN = inicializar_adn()

            nombre_sanador = input("Ingrese el nombre del sanador: ")
            nivel_eficacia = input("Ingrese el nivel de eficacia del sanador: ")

            sanador = clases.Sanador(nombre_sanador, nivel_eficacia)
            ADN = sanador.sanar_mutantes(ADN)
            print(f"ADN después de la sanación: {ADN}")
            
            rta = input("¿Desea realizar otra operación? (y/n): ")
            if rta.lower() != "y":
                break

        elif opcion == "4":
            print("Saliendo...")
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()  
