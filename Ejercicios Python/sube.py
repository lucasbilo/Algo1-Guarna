# ALGORITMO QUE SIMULA EL SISTEMA DE SUBE DE UN TRANSPORTE.

cantidad_de_tarifas = 0
total_recaudado = 0
tarifa = int(input("Ingrese tarifa o 0 para salir: "))
while tarifa != 0:
    saldo = int(input("Ingrese saldo: "))
    if saldo >= tarifa:
        print("Saldo restante: ", saldo - tarifa)
        cantidad_de_tarifas += 1
        total_recaudado += tarifa
    else:
        print("Saldo insuficiente")
    
    tarifa = int(input("Ingrese tarifa o 0 para salir: "))

print("La cantidad de tarifas es: ", cantidad_de_tarifas)
print("Lo recaudado es: ", total_recaudado)
if cantidad_de_tarifas > 0:
    print("El promedio de tarifas es: ", total_recaudado / cantidad_de_tarifas)