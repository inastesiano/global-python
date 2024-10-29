

ADN = input("Ingrese las filas del ADN separadas por espacios: ")

infectado = False

for base in range(1, len(ADN)-2):
    if ADN[base] == ADN[base-1] == ADN[base+1] == ADN [base+2]:
        infectado = True

if infectado:
    print("TENES DOWN")