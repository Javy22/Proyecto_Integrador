

'''
Ejercicio integrador
-----------------------------
Autor: Javier Salinas
Version: 1.0
cccc
Descripción: Ejercicio final del curso PYTHON. El objetivo es conseguir 
datos mediante un menú principal en dónde conoceremos la cantidad total de veces que recetaron 
un laboratorio indicado.
También podremos lograr ver la cantidad total vendida por visitador.

En el código podemos encontrar:
    - Variables
    - Condicionales
    - Bucles
    - Funciones
    - Manejo de diccionarios
    - Manejo de archivos CSV (Comma Separated Values)
'''


import csv
from pickle import TRUE
from this import d
import registro
import random


def ingresar_datos():
    '''
    IMPORTANTE: Los datos se generan automáticamente.
    '''
    
    id = registro.generar_id()
  
    while True:
             nro_nombre = int(input('Elegir Farmacia : 1- Aguila 2- Paso 3- DTL 4- Pharma : '))
           #  categoria = str(input('Ingrese categoria :'))

             if nro_nombre == 1:
              farmacia = "Farmacia Aguila"
              break
             elif nro_nombre == 2:
              farmacia = "Farmacia Paso"
              break   
             elif nro_nombre == 3:
              farmacia = "Farmacia DTL"
              break 
             elif nro_nombre == 4:
              farmacia = "Farmacia Pharma"
              break 
    while True:
             nro_laboratorio = int(input('Elegir Laboratorio : 1- Elea 2- Pfizer 3- Roemers 4- Bago : '))
           

             if nro_laboratorio == 1:
              laboratorio = "Laboratorio Elea"
              break
             elif nro_laboratorio == 2:
              laboratorio = "Laboratorio Pfizer"
              break   
             elif nro_laboratorio == 3:
              laboratorio = "Laboratorio Roemers"
              break 
             elif nro_laboratorio == 4:
              laboratorio = "Laboratorio Bago"
              break 
   
    while True:
             nro_localidad = int(input('Elegir Localidad : 1- CABA 2- GBA 3- Interior : '))
        

             if nro_localidad == 1:
              localidad = "CABA"
              break
             elif nro_localidad == 2:
              localidad = "GBA"
              break   
             elif nro_localidad == 3:
              localidad = "Interior"
              break 
    while True:
             nro_visitador = int(input('Elegir visitador : 1- Salinas Javier 2- Gomez Hernan 3- Cervo Francisco : '))
        

             if nro_visitador == 1:
              visitador = "Salinas Javier"
              break
             elif nro_visitador == 2:
              visitador = "Gomez Hernan"
              break   
             elif nro_visitador == 3:
              visitador = "Cervo Francisco"
              break 
           
    provincia = str(input('Ingresar Provincia :'))
    medicamento = str(input('Ingresar nombre del medicamento :'))
    cantidad = int(input('Ingresar cantidad vendida :'))
   
    print('Se ingreso el seguimiento a la base',farmacia,laboratorio,localidad,provincia,visitador,medicamento,cantidad)
#crear un diccionario
    base ={}
    base["id"] = id
    base["farmacia"] = farmacia
    base["laboratorio"] = laboratorio
    base["localidad"] = localidad
    base["provincia"] = provincia
    base["visitador"] = visitador
    base["medicamento"] = medicamento
    base["cantidad"] = cantidad 
 # El newline es para que no agregue nada a la última línea
 # podría convertirlo en una funcion -- (a) para abri
    with open ("venta.csv","a", newline = "" ) as csvfile:
 #especificar la columna
     header = ["id" , "farmacia", "laboratorio" , "localidad", "provincia", "visitador", "medicamento","cantidad"]
 #crear un objeto writer
     writer = csv.DictWriter(csvfile, header)   
 #escribir la linea
     writer.writerow(base)  

       

def eliminar_visitador_por_nombre():
    '''
    Para eliminar un dato del csv, debemos leer y almacenar el resultado en una variable.
    Luego modificarlo y sobreesccribir el archivo.
    Para finalizar lo ordenamos para que sea entendible.

    '''   
# 1- Abrir el archivo y leer datos (r) es para leer
# en data tenemos una lista de diccionario
# list csv.DictReader(csvfile) nos devuelve una lista dificil de enrtender por eso le ponemos list adelante

    with open ('venta.csv', "r") as csvfile:
     data = list(csv.DictReader(csvfile))
#En este paso imprimo la lista para saber que dato borrar
    print("Imprimiendo inventario....")
    for base in data :
        print(base.get("visitador"))
    base_a_borrar = str(input("Ingrese el visitador que desea borrar : "))
    se_encontro_base = False
    for base in data:
        if base.get("visitador") == base_a_borrar :
