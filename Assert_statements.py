# Otra forma de manejar errores 
# assert condicion, mensaje de error
def palindrome(string):
    assert len(string)>0, "No se puede ingresar una cadena vacia"
    return string == string[::-1]

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(int(num)))
    print("Terminó mi programa")
    


if __name__ == '__main__':
    run() 