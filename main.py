import flet as ft
import numpy as np
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment
import conversiones
import gauss_seidel


def main(page: Page) ->None:
    page.title = 'Calculo Numerico'
    #page.theme_mode = ft.ThemeMode.DARK
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 600 #Ancho 600
    page.window_height = 620  #Alto
    page.window_resizable = False #Para que no se pueda redimensionar
    page.window_center()
    page.padding = 0  #que no haya espaciado entre los elementos
    """
    contenedor = ft.Container(width=600,height=620,bgcolor=ft.colors.WHITE,alignment=ft.alignment.top_center)
    """

    items = []
    items2 = []
    
    #defino los textfield y el combobox
    dd = ft.Dropdown(
        width=130,
        hint_text="Base" ,
        options=[
            ft.dropdown.Option("decimal"),
            ft.dropdown.Option("binario"),
            ft.dropdown.Option("ternario"),
            ft.dropdown.Option("cuaternario"),
            ft.dropdown.Option("octal"),
            ft.dropdown.Option("hexadecimal"),
        ],
    )

    
    #print(dd.value)
    texto = ft.TextField(label="número")
    texto2 = ft.TextField(label="resultado",multiline=True,value="\n\n")
    botonConvertir =ElevatedButton(text='   Convertir   ',disabled=True)
    bb =ElevatedButton(text='Limpiar')
    items.append(texto)
    items.append(dd)
    
    items2.append(texto2)
    items2.append(botonConvertir)
    row = ft.Row(spacing=10, controls=items,alignment=MainAxisAlignment.CENTER)
    row2 = ft.Row(spacing=10, controls=items2,alignment=MainAxisAlignment.CENTER)
    bb =ElevatedButton(text='Limpiar')

    #Funcion que valida que haya un valor en el txt y en el combobox
    def validate(e: ft.ControlEvent) ->None:
        if all([texto.value,dd.value]):
            botonConvertir.disabled=False
        else:
            botonConvertir.disabled=True

        page.update()
    
    
    #Funcion del boton convertir
    def button_clicked(e: ft.ControlEvent) ->None:
        texto2.value=conversiones.basen(dd.value,texto.value)
        page.update()

    #Funcion del boton limpiar
    def button_clicked2(e: ft.ControlEvent) ->None:
        texto.value = None
        texto2.value= None
        botonConvertir.disabled=True
        page.update()

    dd.on_change = validate
    texto.on_change = validate
    botonConvertir.on_click = button_clicked
    bb.on_click= button_clicked2

    #Controles de la pagina de Gauss-seidel
    item3=[]
    item4=[]
    item5=[]
    item6=[]
    txtTamano = ft.TextField(label="dimensión")
    txtIngresar = ft.TextField(label="Matriz A: a11",disabled=True)
    txtVector = ft.TextField(label="Vector b: b1",disabled=True)
    txtEcuacion = ft.TextField(label="Ecuaciones",multiline=True,value="\n\n",disabled=True)
    botonTamano = ElevatedButton(text = 'Aceptar')
    botonAgregar = ElevatedButton(text = 'Agregar',disabled=True)
    botonAgregar2 = ElevatedButton(text = 'Agregar',disabled=True)
    botonResolver = ElevatedButton(text = 'Resolver',disabled=True)
    botonReiniciar = ElevatedButton(text = 'Reiniciar')
    item3.append(txtTamano)
    item3.append(botonTamano)
    item4.append(txtIngresar)
    item4.append(botonAgregar)
    item5.append(txtVector)
    item5.append(botonAgregar2)
    item6.append(txtEcuacion)
    item6.append(botonResolver)
    row3 = ft.Row(spacing=10,controls=item3,alignment=MainAxisAlignment.CENTER)
    row4 = ft.Row(spacing=10,controls=item4,alignment=MainAxisAlignment.CENTER)
    row5 = ft.Row(spacing=10,controls= item5,alignment=MainAxisAlignment.CENTER)
    row6 = ft.Row(spacing=10,controls= item6,alignment=MainAxisAlignment.CENTER)
    
    #Funcion para indicar la dimension de la matriz
    def button_clicked3(e: ft.ControlEvent) ->None:
        if(gauss_seidel.entero(txtTamano.value)):
            n = int(txtTamano.value)
            gauss_seidel.matriz = np.zeros((n,n))
            gauss_seidel.vector = np.zeros(n)
            
            txtTamano.disabled = True
            botonTamano.disabled = True
            botonAgregar.disabled = False
            txtIngresar.disabled = False
        page.update()
    #Funcion para agregar los numeros de la matriz
    def button_clicked4(e: ft.ControlEvent) ->None:
        if(gauss_seidel.es_numero(txtIngresar.value)):
            
            f = gauss_seidel.fila
            c = gauss_seidel.col
            
            gauss_seidel.matriz[f][c]=int(txtIngresar.value)
            txtIngresar.value=""
            if((gauss_seidel.col ==(len(gauss_seidel.matriz)-1)))and((gauss_seidel.fila ==(len(gauss_seidel.matriz)-1))):
                txtIngresar.label = "Matriz A: a"+str(gauss_seidel.fila+2)+str(gauss_seidel.col+2)
                gauss_seidel.col = 0
                gauss_seidel.fila =0
                
                
                botonAgregar2.disabled = False
                txtVector.disabled = False
                botonAgregar.disabled = True
                txtIngresar.disabled = True
                txtIngresar.label = "Matriz A: a"+str(gauss_seidel.fila+1)+str(gauss_seidel.col+1)
            elif(gauss_seidel.col ==(len(gauss_seidel.matriz)-1)):
                gauss_seidel.col = 0
                gauss_seidel.fila +=1
                txtIngresar.label = "Matriz A: a"+str(gauss_seidel.fila+1)+str(gauss_seidel.col+1)
            else:
                gauss_seidel.col +=1
                txtIngresar.label = "Matriz A: a"+str(gauss_seidel.fila+1)+str(gauss_seidel.col+1)
        page.update()
    #Funcion para agregar los elementos del vector            
    def button_clicked5(e: ft.ControlEvent) ->None:
        if(gauss_seidel.es_numero(txtVector.value)):
            
            
            gauss_seidel.vector[gauss_seidel.pos]=int(txtVector.value)
            txtVector.label = "Vector b: b"+str(gauss_seidel.pos+2)
            gauss_seidel.pos+=1
            txtVector.value = ""
            if(gauss_seidel.pos == len(gauss_seidel.matriz)):
                
                botonAgregar2.disabled = True
                txtVector.disabled = True
                txtEcuacion.disabled = False
                botonResolver.disabled = False
                txtEcuacion.value = gauss_seidel.ecuacion(gauss_seidel.matriz,gauss_seidel.vector)
                gauss_seidel.result = np.zeros_like(gauss_seidel.vector)
        page.update()
    #Accion del boton resolver        
    def button_clicked6(e: ft.ControlEvent) ->None:
        
        cadena=""
        gauss_seidel.diagonal_dominante(gauss_seidel.matriz,gauss_seidel.vector)
        gauss_seidel.gauss(gauss_seidel.matriz,gauss_seidel.vector,gauss_seidel.result,0.01,30)
        #tiene_ceros = np.any(gauss_seidel.result)
        
        for i in range(len(gauss_seidel.result)):
            if (i != (len(gauss_seidel.result)-1)):
                cadena+="x"+str(i+1)+"="+str(gauss_seidel.result[i])+"\n"
            else:
                cadena+="x"+str(i+1)+"="+str(gauss_seidel.result[i])
        
        txtEcuacion.label="Solución"     
        txtEcuacion.value = cadena       
        page.update()
    #Accion del boton reiniciar
    def button_clicked7(e: ft.ControlEvent) ->None:
        gauss_seidel.matriz = None
        gauss_seidel.vector = None
        gauss_seidel.result = None
        gauss_seidel.fila = 0
        gauss_seidel.col = 0
        gauss_seidel.pos = 0
        txtTamano.value = ""
        txtTamano.disabled = False
        botonTamano.disabled = False
        txtEcuacion.disabled = True
        txtEcuacion.value = ""
        txtVector.label = "Vector b: b1"
        botonResolver.disabled = True

        page.update()

    botonTamano.on_click = button_clicked3
    botonAgregar.on_click = button_clicked4
    botonAgregar2.on_click = button_clicked5
    botonResolver.on_click = button_clicked6
    botonReiniciar.on_click = button_clicked7

    #Esta funcion se encarga de nuestras vistas y navegaciones
    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()
        #Menu
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Menú'),bgcolor = 'blue'), #Barra superior
                    Text(value = 'Menú',size = 30), #Funciona como una etiqueta
                    ElevatedButton(text='  Método Gauss-Seidel  ', on_click=lambda _: page.go('/gauss')),
                    ElevatedButton(text='Conversiones Numéricas', on_click=lambda _: page.go('/conver'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        #Pagina Gauss Seidel
        if page.route == '/gauss':
            page.views.append(
                View(
                    route='/gauss',
                    controls=[
                        AppBar(title=Text('Gauss-Seidel'),bgcolor = 'blue'),
                        Text(value = 'Gauss-Seidel',size = 30),
                        row3,
                        row4,
                        row5,
                        row6,
                        botonReiniciar
                        #ElevatedButton(text='Regresar a menu', on_click=lambda _: page.go('/'))#Boton que va en el borde superior
                    ],
                    vertical_alignment=MainAxisAlignment.START,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=20
                )
            )
        
        #Pagina Coversiones
        if page.route == '/conver':
            page.views.append(
                View(
                    route='/conver',
                    controls=[
                        AppBar(title=Text('Conversiones Numéricas'),bgcolor = 'blue'),
                        Text(value = 'Conversiones Numéricas',size = 30),
                        row,
                        row2,
                        bb
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )


        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)
    #page.add(contenedor)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)