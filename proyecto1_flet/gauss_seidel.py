import numpy as np

fila = 0
col = 0
pos = 0
matriz = None
vector = None
result = None

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
#Funcion que hace que se acerque o sea diagonalmente dominante
def diagonal_dominante(matriz,vector):
    for i in range(len(matriz)):
        for j in range(i,len(matriz)):    
            if (abs(matriz[i][i])<abs(matriz[j][i])):
                matriz[[i,j]]=matriz[[j,i]]
                vector[i] , vector[j] = vector[j] , vector[i]

#Funcion que comprueba que ningun coeficiente de la diagonal prinncipal sea 0           
def comprobar_diagonal(matriz):
    diago = matriz.diagonal()
    for i in range(len(matriz)):
        if(diago[i]==0):
            return False
    return True

#Funcion para comprobar los errores admisibles
def errores(anterior,actual,tolerancia):
    for i in range(len(anterior)):
        if (actual[i]!=0):
            error = abs(1-anterior[i]/actual[i])
            if(error > tolerancia):
                return False
        else:
            return False
    return True

#Funcion que realiza el metodo gauss seidel
def gauss(matriz, vector , result, tolerancia, iterar):
     
    if (comprobar_diagonal(matriz)):
        cont = 0
        #actualizo el vector 
        copia = result.copy()
        #Ciclo while hasta que se hagan las iteraciones predeterminadas
        while(cont != iterar):
            copia = result.copy()
            #result[:] = 0
            #Ciclo para recorrer la filas de la matriz
            for i in range(len(matriz)):
                #Aqui es donde se guardan los nuevos valores de las incognitas, con el proceso de slices
                result[i] = (vector[i] - np.dot(matriz[i, :i], result[:i]) - np.dot(matriz[i, i+1:], copia[i+1:])) / matriz[i, i]
            #si se cumple la condicion del metodo se para la funcion
            if errores(copia, result, tolerancia):
                return result            
            cont+=1        
        return result           
        
#Retorna una cadena con las ecuaciones
def ecuacion(matriz, vector):
    cadena = ""
    for i in range(len(matriz)):
        for j in range(len(matriz)+1):
            if(j==0):
                cadena += str(matriz[i][j])+"x"+str(j+1)+" "
            else:
                if(j!=len(matriz)):
                    if(matriz[i][j]>=0):
                        cadena += "+"+str(matriz[i][j])+"x"+str(j+1)+" "
                    else:
                        cadena += str(matriz[i][j])+"x"+str(j+1)+" "
                else:
                    cadena += "= "+str(vector[i])+"\n"
    return cadena

