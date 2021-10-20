def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {
        'firstname': 'Stev',
        'lastname': 'Mendoza'
    }
    super_list = [
        {
        'firstname': 'Stev',
        'lastname': 'Mendoza'
        },
        {
        'firstname': 'Miguel',
        'lastname': 'Torres'
        },
        {
        'firstname': 'Susana',
        'lastname': 'Martinez'
        },

    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,4,3,0],
        "floating_nums": [3.2,5.4,5.3]
    }


    for key,value in super_dict.items():
        print(key, " - ", value)

    for i in super_list:
        print(i)

if __name__ == '__main__':
    run()