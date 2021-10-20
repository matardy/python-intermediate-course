import math

def main():
    my_dict = {}

    # Funciona con la logica de matriz
    
    for i in range(1,101):
        if i%3 !=0:
            #Llave       #Valor
            my_dict[i] = i**3

    # Dictionaries comprehensions
    my_new_dict = {i: i**3 for i in range(1,101) if i%3 != 0}
    
    sqrt_dict = {i: round(math.sqrt(i),2) for i in range(1,1001) }
    # key: value for value in iterable if condition

    print(sqrt_dict)
if __name__=='__main__':
    main()