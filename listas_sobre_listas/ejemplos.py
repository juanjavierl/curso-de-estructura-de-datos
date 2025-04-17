matriz = [
            [2,4,6,8,10,12],
            [0,1,0,1,0,1],
            [7,11,12,17,19,21],
            [1,3,5,7,9,11],
            [5,15,20,25,30,35]
         ]

def buscar_elemento(multi_lista):
    #buscar un elemento destro de la lista multinivel
    valor = int(input("Ingrese el valor a buscar: "))
    for fila in range(0, len(multi_lista),1):
        print(multi_lista[fila])
    print("La lista que llego: ",multi_lista)
    print(type(multi_lista))

def multi_lista():
    fila = int(input("Ingrese el num. de filas: "))#ingresamos un número de filas
    columna = int(input("Ingrese el num. de Columnas: "))#número de columnas
    multi_lista = [] #inicializamos una lista vacía
    for f in range(0, fila,1):
        lista = []
        for c in range(0, columna, 1):
            print("Ingrese valor en el indice:",f," : ",c)
            valor = int(input())
            lista.append(valor)  
        multi_lista.append(lista)
    buscar_elemento(multi_lista)

multi_lista()#llamada a la función