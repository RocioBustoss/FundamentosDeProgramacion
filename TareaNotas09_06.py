total_notas = 0
lista_notas = []
for i in range(10):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i+1}: "))
            if(nota < 1.0 or nota > 7.0):
                print("Error, nota inválida.")
            else:
                total_notas = total_notas + nota
                lista_notas.append(nota)
                break
        except ValueError:
            print("Error, Debe ingresar una nota válida.")

promedio = total_notas / len(lista_notas)
print(f"\nEl promedio es: {promedio:.1f}")
lista_notas.sort()
print(f"\nLa peor nota es: {lista_notas[0]}")
print(f"\nLa mejor nota es: {lista_notas [9]}")

#print(f"\nLa peor nota es: {max{lista_notas}}")
#print(f"\nLa mejor nota es: {min{lista_notas}}")
