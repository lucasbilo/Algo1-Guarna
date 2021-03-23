# 1. Hacer una función recursiva que devuelva la sumatoria desde 1 hasta un número n que se pase por parámetro.

"""def sumatoria(n):
    if n == 1:
        return 1
    return n + sumatoria(n-1)"""

# 2. Hacer una función recursiva que devuelva la suma de los elementos de una lista que se pasa por parámetro.

"""def sumatoria_listas(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] + sumatoria_listas(lista[1:])

l = [1, 2, 5, 8, 9, 5, 9, 9, 9]
print(sumatoria_listas(l))"""

# 3. Hacer una función recursiva que devuelva el valor de la sucesión de Fibonacci de un entero n. Nota: la serie de 0,
# devuelve 0, y la de 1 devuelve 1. Luego, devuelve la suma de los dos términos anteriores. Luego, hacerla de manera
# iterativa (mediante un ciclo). Comparar el rendimiento (tomar los tiempos) con la Serie en 5, 15, 30 y 60.

"""def fib_m(n):
    cache = {}
    if n <= 1:
        return 1
    if n not in cache:
        cache[n] = fib_m(n-1) + fib_m(n-2)
    return cache[n]

print(fib_m(5))
print(fib_m(15))
print(fib_m(30))
print(fib_m(60))"""

#4. Hacer una función recursiva que invierta un string que se pase por parámetro, y lo devuelva. Por ejemplo: CASA – ASAC.

"""def invertir(string):
    if len(string) == 1:
        return string[0]
    return string[-1] + invertir(string[:-1])

s = input('string: ')
print(invertir(s))"""