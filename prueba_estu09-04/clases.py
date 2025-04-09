class Alumno:
    def __init__(self,nombre, carrera, calificación): # Se ocupa para definir propiedades a la clase, se crea el constructor
        self.nombre = nombre
        self.carrera = carrera
        self.calificación = calificación
    
    def imprimir_datos(self):
       print(" El nombre del estudiante es: ", self.nombre)
       print(" La carrera del estudiante es: ", self.carrera)
       print(" La calificación del estudiante es: ", self.calificación)

    def aprobado_reprobado(self ):
        if self.calificación >= 70:
            print(" El estudiante ha aprobado!!")
        else:
            print(" El estudiante a reprobado!!")








    


        


        
