class Curso:
    def __init__(self, nombre):
        self.alumnos = {}
        self.nombre = nombre
    
    def cantidad_alumnos(self):
        return len(self.alumnos)

    def ingresar_alumno_con_nota(self, alumno, nota):
        if not self.se_encuentra_el_alumno(alumno):
            self.alumnos[alumno] = []
        self.alumnos[alumno].append(nota)

    def promedio_del_alumno(self, alumno):
        if self.se_encuentra_el_alumno(alumno):
            return sum(self.alumnos[alumno]) / len(self.alumnos[alumno])

    def se_encuentra_el_alumno(self, alumno):
        return alumno in self.alumnos
    
    def nota_del_alumno(self, alumno):
        if self.se_encuentra_el_alumno(alumno):
            return self.alumnos[alumno]
    
    def __str__(self):
        return "Hola, este es un string representativo del curso con nombre" + self.nombre

    def listar_alumnos_con_notas(self):
        for alumno in self.alumnos:
            print("Alumno: {} y sus notas son: {}".format(alumno, self.alumnos[alumno]))

class CursoComputacion(Curso):
    def esta_aprobado(self, alumno):
        return self.promedio_del_alumno(alumno) >= 6

    def alumno_promociona(self, alumno):
        return self.promedio_del_alumno(alumno) >= 8

class CursoMatematica(Curso):
    def esta_aprobado(self, alumno):
        return self.promedio_del_alumno(alumno) >= 4

    def alumno_recursa(self, alumno):
        if self.se_encuentra_el_alumno(alumno):
            cant_notas_desaprobadas = 0
            for nota in self.alumnos[alumno]:
                if nota < 4:
                    cant_notas_desaprobadas += 1
            return cant_notas_desaprobadas >= 3

curso_de_pablo = CursoMatematica("Guarna")

curso_de_pablo.ingresar_alumno_con_nota("Uriel", 10)
curso_de_pablo.ingresar_alumno_con_nota("Juan", 2)
curso_de_pablo.ingresar_alumno_con_nota("Juan", 2)
curso_de_pablo.ingresar_alumno_con_nota("Juan", 4)

print(curso_de_pablo.nota_del_alumno("Uriel"))
print(curso_de_pablo.cantidad_alumnos())
print(curso_de_pablo.se_encuentra_el_alumno("Jorge"))
print(curso_de_pablo.nota_del_alumno("Nadie"))
print(curso_de_pablo.promedio_del_alumno("Juan"))

print(curso_de_pablo.listar_alumnos_con_notas())
print(curso_de_pablo.alumno_recursa("Juan"))
print(curso_de_pablo.alumno_recursa("Ju"))
print(curso_de_pablo.esta_aprobado("Uriel"))


