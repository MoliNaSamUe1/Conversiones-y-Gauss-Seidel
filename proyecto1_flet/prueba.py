import numbers
import numpy as np

def entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

def es_numero(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
    
def rellenar(num,matriz):
    matriz = np.zeros((num,num))
    for i in range(num):
        for j in range(num):
            matriz[i][j]= 2


matriz = np.array(0)
rellenar(3,matriz)
print(matriz)
#num = "232.3"
#print(es_numero(num))