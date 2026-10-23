def area(base, altura):
    resultado = base * altura / 2
    return resultado
def sumar(base, altura):
    resultado = base + altura
    return resultado

base = int(input("Ingrese la base? "))
altura = int(input("Ingrese la altura? "))

area_1 = area(base, altura)

base_2 = int(input("Ingrese la otra base? "))
altura_2 = int(input("Ingrese la otra altura? "))

area_2 = area(base_2, altura_2)

print("Área figura: ", area_1, "y", area_2, "cm2" )

resultado_suma = sumar(area_1, area_2)
print("La suma: ", resultado_suma, "cm2")
