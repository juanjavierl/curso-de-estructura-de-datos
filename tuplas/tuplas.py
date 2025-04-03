celular = 78554845
peso = 55.20
estado = True

datos = celular, peso, estado
print("Datos: ", datos)
#maenjos de tuplas
#Esto es una tupla en python
carreras = ('informatica', 'contabilidad', 'fisica', 'quimica', 'matematicas')
print(type(carreras))
print(carreras[2:])
print("Logitud de valores: ",len(carreras))

alumno = (89766, "Alicia", "Hacker", (9, "Julio", 1988))

print(alumno[3][2])

#print(list(carreras))#convercion de una lista

#ITERACION DE UNA TUPLA
alumnos = [
    ('Perico', 'Los Palotes', '201199001-5', 'Civil'),
    ('Fulano', 'De Tal',      '201199002-6', 'Electrica'),
    ('Beymar', 'De Tal',      '201199003-7', 'Mecanica'),
]


for i in alumnos:
    print(i[0], i[3])