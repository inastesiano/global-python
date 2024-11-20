import os

class Detector:
    def __init__(self, ADN):
        self.ADN = ADN

    def detectar_mutantes(self, ADN):
        infectado = 0
        
        #HORIZONTAL
        for palabra in range(len(ADN)):
            for base in range(1, len(ADN)-2):
                if ADN[palabra][base] == ADN[palabra][base-1] == ADN[palabra][base+1] == ADN [palabra][base+2]:
                    infectado = 1
                    break

        #VERTICAL
        for palabra in range(1, len(ADN)-2):
            for letra in range(len(ADN)):
                if ADN[palabra-1][letra] == ADN[palabra][letra] == ADN[palabra+1][letra] == ADN[palabra+2][letra]:
                    infectado = 2
                    break
                
        if infectado == 1:
            print("El ADN ingresado está MUTADO HORIZONTALMENTE")
        if infectado == 2:
            print("El ADN ingresado está MUTADO VERTICALMENTE")
        else:
            print("El ADN ingresado está SANO")

        return bool(infectado)

class Mutador:
    def __init__(self):
        pass

    def crear_mutante(self):
        pass

class Radiacion(Mutador):
    def __init__(self):
        pass

    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        #debe retornar la matriz con las modificaciones
        pass

class Virus(Mutador):
    def __init__(self):
        pass

    def crear_mutante(self, base_nitrogenada, posicion_inicial):
        #debe retornar la matriz con las modificaciones
        pass

class Sanador:
    def __init__(self):
        pass

    def sanar_mutantes(self, matriz_ADN): 
        pass

