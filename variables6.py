
# Muchos Valores a Múltiples Variables
# Python permite asignar valores a múltiples variables en una sola línea:

x, y, z = "Python", "Javascript", "C#"
print(x)
print(y)
print(z)

# Un valor para múltiples variables
# Puedes asignar el mismo valor a múltiples variables en una sola línea:

x = y = z = "Python"
print(x)
print(y)
print(z)

# Descomprimir una colección
# Si tienes una colección de valores en una lista, tupla, etc. Python te permite extraer los valores en variables. Esto se llama desempaquetar.

tecnologias = ["Python", "Javascript"]
x, y = tecnologias
print(x)
print(y)

