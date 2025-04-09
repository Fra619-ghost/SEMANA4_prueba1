from clases import Alumno


estudiantes = [] # Se lista estudiantes

op = 0 # inicializo el operador en 0 para evitar errores a futuro


while op != 4:
    try:
        print(" BIENVENIDO AL SISTEMA!!") # menu de opciones para el usuario
        print(" 1- Agregar datos del estudiante")
        print(" 2- Imprimir datos del estudiante")
        print(" 3- Promedio del estudiante")
        print(" 4- Salir del programa")
        op = int(input("\nIngresa una opción (1-4): "))
        
        if op == 1: # Se agregan los datos y el numero de estudiantes los cuiales se van a registrar
            num_estu = int(input(" Ingresa el número de estudiantes que deseas ingresar: "))
            for i in range(num_estu):
                nombre = input("Digita un nombre: ")
                carrera = input("Ingresa la carrera del estudiante: ")
                
                calificacion = float(input("Ingresa tu calificación: "))
                if 0 < calificacion <= 100:
                    alumno = Alumno(nombre, carrera, calificacion)
                    estudiantes.append(alumno) #Se agregan  los datos a la lista
                else:
                    print("La calificación no entra en el rango permitido (0-100).")
            input("Presiona ENTER para continuar...")

        elif op == 2:
            if estudiantes: # Se imprimen los datos de la lista estudianyes
                for alumno in estudiantes:
                    print("===============================================================")
                    alumno.imprimir_datos()
                    alumno.aprobado_reprobado()
                    print("===============================================================")
                input("Presiona ENTER para continuar...")
            else:
                print("Debe crear un perfil primero.")
                input("Presiona ENTER para continuar...")
        
        elif op == 3: # Se obtiene el promedio general
            if estudiantes:
                suma = sum(a.calificación for a in estudiantes)
                promedio = suma / len(estudiantes)
                print(f"\n Promedio general de los estudiantes: {promedio:.2f}")
            else:
                print(" No hay estudiantes para calcular el promedio.")
            input("Presiona ENTER para continuar...")
            

        elif op == 4: # Sale del programa
            print("Saliendo del programa...")

        else:
            print("Opción no válida, por favor ingresa una opción entre 1 y 4.")
            input("Presiona ENTER para continuar...")

    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número válido.")
        input("Presiona ENTER para continuar...")
