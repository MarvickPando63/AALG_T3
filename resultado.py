
import random
import math

# Ingreso de datos
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
d = int(input("Ingrese el valor de d: "))
cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))

# Validación
if a <= 0 or b <= 0 or c <= 0 or d <= 0 or cantidad <= 0:
    print("Error: todos los valores deben ser mayores que cero")
    exit()

# Contadores
puntos_elipse = 0
puntos_interseccion = 0

# Generación de puntos aleatorios
for _ in range(cantidad):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)

    # Verificar si el punto pertenece a la elipse
    if (x**2)/(a**2) + (y**2)/(b**2) <= 1:
        puntos_elipse += 1

        # Verificar si también pertenece a la hipérbola
        if (x**2)/(c**2) - (y**2)/(d**2) >= 1:
            puntos_interseccion += 1

# Área de la elipse por fórmula
area_elipse = math.pi * a * b

# Método Monte Carlo basado en proporción
if puntos_elipse > 0:
    area_interseccion = (puntos_interseccion / puntos_elipse) * area_elipse
else:
    area_interseccion = 0

# Resultados
print("\n=========== RESULTADOS ===========")

print(f"Puntos dentro de la elipse: {puntos_elipse}")
print(f"Puntos en la intersección: {puntos_interseccion}")

print(f"\nÁrea de la elipse: {area_elipse:.6f}")
print(f"Área aproximada de la intersección: {area_interseccion:.6f}")
