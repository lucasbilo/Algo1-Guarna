def busqueada_binaria(lista, valor):
    primero = 0
    ultimo = len(lista) - 1
    encontrado = False
    while (encontrado == False) and (primero <= ultimo):
        medio = ((primero + ultimo) // 2)
        if (lista[medio] == valor):
            encontrado == True
        elif (lista[medio] < valor):
            primero = medio + 1
        else:
            ultimo = medio -1
        if encontrado == True:
            return medio
    return -1