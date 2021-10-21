def main():
    squares = []
    # El ultimo parametro es no inclusivo
    # Esto podemos resolver mas eficiente con list comph
    for i in range (1,101):
        if i%3 != 0:
            squares.append(i**2)
        else:
            continue
    print(squares)

    # List comprehensions
    my_squares = [i**2 for i in range(1,101)]
    # [-element- for -element- in -iterable- if -condition]

    my_multiples = [i for i in range(1,99999) if i%4 == 0 and i%6==0 and i%9==0]
    print(my_squares)

if __name__ == '__main__':
    main()