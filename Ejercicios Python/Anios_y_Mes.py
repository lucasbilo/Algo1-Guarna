mes = input("Ingrese un mes:")
anio = int(input("ingrese un anio: "))

if mes in('abril', 'junio', 'septiembre', 'noviembre'):
    print(mes, "al anio", anio, "tiene 30 dias")
elif mes in('enero', 'marzo', 'mayo', 'julio', 'agosto', 'octubre', 'diciembre'):
    print(mes, "al anio", anio, "tiene 31 dias")
elif mes == 'febrero':
    if (anio % 4) == 0:
        if (anio % 100 != 0) or (anio % 100 == 0 and anio % 400 == 0):
            print(mes, "al anio", anio, "tiene 29 dias")
        else:
            print(mes, "al anio", anio, "tiene 28 dias")
    else:
        print(mes, "al anio", anio, "tiene 28 dias")
else:
    print("El mes no existe")
