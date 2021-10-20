# Funcion de orden superior:
# Es una funcion que recibe como parametro otra funcion.

# Filter (retorna iterable)

    #Ejm: Tengo una lista y quiero solo num impares

my_list = [1,4,5,6,9,13,19,12]
odd = [i for i in my_list if i%2 != 0]

# Filter recibe una funcion y un iterable, por ejemplo una lista
# La funcion anonima recibe un x y retorna un boleano cumpliendo o no 
# la expresion. Es decir, filter itera en la lista y cada vez ejecuta
# la funcion cumpliendo o no con la condicion. Posteriormente convierte
# en lista todo.
odd_filter = list(filter(lambda x: x%2 != 0, my_list))
print(odd_filter)


# Map (retorna iterable)

    #Ejm. Tengo una lista y quiero convertir a todos los numeros
    # en su potencia al cuadrado. 

my_list_1 = [1,2,3,4,5]
square = [i**2 for i in my_list_1 ]

square_map = list(map(lambda k: k**2, my_list_1))
print(square_map)


#Reduce 

    #Ejm. Tengo una lista con muchos 2 repetivos
from functools import reduce 
my_list_2 = [2,2,2,2]
multiplied = reduce(lambda a,b: a*b, my_list_2)