#va a buscar la funcion dentro de registro.py
            registro.eliminar_de_lista(data,base)
            se_encontro_base = True
            break
    if se_encontro_base == False :
        print ("No se encontró el visitador a eliminar")
    else:
        print ("Encontre al Visitador")  
        registro.reordenar_ids()
# Aqui sobreescribimos el archivo con "W"
        with open ("venta.csv","w", newline="") as csvfile:
#Columnas
         header = ["id" , "farmacia", "laboratorio" , "localidad", "provincia", "visitador", "medicamento", "cantidad"]
#creo un objeto writer
         writer = csv.DictWriter(csvfile, header) 
         #escribe el header 
         writer.writeheader()
         writer.writerows (data)
         registro.reordenar_ids()


# Reporte de Cantidad vendida por Visitador
def reporte_visitador():
 def reporte_prueba(visitador): 
    data = registro.read_csv('venta.csv')
    d_visitador = {}
    suma_visitador = 0
    for i in range (len(data)):
        valores =  data[i]
        if "visitador" in valores and valores.get('visitador') == visitador:
            suma_visitador += int(valores.get('cantidad', 0))
    d_visitador['nombre'] = visitador
    d_visitador['cantidad'] = suma_visitador
    return d_visitador
 d = reporte_prueba('Salinas Javier')
 d1= reporte_prueba('Gomez Hernan')
 d2= reporte_prueba('Cervo Francisco')
 
 if d.get('Javier Salinas') == 0:
    print('No existe ese Visitador')
 if d.get('Gomez Hernan') == 0:
    print('No existe ese Visitador')
 if d.get('Cervo Francisco') == 0:
    print('No existe ese Visitador')

 else:
     print('Visitador:', d)
     print('Visitador:', d1)
     print('visitador:', d2)
 

# En la siguiente función vamos a generar reporte por Laboratorio
# indica que cantidad fue recetada por farmacia.           
def generar_posicion():
 with open ('venta.csv','r') as archivo:
        data = list(csv.DictReader(archivo))
        laboratorio_elea = 0
        laboratorio_pfizer= 0
        laboratorio_roemers = 0
        laboratorio_bago = 0
        try:
            for i in range (len(data)):
                valores =  data[i]
                for k,v in valores.items():
                    if k == "laboratorio" and v == "Laboratorio Elea":
                        laboratorio_elea += 1
                    if k == "laboratorio" and v == "Laboratorio Pfizer":
                        laboratorio_pfizer += 1
                    if k == "laboratorio" and v == "Laboratorio Roemers":
                        laboratorio_pfizer += 1   
                    if k == "laboratorio" and v == "Laboratorio Bago":
                        laboratorio_pfizer += 1     
        except:
            print("{} No se encuentra registro".format(i))
 print("La cantidad de ventas del Laboratorio Elea es :{}".format(laboratorio_elea))
 print("La cantidad de ventas del Laboratorio Pfizer es :{}".format(laboratorio_pfizer))
 print("La cantidad de ventas del Laboratorio Roemers es :{}".format(laboratorio_roemers))
 print("La cantidad de ventas del Laboratorio Bago es :{}".format(laboratorio_bago))
 
#########################################################################

# Vista general del reporte, el el muestra todo el contenido del csv
def registro_general():
    with open ('venta.csv', "r") as csvfile:
     data = list(csv.DictReader(csvfile))
# Aquí se imprime el listado csv
    print("Imprimiendo base....")
    for base in data :
        print(base.get("id"), base.get("farmacia"), base.get("laboratorio"),base.get("localidad"),base.get("provincia"),base.get("visitador"),base.get("medicamento"),base.get("cantidad"))
        
           

if __name__ == '__main__':

    # 1. Preguntarle al usuario qué desea hacer
    menu = '''\n
    Seleccione una opcion:
    1. Ingresar nuevo registro 
    2. Eliminar un registro
    3. Consulta de ventas por Laboratorio 
    4. Consultar registro venta por visitador
    5. Consulta general de los registros
    Cualquier otro valor - Finalizar ejecución del programa
    Opcion elegida:'''

    while True:
        opcion = int(input(menu))
        print(f'\nElegiste la opción: {opcion}\n')  # Menú principal

        if opcion == 1:
            # Ingresar un nuevo dato
            ingresar_datos()
            print('Seguimniento Ingresado al inventario')

        elif opcion == 2:
            # Elimina visitador de una lista impresa
            eliminar_visitador_por_nombre()
            print('¡El visitador ya no se encuentra en la base!')
            
        elif opcion == 3:
            # Posicionamiento en Mercado
           generar_posicion()
           print('¡Reporte de ventas realizadas finalizado!')

        elif opcion == 4:
            # Genera reporte de ventas por visitador
            reporte_visitador()   
            print('¡Reporte de ventas por Visitador terminado!')
        elif opcion == 5:
           registro_general()   
           print('¡Base de datos general')
            
        else:
            # Finalizar ejecución
         print('¡Fin del programa!')
        break