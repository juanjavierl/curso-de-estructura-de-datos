#diccionario = dict(clave1="valor1", clave2="valor2")

diccionario = {
        'clave1':'valor1',
         1:'uno',
        'cursos':['python','PHP','C++'],
        'numeros':{'uno':1, 'dos':2}
    }

diccionario['clave1'] = 'juan david'

del diccionario['cursos']
print(len(diccionario))
print(diccionario)

print(diccionario.values())

""" for c, v in diccionario.items():
    print(c, " => ", v) """

for i in diccionario:
    print(i, " => ", diccionario[i])
