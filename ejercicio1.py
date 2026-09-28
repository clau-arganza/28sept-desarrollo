#Ejercicio 1: 

#Crear una clase "AlumnoDOO" para gestionar la nota de los alumnos.
#- La instancia de objetos recibe los argumentos nombre, apellido, email, nota_teoria y nota_practica.
#- La asignatura y la carrera se definen como atributos de clase: asignatura = "Desarrollo Orientado a Objetos", carrera = "Grado en Ingeniería Matemática".
#- La nota media ponderada se calcula (sobre 10) en función del porcentaje teoría:práctica 60:40, 
# siendo necesario haber sacado al menos un 4 en la parte teórica para que se tenga en cuenta la práctica en el cálculo de la nota final.

#- Deben generarse los siguientes métodos:
#    .- mostrarNota: devuelve el nombre completo y la nota media con un decimal y en formato texto (SS, AP, NT, SB)
#    .- modificarNota: permite subir o bajar la nota media del alumno


#Ejemplo de uso:

#alumno1 = AlumnoDOO("Sara", "Sánchez", 7,5)
#alumno1.mostrarNota()
#resultado: Sara Sánchez ha sacado un 6.2 (AP) en Desarrollo Orientado a Objetos de Grado en Ingeniería Matemática

class AlumnoDOO:
    asignatura = "Desarrollo Orientado a Objetos"
    carrera = "Grado en Ingeniería Matemática"

    def __init__(self, nombre, apellido, gmail, nota_teoria, nota_practica):
        self.nombre = nombre
        self.apellido = apellido
        self.gmail = gmail
        self.nota_teoria = nota_teoria
        self.nota_practica = nota_practica

        if self.nota_teoria >= 4:
            self.nota_media = self.nota_teoria * 0.6 + self.nota_practica * 0.4
        else:
            self.nota_media = self.nota_teoria

    def mostrarNota(self):
        if self.nota_media < 5:
            calificacion = "SS"
        elif self.nota_media < 7:
            calificacion = "AP"
        elif self.nota_media < 9:
            calificacion = "NT"
        else:
            calificacion = "SB"

        return (
            f"{self.nombre} {self.apellido} ha sacado un "
            f"{self.nota_media:.1f} ({calificacion}) en "
            f"{self.asignatura} de {self.carrera}"
        )

    def modificarNota(self, puntos):
        self.nota_media = max(0, min(10, self.nota_media + puntos))


# Crear un alumno y mostrar su nota
alumno1 = AlumnoDOO("Sara", "Sánchez", "sara.sanchez@gmail.com", 7, 5)
print(alumno1.mostrarNota())

# Subir la nota un punto y mostrarla
alumno1.modificarNota(1)
print(alumno1.mostrarNota())

# Bajar la nota dos puntos y mostrarla
alumno1.modificarNota(-2)
print(alumno1.mostrarNota())