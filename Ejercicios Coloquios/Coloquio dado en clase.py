#Creo el archivo saldo_anual
import pickle
from utils import leer_desde_archivo

def cargar_a_binario(archivo, nro_cta, nombre, apellido, saldo):
    lista = [nro_cta, nombre, apellido, saldo]
    pickle.dump(lista, archivo)

an = open("saldo_anual.dat", 'rb')
mov = open("movi.dat", 'rb')
actual = open("saldo_actual.dat", 'wb')

an, fin_a = leer_desde_archivo(an)
movimientos, fin_m = leer_desde_archivo(mov)

while (fin_a == True) and (fin_m == True):
    nro_an, nombre, apellido, saldo = an.split(',')
    nro_mov, importe = movimientos.split(',')
    if nro_an < nro_mov:
        cargar_a_binario(actual, nro_an, nombre, apellido, saldo)
        an, fin_a = leer_desde_archivo(an)
    elif nro_an == nro_mov:
        cargar_a_binario(actual, nro_an, nombre, apellido, saldo + importe)
        an, fin_a = leer_desde_archivo(an)
        movimientos, fin_m = leer_desde_archivo(mov)
