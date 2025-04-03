"""
2.- Escribir un programa que almacene en una tupla los 
siguientes precios, 50, 75, 46, 22, 80, 65, 8, y 
muestre por pantalla del menor y el mayor de los precios.
"""
def hallar_mayor_menor():
    precios = (50, 75, 46, 22, 80, 65, 8)
    mayor = precios[0]
    for i in precios:
        if i > mayor:
            mayor = i
    print("El ele3mento Mayor es: ", mayor)

hallar_mayor_menor()