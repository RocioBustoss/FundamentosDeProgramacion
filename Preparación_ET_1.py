def registrar_libro(libros: dict, estado: dict, codigo: str, datos: list) -> bool:
    if codigo not in libros:
        libros[codigo]= datos
        estado[codigo]=['disponible',None]
        return True
    else:
        return False

def prestar_libro(estado: dict, codigo: str, lector: str) -> bool:
    if codigo in estado:
        if estado[codigo][0] == "disponible":
            estado[codigo][0] = 'prestado'
            estado[codigo][1] = lector
            return True
        else:
            print("Libro ya esta prestado")
            return False
    else:
        return False
    
def devolver_libro(estado: dict, codigo: str) -> bool:
    if codigo in estado:
        if estado[codigo][0] == "prestado":
            estado[codigo][0] = 'disponible'
            estado[codigo][1] = None
            return True
        else:
            print("Libro no esta prestado")
            return False
    else:
        return False

def listar_disponibles(libros: dict, estado: dict) -> None:
    for id in libros:
        if estado[id][0] == "disponible":
            print(f"Libro: {id}, Titulo: {libros[id][0]}, Autor: {libros[id][1]}")



def listar_prestamos(libros: dict, estado: dict) -> None:
    for id in libros:
        if estado[id][0] == "prestado":
            print(f"Libro: {id}, Titulo: {libros[id][0]}, Autor: {libros[id][1]}, Lector: {estado[id][1]}")

            
def main():
    libros = {}
    estado = {}
    while True:
        print("------------------------------")
        print("-----SISTEMA DE GESTIÓN-----")
        print("1. Registrar libro.")
        print("2. Prestamo de libros.")
        print("3. Devolver un libro.")
        print("4. Libros disponibles.")
        print("5. Libros prestados.")
        print("6. Salir.")
        print("------------------------------")

        op = input("Seleccione una opción: ")
        if op == "1":
            try:
                codigo = input("Ingrese el codigo del libro: ")
                titulo = input("Ingrese el titulo del libro: ")
                autor = input("Ingrese el autor del libro: ")
                editorial = input("Ingrese la editorial del libro: ")
                año = int(input("Ingrese el año de publicación: "))
            except ValueError:
                print("Error, año inválido")
            datos =[titulo, autor, editorial, año]
            if codigo.strip() == "":
                print("Código no puede estar vacío.")
            else:
                if registrar_libro(libros, estado, codigo, datos):
                    print("Registro exitoso")
                else:
                    print("Libro ya existe.")


            
        elif op == "2":
            codigo = input("Ingrese el codigo del libro: ")
            lector = input("Ingrese el nombre del lector: ")
            if prestar_libro(estado, codigo, lector):
                print("Prestamo exitoso")
            else:
                print("Libro prestado o codigo inválido")


        elif op == "3":
            codigo = input("Ingrese el codigo del libro: ")
            if devolver_libro(estado, codigo):
                print("Devolución exitosa.")
            else:
                print("Libro no existe.")

        elif op == "4":
            listar_disponibles(libros, estado)
            
        elif op == "5":
            listar_prestamos(libros, estado)
            
        elif op == "6":
            print("Saliendo del programa...")
            break


main()