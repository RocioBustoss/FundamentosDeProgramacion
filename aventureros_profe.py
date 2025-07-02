
def registrar_aventurero(lst_aventureros: dict, codigo: str, datos: list) -> bool:
    nombre, edad = datos
    if codigo not in lst_aventureros:
        lst_aventureros[codigo] = {
            "nombre" : nombre,
            "edad" :edad,
            "puntajes": []
        }
        return True
    return False


def registrar_puntaje(lst_aventureros: dict, codigo: str, puntaje: int) -> bool:
    if codigo in lst_aventureros:
        lst_aventureros[codigo]["puntajes"].append(puntaje)
        return True
    return False


def modificar_puntaje(lst_aventureros: dict, codigo: str, sesion: int, nuevo_puntaje: int) -> bool:
    if codigo in lst_aventureros and 0 <= sesion < len(lst_aventureros[codigo]["puntajes"]):
        lst_aventureros[codigo]["puntajes"][sesion] = nuevo_puntaje
        return True
    return False


def mostrar_participacion(lst_aventureros: dict):
    for codigo, datos in lst_aventureros.items():
        nombre = datos["nombre"]
        puntajes = datos["puntajes"]
        total = sum(puntajes)
        promedio = total / len(puntajes)
        if len(puntajes) > 0 :
            promedio = total / len(puntajes)
        else:
            promedio = 0
        print(f"{nombre}:({codigo}) - total: {total} - promedio: {promedio}")


def participacion_con_bajo_promedio( lst_avaentureros : dict, umbral : float):
    for codigo, datos in lst_avaentureros.tems():
        nombre = datos ["nombre"]
        puntajes = datos["puntajes"]
        if len(puntajes) > 0:
            promedio = sum(puntajes)/len(puntajes)
            if promedio < umbral:
                print(f"{nombre} {codigo} tiene un promedio de {promedio:.2f} que esta bajo el umbral")
            else:
                print("El promedio esta por sobre el umbral")

def listar_aventureros(lst_aventureros: dict):
    for codigo, datos in lst_aventureros.items():
        nombre = datos["nombre"]
        edad= datos["edad"]
        puntajes = datos["puntajes"]
        print(f"{nombre} {codigo} -edad: {edad} -puntajes: {puntajes}")

def obtener_aventureros_por_edad(lst_aventureros : dict,edad : int):
    print(f"Aventureros mayores a {edad}")
    for codigo, datos in lst_aventureros.items():
        nombre = datos["nombre"]
        edad_aventurero= datos["edad"]
        puntajes = datos["puntajes"]
        if edad_aventurero > edad:
            print(f"{nombre} {codigo} -edad: {edad} -puntajes: {puntajes}")






def main():
    aventureros = {}
    
    while True:
        print("\nBIENVENIDO AL CLUB DE AVENTUREROS")
        print("1. Registrar aventureros")
        print("2. Registrar puntajes")
        print("3. Modificar puntajes.")
        print("4. Ver participación total y promedio")
        print("5. Ver aventureros con bajo promedio")
        print("6. Listar aventureros por edad")
        print("7. Modificar puntajes.")
        print("0. Salir \n")
        
        op = input("Seleccione una opción: ")
        
        if op == "1":
            codigo = input("Ingrese codigo del aventurero: ")
            nombre= input("Ingrese el nombre del aventurero: ")
            edad =input("Ingrese la edad del aventurero: ")
            if registrar_aventurero(aventureros, codigo, [nombre,edad]):
                print("El aventurero fue registrado exitosamente.")
            else:
                print("El aventurero ya existe")
        
        
        elif op == "2":
            try:
                codigo = input("Ingrese codigo del aventurero: ")
                puntaje = int(input("Ingrese puntaje: "))
                if registrar_puntaje(aventureros, codigo, puntaje):
                    print("Puntaje registrado correctamente.")
                else:
                    print("No se pudo registrar el puntaje, codigo no encontrado.")
            except ValueError:
                print("Error, debe ingresar un nro")
        

        elif op == "3":
            codigo = input("Ingrese codigo del aventurero: ")
            try:
                sesion = int(input("Ingrese la sesion: "))
                nuevo_puntaje = int(input("Ingrese nuevo puntaje: "))
                if modificar_puntaje(aventureros, codigo, sesion, nuevo_puntaje):
                    print("Puntaje modificado correctamente")
            except ValueError:
                print("Sesion invalida.")
        
        
        elif op == "4":
            mostrar_participacion(lst_aventureros = dict)
        
        
        elif op == "5":
            try:
                umbral = float(input("Ingresa el umbral de promedio: "))
                participacion_con_bajo_promedio(aventureros,umbral)
            except ValueError:
                print("Umbral invalido")
        
        
        elif op == "6":
            listar_aventureros(aventureros)
        
        
        elif op == "7":
            try:
                edad = int(input("Ingrese el umbral de edad"))
                obtener_aventureros_por_edad(aventureros,edad)
            except ValueError:
                print("Edad invalida")
        
        
        elif op == "0":
            break
        
        
        else:
            print("Opcion no válida")
            
main()