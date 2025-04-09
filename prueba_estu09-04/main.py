from clases import Alumno # importar la clase Alumno del archivo clases


estudiantes = [] # Se crea lista estudiantes

op = 0 # inicializo el operador en 0 para evitar errores a futuro


while op != 4:
    try:
        print(" BIENVENIDO AL SISTEMA!!") # menu de opciones para el usuario
        print(" 1- Agregar datos del estudiante")
        print(" 2- Imprimir datos del estudiante")
        print(" 3- Promedio del estudiante")
        print(" 4- Salir del programa")
        op = int(input("\nIngresa una opción (1-4): "))
        
        if op == 1: # Se agregan los datos y el numero de estudiantes los cuales se van a registrar
            num_estu = int(input(" Ingresa el número de estudiantes que deseas ingresar: "))
            for i in range(num_estu): # for para ingresar datos en base al numero de estudiantes ingresado por el usuario
                nombre = input("Digita un nombre: ")
                carrera = input("Ingresa la carrera del estudiante: ")
                
                calificacion = float(input("Ingresa tu calificación: "))
                if 0 < calificacion <= 100:
                    alumno = Alumno(nombre, carrera, calificacion) # Constructor de la clase Alumno 
                    estudiantes.append(alumno) #Se agregan  los datos a la lista
                else:
                    print("La calificación no entra en el rango permitido (0-100).")
            input("Presiona ENTER para continuar...") # simplemnete para que el usuario tenga qie ingresar una tecla para continuar

        elif op == 2:
            if estudiantes: # Se imprimen los datos de la lista estudiantes
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
                suma = sum(a.calificación for a in estudiantes) # se suman las calificaciones de los estudiantes para luego divirlas 
                promedio = suma / len(estudiantes)# por la longitud de los estudiantes (numero de estudiantes que se afregó)
                print(f"\n Promedio general de los estudiantes: {promedio:.2f}")
            else:
                print(" No hay estudiantes para calcular el promedio.")
            input("Presiona ENTER para continuar...")
            

        elif op == 4: # Sale del programa
            print("Saliendo del programa...")

        else:
            print("Opción no válida, por favor ingresa una opción entre 1 y 4.")
            input("Presiona ENTER para continuar...")

    except ValueError: # validación de datos 
        print("Entrada inválida. Asegúrate de ingresar un número válido.")
        input("Presiona ENTER para continuar...")
