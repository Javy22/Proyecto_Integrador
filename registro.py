

'''
Registro para utilizar en reporte
-----------------------------
Autor: Salinas Javier
Version: Proyecto integrador

Descripción: Este módulo contiene las funciones
    - Buscar 
    - Generar un IDpara cada visitador 
    - Reordenar IDs de un archivo CSV
    - Eliminar un visitador de una lista
    - Se toma como ejemplo la una de las últimas clases, me pareció prudente dejar algunos comentarios
    para poder entender que hace el código, sí bien son similares a los de la clase, cero que me ayuda 
    a entender.
'''

import csv

def generar_id():
    '''
    Funcion para obtener el ID al insertar un nuevo registrp, el ID que devuelve
    es el último ID registrado + 1

    Ejemplo de funcionamiento
    CSV de entrada
        |----|-----------------|------------------- |------------|-----------|-----------------|-------------|----------|
        | id | farmacia        | laboratorio        | localidad  | provincia | visitador       | medicamento | cantidad |
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        |  1 | Farmacia Aguila | Laboratorio Elea   | CABA       | Bs As     |Salinas Javier   | Omatex      | 30       | 
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        |  2 | Farmacia Paso   | Laboratorio Pfizer | GBA        | Córdoba   |Salinas Felipe   | Aziatop     | 40       |
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        |  3 | Farmacia DTL    | Laboratorio Roemers| Interior   | Mendoza   |Salinas Victoria | Lipex       | 50       | 
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|

    Valor de retorno → 3 + 1 → 4
    '''
    with open('venta.csv') as csvfile:
    # Leo el archivo CSV y lo almaceno en data
        data = list(csv.DictReader(csvfile))

    # Obtengo la ultima fila del CSV 
    ultima_fila = data[-1]

    # Obtener el ID de la última fila
    ultimo_id = int(ultima_fila.get('id'))
    
    # Aumento en 1 el ID encontrado, y retornarlo
    return ultimo_id + 1
    
def reordenar_ids():
    '''
    Función para que reordenar los IDs del CSV venta
    
    Ejemplo de funcionamiento:

    CSV de entrada
        |----|-----------------|------------------- |------------|-----------|-----------------|-------------|----------|
        | id | farmacia        | laboratorio        | localidad  | provincia | visitador       | medicamento | cantidad |
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        | 4  | Farmacia Aguila | Laboratorio Elea   | CABA       | Bs As     |Salinas Javier   | Omatex      | 30       | 
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        | 3  | Farmacia Paso   | Laboratorio Pfizer | GBA        | Córdoba   |Salinas Felipe   | Aziatop     | 40       |
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        | 1  | Farmacia DTL    | Laboratorio Roemers| Interior   | Mendoza   |Salinas Victoria | Lipex       | 50       | 
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        
    CSV de salida

        |----|-----------------|------------------- |------------|-----------|-----------------|-------------|----------|
        | id | farmacia        | laboratorio        | localidad  | provincia | visitador       | medicamento | cantidad |
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        |  1 | Farmacia Aguila | Laboratorio Elea   | CABA       | Bs As     |Salinas Javier   | Omatex      | 30       | 
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        |  2 | Farmacia Paso   | Laboratorio Pfizer | GBA        | Córdoba   |Salinas Felipe   | Aziatop     | 40       |
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|
        |  3 | Farmacia DTL    | Laboratorio Roemers| Interior   | Mendoza   |Salinas Victoria | Lipex       | 50       | 
        |----|-----------------|--------------------|------------|-----------|-----------------|-------------|----------|


            '''

    with open('venta.csv', 'r') as csvfile:
      data = list(csv.DictReader(csvfile))

    for i in range(len(data)):
        # Asignar como id de un visitador, su índice en la lista + 1, para no asignarle a nadie el ID = 0
        data[i]['id'] = i + 1

    with open('venta.csv', 'w') as csvfile:
        # Especificar cuales serán las columnas del CSV
        header = ['id', 'farmacia', 'laboratorio', 'localidad', 'provincia', 'visitador', 'medicamento','cantidad']

        # Construir el objeto writer, que se encargará de escribir el csv
        writer = csv.DictWriter(csvfile, fieldnames = header)

        # Escribir los nombres de las columnas
        writer.writeheader()

        # Escribe el dato
        writer.writerows(data)



def eliminar_de_lista(lista, elemento):
    '''
    función que elimina un elemento de una lista
    '''
    lista.pop(lista.index(elemento))

def read_csv(filename):
     with open(filename, 'r') as csvfile:
        data=list(csv.DictReader(csvfile))
     return data

