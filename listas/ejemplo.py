def invertir_cadenas(cadena):

    textos_invertidos = []
    for texto in cadena.split():
        """ txt = ''
        for i in range(len(texto)-1, -1, -1):
            txt += texto[i] """
        txt = texto[::-1]
        textos_invertidos.append(txt)
    print(" ".join(textos_invertidos))
        
    #juan perez   >>  nauj zerep

cadena = input("Escriba un texto: ")
invertir_cadenas(cadena)



""" oso    oso

ana    ana 

reconocer  reconocer 

juan    nauj

maria  = airam

dado un cadena como parametro crear una
funcion para
determinar si esta palabra es palindromo """

def palindromo(cadena):
    for texto in cadena.split():
        txt = texto[::-1]
        if txt == cadena:
            print("Es palindromo")
        else:
            print("No es palindromo")

cadena = input("Escriba un texto: ")
palindromo(cadena)