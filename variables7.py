# Variables globales
# Las variables que se crean fuera de una función se conocen como variables globales y pueden ser utilizadas dentro de las funciones como fuera de ellas.

x = "Sergie Code"

def miFuncion():
  print("Aprendé Python con " + x)

miFuncion()



# Si crea una variable con el mismo nombre dentro de una función, esta variable será local y sólo podrá utilizarse dentro de la función. La variable global con el mismo nombre permanecerá como estaba

x = "Python"

def miFuncion():
    x = "React"
    print("Aprendé" + x + "con Sergie Code")

miFuncion()
print("Aprendé" + x + "con Sergie Code")

