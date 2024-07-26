import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#para visualizar tabla
import seaborn as sns

class Grafica:
    def __init__(self,model):
        self.model = model

    def ejercicio1(self):
        # Extraer los primeros 1000 registros
        data_subset = self.model.loc[self.model.index[:1000], ['M(m/s)', 'D(deg)']]
        # Crear la matriz de dispersión (scatter matrix)
        pd.plotting.scatter_matrix(data_subset, alpha=0.75, figsize=(6, 6), diagonal='kde')
        plt.suptitle("Scatter Matrix de Velocidad y Orientación del Viento")
        plt.show()

    def ejercicio2(self):
        pd.plotting.scatter_matrix(
            self.model.loc[self.model.sort_values('M(m/s)', ascending=False).index[:1000],
            'M(m/s)':'D(deg)']
        )
        plt.suptitle("Scatter Matrix mayor Velocidad ordenados")
        plt.show()
    
    def ejercicio3(self):
        self.model['M(m/s)'].plot.hist(bins=np.arange(0, 36))  # Corregido para usar 36 particiones
        plt.suptitle("Histograma de la velocidad del viento con 36 particiones")
        plt.xlabel("Velocidad del Viento (m/s)")
        plt.ylabel("Frecuencia")
        plt.show()

    def ejercicio4(self):
        # Extraer año y mes
        self.model['year'] = self.model.index.year
        self.model['month'] = self.model.index.month
        # Agrupar por año y mes y calcular la media
        media_mensual = self.model.groupby(['year', 'month']).mean()
        print("Historico de la velocidad media")
        #print(media_mensual[['M(m/s)']].head(36))
        print(media_mensual.head(36))
        media_mensual.plot(y='M(m/s)', figsize=(15, 5))
        plt.title('Velocidad media del viento por año y mes')
        plt.xlabel('Año, Mes')
        plt.ylabel('Velocidad media del viento (m/s)')
        plt.show()

    def ejercicio5(self):
        # Extraer año y mes
        self.model['year'] = self.model.index.year
        self.model['month'] = self.model.index.month

        # Agrupar por año y mes y calcular la media
        media_mensual = self.model.groupby(['year', 'month']).mean()

        # Pivotar los datos para tener los meses como columnas y los años como filas
        pivot_table = media_mensual.loc[:, 'M(m/s)'].reset_index().pivot(index='year', columns='month')

        # Mostrar la tabla pivotada
        print(pivot_table)

        plt.figure(figsize=(15, 10))
        sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="viridis")
        plt.title('Histórico de la velocidad media del viento por año y mes')
        plt.xlabel('Mes')
        plt.ylabel('Año')
        plt.show()

    def ejercicio6(self):
        # Extraer año y mes
        self.model['year'] = self.model.index.year
        self.model['month'] = self.model.index.month

        # Agrupar por año y mes y calcular la media
        monthly_mean = self.model.groupby(['year', 'month']).mean()

        # Pivotar los datos para tener los meses como columnas y los años como filas
        pivot_table = monthly_mean.loc[:, 'M(m/s)'].reset_index().pivot(index='year', columns='month')

        # Mostrar la tabla pivotada
        print(pivot_table)

        # Plotear la tabla pivotada transpuesta
        pivot_table.T.plot(figsize=(15, 5), legend=False)
        plt.title('Velocidad media del viento por año y mes')
        plt.xlabel('Mes')
        plt.ylabel('Velocidad media del viento (m/s)')
        plt.show()















