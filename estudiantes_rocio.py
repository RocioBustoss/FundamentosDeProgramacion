
#estudiantes_rocio

def registrar_estudiante(lst_estudiantes: dict, rut: str, nombre: str):
    if rut not in lst_estudiantes:
        lst_estudiantes[rut] = {
            "nombre": nombre,
            "sesiones":[]
        }
        return True
    return False
    
def registrar_participacion(lst_estudiantes: dict, rut: str, puntaje: int):
    if rut in lst_estudiantes:
        lst_estudiantes[rut]["sesiones"].append(puntaje)
        return True
    return False

def actualizar_participacion(lst_estudiantes: dict, rut: str, sesion: int, nuevo_puntaje: int):
    if rut in lst_estudiantes:
        if sesion >= 0 and sesion < len(lst_estudiantes[rut]["sesiones"]):
            lst_estudiantes[rut]["sesiones"][sesion] = nuevo_puntaje
            return True
    return False

def calcular_total_y_promedio(lst_estudiantes: dict):
    for rut,datos in lst_estudiantes.items():
        nombre = datos["nombre"]
        puntajes = datos["sesiones"]
        total = sum(puntajes)
        promedio = total / len(puntajes)
        print(f"{nombre} RUT: {rut} Total: {total} Promedio: {promedio}")

def participacion_baja(lst_estudiantes: dict, umbral: float):
    for rut,datos in lst_estudiantes.items():
        nombre = datos["nombre"]
        puntajes = datos["sesiones"]
        total = sum(puntajes)
        promedio = total / len(puntajes)
        if promedio < umbral:
            print(f"Estudiantes por debajo del umbral: {nombre}")
def eliminar_estudiante(lst_estudiantes: dict, rut: str):
    if rut in lst_estudiantes:
        del lst_estudiantes[rut]
        return True
    return False

estudiantes = {}

def main():
    while True:
        print("\n-----------------------------")
        print("MENÚ")
        print("1. Rgistrar un nuevo estudiante")
        print("2. Registrar puntaje por sesión")
        print("3. Modificar un puntaje anterior")
        print("4. Ver todos los estudiantes con su total de puntajes y promedio")
        print("5. Ver estudiantes con baja participación")
        print("6. Salir")
        print("7. Eliminar estudiante")
        print("-----------------------------\n")

        opcion = input("Seleccione una opción: ")

        if(opcion =="1"):
            rut = input("Ingrese su RUT: ")
            nombre = input("Ingrese su nombre: ")
            if registrar_estudiante(estudiantes,rut,nombre):
                print("Registro exitoso")
            else:
                print("Estudiante ya registrado")
            
        elif(opcion =="2"):
            try:
                rut = input("Ingrese el rut: ")
                puntaje = int(input("Ingrese el puntaje: "))
                if registrar_participacion(estudiantes, rut, puntaje):
                    print("puntaje registrado exitosamente.")
                else:
                    print("Rut no existe")
            except ValueError:
                print("Error, debe ingresar un puntaje válido.")

        elif(opcion =="3"):
            try:
                rut = input("Ingrese el rut: ")
                sesion =int(input("Ingrese la sesión (desde 0): "))
                nuevo_puntaje = int(input("Ingrese el nuevo puntaje: "))
                if actualizar_participacion(estudiantes,rut,sesion,nuevo_puntaje):
                    print("Puntaje actualizado")
                else:
                    print("Rut o sesion no encontrado")
            except ValueError:
                print("Error, debe ingresar una sesion o puntaje válido.")
            
        elif(opcion =="4"):
            calcular_total_y_promedio(estudiantes)

        elif(opcion =="5"):
            try:
                umbral = float(input("Ingrese el umbral: "))
            except ValueError:
                print("Error, ingrese un umbral válido.")

            participacion_baja(estudiantes,umbral)
            
        elif(opcion == "6"):
            print("Terminando programa...")
            break
        
        elif (opcion == "7"):
            rut = input("Ingrese el rut: ")
            eliminar_estudiante(estudiantes,rut)
        else:
            print("la opcion es invalida")
main()