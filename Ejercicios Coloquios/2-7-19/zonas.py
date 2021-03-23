MAX = '99999999999'
def leer_linea(archivo):
    linea = archivo.readline()
    if not linea:
        linea = MAX
    linea = linea.rstrip("\n")
    return linea.split(',')

def cargar_a_archivo(archivo, codigo, importe):
    archivo.write("{},{}\n".format(codigo, importe))

z1 = open("ZONA1.txt")
z2 = open("ZONA2.txt")
z3 = open("ZONA3.txt")
z4 = open("ZONA4.txt")
res = open("RES_COMPRAS.CSV", 'w')

zona1 = leer_linea(z1)
zona2 = leer_linea(z2)
zona3 = leer_linea(z3)
zona4 = leer_linea(z4)

while (zona1[0] != MAX) or (zona2[0] != MAX) or (zona3[0] != MAX) or (zona4[0] != MAX):
    importe = 0
    codigo_actual = min(int(zona1[0]), int(zona2[0]), int(zona3[0]), int(zona4[0]))
    while int(zona1[0]) == codigo_actual:
        importe += int(zona1[1])
        zona1 = leer_linea(z1)
    while int(zona2[0]) == codigo_actual:
        importe += int(zona2[1])
        zona2 = leer_linea(z2)
    while int(zona3[0]) == codigo_actual:
        importe += int(zona3[1])
        zona3 = leer_linea(z3)
    while int(zona4[0]) == codigo_actual:
        importe += int(zona4[1])
        zona4 = leer_linea(z4)
    cargar_a_archivo(res, codigo_actual, importe)

z1.close()
z2.close()
z3.close()
z4.close()
res.close()