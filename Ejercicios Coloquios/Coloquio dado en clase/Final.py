MAX = '9999999'

def leer_linea(archivo):
    linea = archivo.readline()
    if not linea:
        linea = MAX
    linea = linea.rstrip("\n")
    return linea.split(',')

def esta_en_diccionario(clave, diccionario):
    if clave in diccionario:
        return True
    return False

def esta_en_lista(tipo, lista):
    for i in range(len(lista)):
        if tipo in lista[i]:
            return i
    return None

def cargar_a_dicc_alumnos(alumno, alumnos):
    nota = int(alumno[4])
    if not esta_en_diccionario(alumno[0], alumnos):
        alumnos[alumno[0]] = 0
    if nota >= 4:
        alumnos[alumno[0]] += 1

def cargar_a_dicc_estadisticas(alumno, estadisticas):
    nota = int(alumno[4])
    carrera = alumno[1]
    tipo_evaluacion = alumno[3]
    if not esta_en_diccionario(carrera, estadisticas):
        estadisticas[carrera] = [[tipo_evaluacion, nota, 1]]
    i = esta_en_lista(tipo_evaluacion, estadisticas[carrera])
    if i != None:
        estadisticas[carrera][i][1] += nota
        estadisticas[carrera][i][2] += 1
    else:
        estadisticas[carrera].append([tipo_evaluacion, nota, 1])


lh = open("LH.txt")
pc = open("PC.txt")
cu = open("CU.txt")
lu = open("LU.txt")
aprobados = open("aprobados.csv", 'w')

alumno_lh = leer_linea(lh)
alumno_pc = leer_linea(pc)
alumno_cu = leer_linea(cu)
alumno_lu = leer_linea(lu)

alumnos = {}
estadisticas = {}
while (alumno_pc[0] != MAX) or (alumno_cu[0] != MAX) or (alumno_lh[0] != MAX) or (alumno_lu[0] != MAX):
    padron_actual = min(alumno_pc[0], alumno_lh[0], alumno_lu[0], alumno_cu[0])
    if alumno_pc[0] == padron_actual:
        cargar_a_dicc_alumnos(alumno_pc, alumnos)
        cargar_a_dicc_estadisticas(alumno_pc, estadisticas)
        alumno_pc = leer_linea(pc)
    if alumno_lh[0] == padron_actual:
        cargar_a_dicc_alumnos(alumno_lh, alumnos)
        cargar_a_dicc_estadisticas(alumno_lh, estadisticas)
        alumno_lh = leer_linea(lh)
    if alumno_cu[0] == padron_actual:
        cargar_a_dicc_alumnos(alumno_cu, alumnos)
        cargar_a_dicc_estadisticas(alumno_cu, estadisticas)
        alumno_cu = leer_linea(cu)
    if alumno_lu[0] == padron_actual:
        cargar_a_dicc_alumnos(alumno_lu, alumnos)
        cargar_a_dicc_estadisticas(alumno_lu, estadisticas)
        alumno_lu = leer_linea(lu)

for padron in alumnos:
    aprobados.write("{},{}\n".format(padron, alumnos[padron]))
    print("Padron : {}, Notas aprobadas : {}".format(padron, alumnos[padron]))

for carreras in estadisticas:
    print("Promedios para la carrera {}.".format(carreras))
    for i in range(len(estadisticas[carreras])):
        promedio = int(estadisticas[carreras][i][1]) / int(estadisticas[carreras][i][2])
        print("Tipo de evaluacion {}, tiene un promedio de {}".format(estadisticas[carreras][i][0], round(promedio,2)))


lh.close()
pc.close()
cu.close()
lu.close()
aprobados.close()
