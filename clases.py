import os
import random
class Detector:
    def __init__(self, ADN):
        self.ADN = ADN

    def detectar_mutantes(self, ADN):
        infectado = 0
        
        #HORIZONTAL
        for palabra in range(len(ADN)):
            for base in range(1, len(ADN)-2):
                if ADN[palabra][base] == ADN[palabra][base-1] == ADN[palabra][base+1] == ADN [palabra][base+2]:
                    print("El ADN ingresado está MUTADO HORIZONTALMENTE")
                    return True 

        #VERTICAL
        for palabra in range(1, len(ADN)-2):
            for letra in range(len(ADN)):
                if ADN[palabra-1][letra] == ADN[palabra][letra] == ADN[palabra+1][letra] == ADN[palabra+2][letra]:
                    print("El ADN ingresado está MUTADO VERTICALMENTE")
                    return True
                
        #DIAGONAL
        for palabra in range(len(ADN)-3):
            for letra in range(len(ADN[palabra])-3):
                if ADN[palabra][letra] == ADN[palabra+1][letra+1] == ADN[palabra+2][letra+2] == ADN[palabra+3][letra+3]:
                    print("El ADN ingresado está MUTADO DIAGONALMENTE")
                    return True
                
        print("El ADN ingresado está SANO")
        return False

        return bool(infectado)

class Mutador:
    def __init__(self,base_nitrogenada,tipo_mutacion, intensidad):
        self.base_nitrogenada=base_nitrogenada
        self.tipo_mutacion=tipo_mutacion
        self.intensidad=intensidad
        
    def crear_mutante(self):
        pass

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, tipo_mutacion, intensidad):
        
        super().__init__(base_nitrogenada, tipo_mutacion, intensidad)
        
    def crear_mutante(self, matriz_ADN, posicion_inicial, orientacion_de_la_mutacion):
        try:
            fila, columna = posicion_inicial
            if fila < 0 or fila >= len(matriz_ADN) or columna < 0 or columna >= len(matriz_ADN[0]):
                raise ValueError("La posición inicial está fuera de los límites de la matriz.")
            
            if orientacion_de_la_mutacion not in ("H", "V"):
                raise ValueError("La orientación debe ser 'H' (horizontal) o 'V' (vertical).")

            if orientacion_de_la_mutacion == "H":
                if columna + 3 >= len(matriz_ADN[fila]):
                    raise ValueError("La mutación horizontal excede los límites de la fila.")
                matriz_ADN[fila] = (
                    matriz_ADN[fila][:columna] +
                    self.base_nitrogenada * 4 +
                    matriz_ADN[fila][columna + 4:]
                )

            elif orientacion_de_la_mutacion == "V":
                if fila + 3 >= len(matriz_ADN):
                    raise ValueError("La mutación vertical excede los límites de la columna.")
                for i in range(4):
                    matriz_ADN[fila + i] = (
                        matriz_ADN[fila + i][:columna] +
                        self.base_nitrogenada +
                        matriz_ADN[fila + i][columna + 1:]
                    )

            return matriz_ADN

        except ValueError as e:
            print(f"Error: {e}")
            return matriz_ADN
        except Exception as e:
            print(f"Error inesperado: {e}")
            return matriz_ADN


class Virus(Mutador):
    def __init__(self, base_nitrogenada, tipo_virus, nivel_contagio):
        super().__init__(base_nitrogenada, tipo_virus, nivel_contagio)
        self.tipo_virus = tipo_virus
        self.nivel_contagio = nivel_contagio

    def crear_mutante(self, matriz_ADN, posicion_inicial):
        try:
            fila, columna = posicion_inicial
            if fila < 0 or fila >= len(matriz_ADN) or columna < 0 or columna >= len(matriz_ADN[0]):
                raise ValueError("La posición inicial está fuera de los límites de la matriz.")

            if fila + 3 >= len(matriz_ADN) or columna + 3 >= len(matriz_ADN[0]):
                raise ValueError("La mutación diagonal excede los límites de la matriz.")

            for i in range(4):
                matriz_ADN[fila + i] = (
                    matriz_ADN[fila + i][:columna + i] +
                    self.base_nitrogenada +
                    matriz_ADN[fila + i][columna + i + 1:]
                )

            return matriz_ADN

        except ValueError as e:
            print(f"Error: {e}")
            return matriz_ADN
        except Exception as e:
            print(f"Error inesperado: {e}")
            return matriz_ADN

class Sanador:
    def __init__(self, nombre, nivel_eficacia):
     
        self.nombre = nombre
        self.nivel_eficacia = nivel_eficacia

    def sanar_mutantes(self, matriz_ADN):
        detector = Detector(matriz_ADN)

        if detector.detectar_mutantes(matriz_ADN):
            print(f"{self.nombre} detectó una mutación y procederá a sanar el ADN...")
            
            # Crear un nuevo ADN sin mutaciones
            nuevo_ADN = self.generar_nuevo_ADN(len(matriz_ADN), len(matriz_ADN[0]))
            
            return nuevo_ADN
        else:
            print("El ADN está sano, no es necesario sanarlo.")
            return matriz_ADN

    def generar_nuevo_ADN(self, filas, columnas):
      
        bases = ['A', 'T', 'C', 'G']
        nuevo_ADN = []

        for i in range(filas):
            fila = ''.join(random.choice(bases) for _ in range(columnas))
            nuevo_ADN.append(fila)

        return nuevo_ADN


