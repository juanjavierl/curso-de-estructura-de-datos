def agregarAlumnos():
    alumnos={
        0:{'nombre': "juan david",'notas':[60,55,75]},
        1:{'nombre': "Rodrigo",'notas':[50,30,45]},
        2:{'nombre': "david",'notas':[70,55,75]},
        3:{'nombre': "Jhennet",'notas':[60,65,85]},
        4:{'nombre': "Beto",'notas':[25,50,35]}
    }
    for alumno in alumnos:
        total =  alumnos[alumno]['notas'][0] + alumnos[alumno]['notas'][1] + alumnos[alumno]['notas'][2]
        promedio = total//len(alumnos[alumno]['notas'])
        estado = ""
        if promedio >=61:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        print(alumnos[alumno]['nombre'], alumnos[alumno]['notas'][0], alumnos[alumno]['notas'][1], 
              alumnos[alumno]['notas'][2], " Total: ",total , "Prom: ", promedio, estado)

agregarAlumnos()