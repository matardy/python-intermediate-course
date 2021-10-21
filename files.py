def read():
    numbers = []
    # with es nuestro manejador contextual
    # impide que el archivo se rompa si se cierra 
    # inesperadamente
    # Con encoding podemos leer los signos de espaniol
    with open("./my_files/numbers.txt" , "r", encoding="utf-8") as f:
        for line in f: 
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Facundo", "Miguel", "Pepe", "Chris"]
    with open("./my_files/names.txt", "w", encoding="utf-8") as f:
        for name in names: 
            f.write(name)
            f.write("\n")



def main():
    write()


if __name__ == '__main__':
    main()