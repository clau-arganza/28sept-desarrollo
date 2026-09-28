#Ejercicio 2

#Crear una clase CestaFruta que gestiona una cesta de frutas.
#Se pueden instanciar n objetos que añaden una fruta y un número de piezas de dicha fruta,
# tal y como podemos añadir al hacer la compra.
#En cualquier momento se puede acceder a la cesta de fruta para ver en un formato diccionario que frutas hay dentro.
#Ejemplo resultado: {'manzanas': 2, 'peras': 2, 'cerezas': 5}

class CestaFruta:
    cesta = {}

    def __init__(self, fruta, piezas):
        if fruta in CestaFruta.cesta:
            CestaFruta.cesta[fruta] += piezas
        else:
            CestaFruta.cesta[fruta] = piezas


# Añadir frutas a la cesta
fruta1 = CestaFruta("manzanas", 2)
fruta2 = CestaFruta("peras", 2)
fruta3 = CestaFruta("cerezas", 5)

# Mostrar el contenido de la cesta
print(CestaFruta.cesta)