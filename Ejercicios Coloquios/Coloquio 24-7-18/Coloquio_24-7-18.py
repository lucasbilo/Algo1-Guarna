from datetime import datetime

def leer_linea(archivo):
    linea = archivo.readline()
    linea = linea.rstrip("\n")
    if not linea:
        linea = None
    return linea

def agregar_a_archivo(archivo, linea):
    archivo.write("{}\n".format(linea))

def es_proximo_a_jubilarse(nacimiento_entero, legajo, nombre, telefono):
    nacimiento = str(nacimiento_entero)
    nac = datetime(int(nacimiento[:4]), int(nacimiento[4:6]), int(nacimiento[6:8]))
    hoy = datetime.now()
    rectifico = datetime(hoy.year, nac.month, nac.day) >= hoy
    edad = hoy.year - nac.year - rectifico
    if edad >= 69:
        print("{} - {} - {}".format(legajo, nombre, telefono))


empleados = open("EMPLEADOS.CSV.txt")
novedades = open("NOVEDADES.CSV.txt")
actualizado = open("ACTUALIZADO.CSV", 'w')
errores = open("LOG.CSV", 'w')

empl = leer_linea(empleados)
novs = leer_linea(novedades)

print("*** EMPLEADOS PROXIMOS A JUBILARSE ***")
print("LEGAJO - NOMBRE - TELEFONO")
while empl and novs:
    l_empl = empl.split(',')
    l_novs = novs.split(',')
    if l_empl[0] < l_novs[0]:
        agregar_a_archivo(actualizado, empl)
        es_proximo_a_jubilarse(int(l_empl[4]), l_empl[0], l_empl[1], l_empl[3])
        empl = leer_linea(empleados)
    elif l_empl[0] > l_novs[0]:
        if l_novs[5] == 'A':
            agregar_a_archivo(actualizado, novs)
            es_proximo_a_jubilarse(l_novs[4], l_novs[0], l_novs[1], l_novs[3])
        else:
            agregar_a_archivo(errores, novs)
        novs = leer_linea(novedades)
    else: # son iguales
        if l_novs[5] == 'M':
            agregar_a_archivo(actualizado, novs)
        elif l_novs[5] == 'A':
            agregar_a_archivo(errores, novs)
        es_proximo_a_jubilarse(int(l_empl[4]), l_empl[0], l_empl[1], l_empl[3])
        empl = leer_linea(empleados)
        novs = leer_linea(novedades)

while empl:
    agregar_a_archivo(actualizado, novs)
    l_empl = empl.split(',')
    es_proximo_a_jubilarse(int(l_empl[4]), l_empl[0], l_empl[1], l_empl[3])
    novs = leer_linea(novedades)

while novs:
    l_novs = novs.split(',')
    if l_novs[5] == 'A':
        agregar_a_archivo(actualizado, novs)
        es_proximo_a_jubilarse(int(l_novs[4]), l_novs[0], l_novs[1], l_novs[3])
    else:
        agregar_a_archivo(errores, novs)
    novs = leer_linea(novedades)


empleados.close()
novedades.close()
errores.close()
actualizado.close()