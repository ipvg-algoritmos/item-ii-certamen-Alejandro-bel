# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código
cantidad_notas = int(input("¿Cuántas notas desea ingresar? "))

notas = []
for i in range(cantidad_notas):
    while True:
        try:
            nota = float(input(f"Ingrese la nota #{i + 1} (entre 1.0 y 7.0): "))
            if 1.0 <= nota <= 7.0:
                notas.append(nota)
                break
            else:
                print("Intente de nuevo.")
        except:
            print("Ingrese un número válido.")

promedio = round(sum(notas) / cantidad_notas, 2)

print(f"\nEl promedio es: {promedio}")
if promedio >= 4.0:
    print("Has aprobado.")
else:
    print("no has aprobado.")