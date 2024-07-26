import pandas as pd
from ejercicios import Grafica
# Leer el archivo model.txt
model = pd.read_csv(
    "model.txt", 
    sep='\s+', 
    skiprows=3,
    parse_dates={'Timestamp': [0, 1]}, 
    index_col='Timestamp'
)

grafica = Grafica(model)
band =""

while (band!="7"):
    print("""         ***********MENU***********
        1.- Representar la matriz scatter de la velocidad y orientación del viento de los primeros mil registros.
        2.- Misma matriz scatter para los 1000 registros con mayor velocidad, ordenados.
        3.- Histograma de la velocidad del viento con 36 particiones.
        4.- Histórico de la velocidad media, con los datos agrupados por años y meses.
        5.- Tabla de velocidades medias en función del año (filas) y del mes (columnas).
        6.- Gráfica con los históricos de cada año, agrupados por meses, superpuestos.
        7.- Salir.
    """)

    band = input("Ingrese su opcion: ")
    if band == "1":
        grafica.ejercicio1()
    elif band == "2":
        grafica.ejercicio2()
    elif band == "3":
        grafica.ejercicio3()
    elif band == "4":
        grafica.ejercicio4()
    elif band == "5":
        grafica.ejercicio5()
    elif band == "6":
        grafica.ejercicio6()
    elif band == "7":
        print("Ha finalizado el programa")
    else:
        print("Ingrese una opcion valida")

