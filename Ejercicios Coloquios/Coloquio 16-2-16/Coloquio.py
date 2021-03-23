"""La empresa Mudanzas El Neutral ofrece un servicio extra a sus clientes para asegurarles que todas
las cosas que salen del origen llegan efectivamente a destino. Para esto, los clientes imprimen
etiquetas con códigos QR que se pegan a los distintos elementos transportados. Estas etiquetas
son escaneadas al salir de origen y al llegar a destino. Se tienen luego dos archivos con el mismo
formato: salida.csv, llegada.csv (ordenados por id creciente):
 id,hora,volumen_en_m3,peso_en_kg,descripción
Se requiere procesar ambos archivos al finalizar la mudanza para:
● Detectar si hubo elementos que no llegaron a desƟno. En caso de haberlos, se deberá generar
un archivo faltantes.txt donde por cada línea se registre: “El artículo descripción con hora de salida
hh:mm:ss no llegó a destino”.
● Detectar si hubo pérdida de elementos dentro de los cajones (diferencia de peso en desƟno
inferior en 0,25 kg o más). Registrar en faltantes.txt: “El cajón descripción salió con peso_en_kg kg
de origen y llegó con peso_en_kg kg a destino”.
● Informar por pantalla el volúmen y peso total de salida y llegada.
● El formato de la hora en los archivos es hhmmss (por ejemplo, 184802).
● Suponer que los archivos existen y que todas las líneas Ɵenen el formato esperado.
● Los archivos no pueden cargarse en memoria ya que no hay un límite predefinido.
● Considerar que nunca se registran en desƟno elementos que no salieron en origen."""

def leer_linea(archivo):
    linea = archivo.readline()
    linea = linea.rstrip("\n")
    if not linea:
        return None
    return linea.split(',')

def calcular_peso(peso_salida, peso_llegada):
    diferencia = float(peso_salida) - float(peso_llegada)
    return diferencia >= 0.25

def modificar_formato_hora(hora):
    string = str(hora)
    return "{}:{}:{}".format(string[:2], string[2:4], string[4:6])

salida = open("salida.csv.txt")
llegada = open("llegada.csv.txt")
faltantes = open("faltates.txt", 'w')

s = leer_linea(salida)
l = leer_linea(llegada)

volumen_salida = 0
volumen_llegada = 0
while s and l:
    if s[0] < l[0]:
        hora_salida = modificar_formato_hora(s[1])
        faltantes.write("El artículo {} con hora de salida {} no llegó a destino\n".format(s[4], hora_salida))
        volumen_salida += int(s[2])
        s = leer_linea(salida)
    elif s[0] == l[0]:
        volumen_salida += int(s[2])
        volumen_llegada += int(l[2])
        if calcular_peso(s[3], l[3]):
            faltantes.write("El cajón {} salió con {} kg de origen y llegó con {} kg a destino\n".format(s[4], s[3], l[3]))
        s = leer_linea(salida)
        l = leer_linea(llegada)

while s:
    hora_salida = modificar_formato_hora(s[1])
    faltantes.write("El artículo {} con hora de salida {} no llegó a destino\n".format(s[4], hora_salida))
    volumen_salida += int(s[2])
    s = leer_linea(salida)

print("Volumen salida {} y de llegada {}".format(volumen_salida, volumen_llegada))

faltantes.close()
llegada.close()
salida.close()